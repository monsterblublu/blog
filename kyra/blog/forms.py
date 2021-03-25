from django import forms
from django_summernote.fields import SummernoteTextFormField
from .models import Article

class ArticleForm(forms.ModelForm):
    text = SummernoteTextFormField()
    class Meta:
        model = Article
        fields = ('title','snippet','thumbnail','author','text')

        widgets = {
            'author': forms.TextInput(attrs={'id':'author-name','value':'','placeholder':' ','readonly':''}),
        }
