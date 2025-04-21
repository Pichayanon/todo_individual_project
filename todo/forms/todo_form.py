from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    """
    Form for creating and editing todo tasks.

    Fields:
        title (CharField): Title of the todo task.
        description (TextField): Optional detailed description.
        photo (CloudinaryField): Optional image associated with the task.
        due_at (DateTimeField): Optional due date and time for the task.
    """
    class Meta:
        model = Todo
        fields = ["title", "description", "photo", "due_at"]
        widgets = {
            "due_at": forms.TextInput(attrs={'placeholder': 'Select date and time'}),
        }

    def __init__(self, *args, **kwargs):
        """Initialize the form and apply Bootstrap 5 classes to all fields."""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
