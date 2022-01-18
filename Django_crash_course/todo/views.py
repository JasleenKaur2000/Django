from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    context={
        "todo_list":todos
    }
    return render(request,"todo-list2.html",context)

