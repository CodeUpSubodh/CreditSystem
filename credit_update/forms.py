from django import forms
from .models import UserResponse, Question

class UserResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f"question_{question.id}"] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    ('A', question.answer_a),
                    ('B', question.answer_b),
                    ('C', question.answer_c),
                    ('D', question.answer_d),
                ],
                widget=forms.RadioSelect,
            )
