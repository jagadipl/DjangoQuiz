from django.shortcuts import render
from .models import Question
# Create your views here.
def homepage(request):
    questions = Question.objects.all()
    if request.method == "POST":
        score = 0
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_answer:
                score+=1
        return render(request, 'quizapp/results.html', {
            'score': score,
            'total': len(questions)

        })        
    return render(request,'quizapp/quiz.html',{'questions': questions})


def index(request):
    return render(request,'quizapp/index.html')

def result(request):
    return render(request,'quizapp/result.html')