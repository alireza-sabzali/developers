from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']


messages = {
    'required': 'لطفا این فیلد را پر کنید',
    'invalid': 'لطفا موارد معتبر وارد کنید',
    'max_length': 'تعداد کاراکترهای ورودی بیش از حد مجاز است',
    'min_length': 'تعداد کاراکترهای ورودی کمتر از حد مجاز است',
}


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, error_messages=messages)

