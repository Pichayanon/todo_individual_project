from django.views.generic import TemplateView
from todo.models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoListView(LoginRequiredMixin, TemplateView):
    """
    View to display categorized todo tasks for the authenticated user.

    Attributes:
        template_name (str): The HTML template for the todo list page.
    """
    template_name = 'todo/todo_list.html'

    def get_context_data(self, **kwargs):
        """Adds categorized todos to the context."""
        context = super().get_context_data(**kwargs)
        context['pending_todos'] = Todo.objects.filter(status='Pending', user=self.request.user)
        context['inprogress_todos'] = Todo.objects.filter(status='In Progress', user=self.request.user)
        context['done_todos'] = Todo.objects.filter(status='Done', user=self.request.user)
        return context
