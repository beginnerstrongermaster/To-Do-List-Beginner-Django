from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from ToDoListPro import settings
from todo import views

urlpatterns = [
    path('',views.TodoListView.as_view(),name='todo-list'),
    path('todo/detail/<int:pk>',views.TodoDetailView.as_view(),name='todo-detail'),
    path('todo/add/',views.TodoCreateView.as_view(),name='todo-add'),
    path('todo/update/<int:pk>',views.TodoUpdateView.as_view(),name='todo-update'),
    path('todo/delete/<int:pk>',views.TodoDeleteView,name='todo-delete'),
    path('register/',views.UserCreateView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)