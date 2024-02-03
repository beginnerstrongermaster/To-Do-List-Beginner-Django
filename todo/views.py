from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from todo.models import Todo
from .forms import TodoForm, UserForm


# Create your views here.

# ToDoList
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todolist"

    # If the current user is admin, display all todos
    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        return Todo.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search") or ''
        # filter again based on what we just filtered, with title__icontains=search
        context['todolist'] = context['todolist'].filter(title__icontains=search)
        return context

# Todo Details
class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = "todo_detail.html"
    context_object_name = "todo"


# Todo Create
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'details', 'completed']
    template_name = "todo_edit.html"
    context_object_name = "form"
    success_url = reverse_lazy('todo-list')

    # Set logged-in user as selected user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Todo Update
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo_edit.html"
    fields = ['title', 'details', 'completed']
    context_object_name = "form"
    success_url = reverse_lazy('todo-list')

    # Set logged-in user as selected user
    def form_valid(self, form):
        # set default user to self.request.user
        form.instance.user = self.request.user
        return super().form_valid(form)


# Todo Delete
def TodoDeleteView(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo-list')


# Register
class UserCreateView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    context_object_name = "form"
    success_url = "login"


class UserLoginView(LoginView):
    template_name = "registration/login.html"


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect("login")
        else:
            return redirect("todo-list")
