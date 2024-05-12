from django import forms
from .models import Calculator

class BlockForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = ('width', 'height', 'length','concrete_type')

class QuestionForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=100)
    email = forms.EmailField(label='Е-mail')
    phone_number = forms.CharField(label='Номер телефона', max_length=20)
    question = forms.CharField(label='Питання', widget=forms.Textarea)

class QuickContactForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea)