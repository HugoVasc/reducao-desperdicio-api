from django import forms

class CEPField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 9)
        super().__init__(*args, **kwargs)
    
    def clean(self, value):
        value = super().clean(value)
        if not value.isdigit() or len(value) != 8:
            raise forms.ValidationError("CEP inválido")
        return value