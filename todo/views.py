from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from todo.models import Todo

# Create your views here.


def register(request):

    todo = request.POST.get('todo')
    if todo:
        Todo.objects.create(text=todo)

        return redirect('todo:todos_list')

    return render(
        request,
        'todo/register.html',
    )


def todos_list(request):

    todos = Todo.objects.all()

    return render(
        request,
        'todo/cars_list.html',
        context={
            'todos': todos
        }
    )


def update(request, todo_id):

    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == "POST":
        updated_todo = request.POST.get("todo")
        if updated_todo:
            todo.text = updated_todo
            todo.save()

            return redirect('todo:todos_list')

    return render(
        request,
        'todo/update.html',
        context={
            'todo': todo
        }
    )


@require_http_methods(["POST"])
def delete(request, todo_id):

    if request.method == "POST":
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()

    return redirect('todo:todos_list')
