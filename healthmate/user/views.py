from django.shortcuts import render
from django.http import JsonResponse
from user.forms import ApprovalForm
import pandas as pd
from joblib import load

with open(r"C:\Users\Deepesh\Downloads\Django with machine learning\healthmate\user\gradient_boost_model.joblib", "rb") as file:
    loaded_gradient_boost_model = load(file)

with open(r"C:\Users\Deepesh\Downloads\Django with machine learning\healthmate\user\gradient_boost_model.joblib", "rb") as file:
    scaler = load(file)

def approvereject(input_data):
    try:
        feature_keys = [
            "Temperature", "Humidity", "PM2.5", "PM10", "NO2", "SO2", 
            "CO", "Proximity_to_Industrial_Areas", "Population_Density"
        ]
        input_features = [float(input_data.get(key, 0)) for key in feature_keys]
        scaled_features = scaler.transform([input_features])
        prediction = loaded_gradient_boost_model.predict(scaled_features)
        return prediction[0]
    except Exception as e:
        print("Prediction Error:", str(e))
        return None

def form_approval(request):
    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            input_data = {
                "Temperature": form.cleaned_data['temperature'],
                "Humidity": form.cleaned_data['humidity'],
                "PM2.5": form.cleaned_data['pmTwoPointFive'],
                "PM10": form.cleaned_data['pmTen'],
                "NO2": form.cleaned_data['nitrogendioxide'],
                "SO2": form.cleaned_data['sulphurdioxide'],
                "CO": form.cleaned_data['carbonmonxide'],
                "Proximity_to_Industrial_Areas": form.cleaned_data['Proximity_to_Industrial_Areas'],
                "Population_Density": form.cleaned_data['Population_Density'],
            }
            prediction = approvereject(input_data)
            print("Input Data:", input_data)
            print("Prediction:", prediction)
    form = ApprovalForm()
    return render(request, 'index.html', {'form': form})
