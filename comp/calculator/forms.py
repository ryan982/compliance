from django import forms

class Calculate(forms.Form):
    amount = forms.FloatField()
    gst = forms.FloatField()
    tds = forms.FloatField()