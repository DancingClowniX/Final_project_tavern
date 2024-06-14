from django import forms
from django.core.exceptions import ValidationError

from feedback.models import Feedback


# class UserForm(forms.Form):
#     name = forms.CharField() # -> html input
#     age = forms.IntegerField(required=False)
def example_validation():
    pass


def check_blocker_symbols(text):
    blocker_symbols = ['<', '>', '=']# список недопустимых символов
    for symbol in blocker_symbols:
        if symbol in text:
            raise ValidationError("Запрещенные символы")
    return text
class AddFeedbackForm(forms.ModelForm):
    text = forms.CharField(
        label='ваш текст для отзыва',
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}),
        required=False, # поле необязательное к заполнению
        validators=[check_blocker_symbols]
    )
    error_css_class = "error"
    rating = forms.IntegerField(
        label='Оценка',
        max_value=5,
        min_value=0
    )
    class Meta:
        model = Feedback

        fields = '__all__' # ['text', 'rating']

    # не требует самостоятельного вызова
    def clean_text(self):  # clean_атрибут_формы, Django в момент валидации формы сам вызывает Form
        text = self.cleaned_data['text']
        if not ('А' in text) and text != '':
            raise ValidationError('А русская нет в строке')
        return text
