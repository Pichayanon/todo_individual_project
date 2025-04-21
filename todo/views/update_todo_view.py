from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Todo


class UpdateStatusView(LoginRequiredMixin, View):
    """View for updating the status of an existing todo task."""

    def post(self, request, todo_id):
        """
        Updates the status of the todo task if the new status is valid.
        Redirects to the todo list page after deletion.
        """
        todo = get_object_or_404(Todo, id=todo_id, user=request.user)
        new_status = request.POST.get('status')
        if new_status in dict(Todo.STATUS_CHOICES):
            todo.status = new_status
            todo.save()
        return redirect('todo_list')
