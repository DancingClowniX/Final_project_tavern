from django import forms
from feedback.models import Feedback


class AddFeedbackForm(forms.ModelForm):
    text = forms.CharField(
        label='ваш текст для отзыва',
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 10, 'class': 'form-input'}),
    )
    error_css_class = "error"
    rating = forms.IntegerField(
        label='Оценка',
        max_value=5,
        min_value=0
    )
    class Meta:
        model = Feedback
        fields = ['text', 'rating']


