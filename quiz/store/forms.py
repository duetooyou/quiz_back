from django import forms


class QuestionFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        correct_array = []
        for data in self.cleaned_data:
            correct_array.append(data['correct'])
        if all(correct_array) or not any(correct_array):
            raise forms.ValidationError('Все значения ответов не могут быть верными'
                                        ' и должен быть указан как минимум один верный ответ')
