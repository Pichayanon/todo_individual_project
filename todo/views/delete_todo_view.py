from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Todo


class DeleteTodoView(LoginRequiredMixin, View):
    """View to handle the deletion of a todo task."""

    def get(self, request, todo_id):
        """
        Deletes the todo task with the given ID that belongs to the current user.
        Redirects to the todo list page after deletion.
        """
        todo = get_object_or_404(Todo, id=todo_id, user=request.user)
        todo.delete()
        return redirect('todo_list')
