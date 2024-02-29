from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Имя пользователя должно состоять максимум из 150 символов', widget=forms.TextInput(attrs={'class': "form-control", 'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'published', 'category']
        widget = {
            'title': forms.TextInput(attrs={
                'class': 'forms-control'
                }),
            'content': forms.Textarea(attrs={
                'class': 'forms-control',
                'rows': 5
                }),
            'category': forms.Select(attrs={
                'class': 'forms-control'
                })
        }


    # title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
    #     'class': 'forms-control'
    # }))
    # content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
    #     'class': 'forms-control',
    #     'rows': 5
    # }))
    # published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={
    #     'class': 'forms-control'
    # }))


