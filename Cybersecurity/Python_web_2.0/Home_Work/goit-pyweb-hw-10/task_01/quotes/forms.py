#quotes/forms.py
from django import forms
from .models import Author, Quote

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        labels = {
            'fullname': 'Повне ім\'я',
            'born_date': 'Дата народження (напр. March 14, 1879)',
            'born_location': 'Місце народження',
            'description': 'Біографія / Опис',
        }

class QuoteForm(forms.ModelForm):
    # Кастомне поле для тегів (через кому)
    tags_input = forms.CharField(
        max_length=255,
        required=False,
        label="Теги (через кому)",
        help_text="Наприклад: life, success, motivation"
    )

    class Meta:
        model = Quote
        fields = ['text', 'author']
        labels = {
            'text': 'Текст цитати',
            'author': 'Автор',
        }
