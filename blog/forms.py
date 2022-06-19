from .models import Articles,Contacts
from django.forms import ModelForm,TextInput,EmailInput,Textarea,NumberInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','email','text']

        widgets = {
            'title':TextInput(attrs={
                'class':'comments__input comments__input--name',
                'placeholder':'Имя пользователя',

            }),
            'email': EmailInput(attrs={
                'class': 'comments__input comments__input--email',
                'placeholder': 'Email',

            }),
            'text': Textarea(attrs={
                'class': 'comments__textarea',
                'placeholder': 'Текст коментарии',

            }),
        }

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['title', 'email', 'phone_number', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'contacts__input',
                'placeholder': 'Имя пользователя',

            }),
            'email': EmailInput(attrs={
                'class': 'contacts__input',
                'placeholder': 'name@gmail.com',

            }),
            'phone_number': TextInput(attrs={
                'class': 'contacts__input',
                'placeholder': '+998 99 000 00 00',
            }),
            'text': Textarea(attrs={
                'class': 'contacts__textarea',
                'placeholder': 'Напишите текст',

            }),
        }


