# from django import template
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# from django.template import Template, loader
from .models import Question

"""
Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. 
The rest is up to you.

"""


# returns last 5 most recent questions
# def index(request):
#     latest_question_list: list[Question] = Question.objects.order_by("-pub_date")[:5]
#     template: Template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


# shorter way of providing context to template and sending a HttpResponse - handles /polls
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# when we click on question - handles /polls/<nos>/
# def detail(request: HttpRequest, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         return Http404("Question does not exist")
#     return render(request, "polls/details.html", {"question": question})


def detail(request: HttpRequest, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "polls/details.html", {"question": question})


# when we navigate to a question - handles /polls/<nos>/results
def results(request, question_id):
    response = f"You are looking for question {question_id}"
    return HttpResponse(response)


# when we vote on a question - handles /polls/<nos>/vote
def vote(request, question_id):
    return HttpResponse(f"You are voting on the question {question_id}")
