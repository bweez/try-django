from dataclasses import fields
from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title_icontains=title)
        if qs.exists():
            self.add_error('title', f"{title} already exists")

        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # This is an override for a function that is apart of
    # the form.Form model that this class inherits from.
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        return title
