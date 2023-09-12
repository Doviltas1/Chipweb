from django import forms

class Cars (forms.Form):
    Marke = forms.CharField(max_length=50)
    Model = forms.CharField(max_length=50)
    Engine = forms.CharField(max_length=50)
    Year = forms.CharField(max_length=50)
    kw = forms.CharField(max_length=50)
    kWA = forms.CharField(max_length=50)
    nM = forms.CharField(max_length=50)
    nMA = forms.CharField(max_length=50)
    Price = forms.CharField(max_length=50)
    Fuel = forms.CharField(max_length=50)


class CarsS (forms.Form):
    Marke = forms.CharField(max_length=50)