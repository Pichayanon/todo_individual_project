from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Todo
from todo.forms import TodoForm


class EditTodoView(LoginRequiredMixin, View):
    """View to handle editing an existing task."""

    def get(self, request, todo_id):
        """Displays a form pre-filled with the task current data."""
        todo = get_object_or_404(Todo, id=todo_id, user=request.user)
        form = TodoForm(instance=todo)
        return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})

    def post(self, request, todo_id):
        """
        Updates the todo task with the submitted data if the form is valid.
        Redirects to the todo list page after saving.
        """
        todo = get_object_or_404(Todo, id=todo_id, user=request.user)
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})
