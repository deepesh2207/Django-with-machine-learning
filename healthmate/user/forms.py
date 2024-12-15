from django import forms

class ApprovalForm(forms.Form):
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    pmTwoPointFive = forms.FloatField()
    pmTen = forms.FloatField()
    nitrogendioxide = forms.FloatField()
    sulphurdioxide = forms.FloatField()
    carbonmonxide = forms.FloatField()
    Proximity_to_Industrial_Areas = forms.FloatField()
    Population_Density = forms.IntegerField()