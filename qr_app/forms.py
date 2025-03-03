from django import forms

class QRCodeForm(forms.Form):
    text = forms.CharField(label="Enter text, URL, or number", max_length=255)
