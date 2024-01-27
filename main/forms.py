from django import forms

from main.models import Student, Subject


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar', 'email',)
        # exclude = ('is_activ',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('почта должна относиться к учебному заведению')

        return cleaned_data


class SubjectForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
