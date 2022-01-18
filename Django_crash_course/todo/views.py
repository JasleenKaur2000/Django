from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    context={
        "todo_list":todos
    }
    return render(request,"todo-list2.html",context)

#crud
def todo_detail(request,id):
    todo=Todo.objects.get(id=id)
    context={
        "todo":todo
    }
    return render(request,"todo_detail.html",context)


def todo_create(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        #name=form.cleaned_data['name'] #1
        #due_date=form.cleaned_data['due_date'] #2
        #print(name,due_date) #3
        #new_todo=Todo.objects.create(name=name,due_date=due_date) #4
        #the tasks done by lines 1,2,4 can be abstracted to just one line as below ,this is bcz we are using model form from django forms library
        form.save()  # it will create a Todo instance
        return redirect('/')
        
    context={"form":form}
    return render(request,"todo_create.html",context)

def todo_update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()  # it will create a Todo instance
        return redirect('/')
        
    context={"form":form}
    return render(request,"todo_update.html",context)

def todo_delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
