from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import TodoListView, AddTodoView, UpdateStatusView, EditTodoView, DeleteTodoView, SignupView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('add/', AddTodoView.as_view(), name='add_todo'),
    path('update/<int:todo_id>/', UpdateStatusView.as_view(), name='update_status'),
    path('delete/<int:todo_id>/', DeleteTodoView.as_view(), name='delete_todo'),
    path('edit/<int:todo_id>/', EditTodoView.as_view(), name='edit_todo'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
