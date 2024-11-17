from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserResponse
from .forms import UserResponseForm
from .utils import calculate_credit_score

@login_required
def credit_score_form(request):
    questions = Question.objects.all()
    if request.method == "POST":
        responses = []
        for question in questions:
            answer = request.POST.get(f"question_{question.id}")
            if answer:
                responses.append(UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    answer=answer
                ))
        score = calculate_credit_score(responses)
        return redirect('credit_score_result', score=score)

    form = UserResponseForm(questions=questions)
    return render(request, 'credit_update/form.html', {'form': form})

@login_required
def credit_score_result(request, score):
    return render(request, 'credit_update/result.html', {'score': score})
