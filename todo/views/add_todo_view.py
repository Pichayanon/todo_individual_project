from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from todo.models import Todo
from todo.forms import TodoForm


class AddTodoView(LoginRequiredMixin, CreateView):
    """
    View for creating a new todo task.

    Attributes:
        model (Todo): The Todo model used for creating a new entry.
        form_class (TodoForm): The form used to input todo data.
        template_name (str): The HTML template for the add todo page.
        success_url (str): The URL to redirect to after successful creation.
    """
    model = Todo
    form_class = TodoForm
    template_name = 'todo/add_todo.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        """Sets the current user as the task owner before saving."""
        form.instance.user = self.request.user
        return super().form_valid(form)
