from django.urls import path

from . import views


# used to differntiate routes between other apps
app_name = "todo"
urlpatterns = [
    path("",views.todo_index,name="todo_index")
]
