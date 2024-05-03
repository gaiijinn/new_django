from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя получателя',
        'type': 'text',
    }), required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'lastName',
        'placeholder': 'Введите фамилию получателя',
        'type': 'text'
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'you@example.com',
        'type': 'email'
    }), required=True)

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'placeholder': 'Украина, Житомир, шевченко 107',
        'type': 'text'
    }), required=True)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
