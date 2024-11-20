from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo.models import User

# Create your views here.


def todo_index(req):
    return HttpResponse("index page of todo app")


def todo_show_all_users(req):
    all_users = User.objects.all()
    return render(req, "todo/showall.html", {"users": all_users})


