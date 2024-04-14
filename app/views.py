from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import *

def index(request):
    questions = Question.objects.order_by("date")[:5]
    context = {"questions": questions}
    return render(request, "app/index.html", context)

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "app/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app/results.html", {"question": question})


def vote(request , pk):
     question = get_object_or_404(Question, pk=pk)
     try :
         choice = question.choice_set.get(pk= request.POST.get('choice'))
         
     except (KeyError , Choice.DoesNotExist):
         context = {'question':question , 'error_message': 'you didnt select a choice' }
         return render(request , 'app/detail.html' ,  context)        
     else: 
         choice.votes = F('votes') + 1
         choice.save()
         return HttpResponseRedirect(reverse("results", args=(question.id,)))

                

