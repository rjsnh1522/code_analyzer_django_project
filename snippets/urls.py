
from django.urls import path, include
from . import views

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetIndexView.as_view(), name='index'),
    path('list', views.SnippetListView.as_view(), name='index'),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='detail'),
    path('check_code_language/', views.SnippetCheckView.as_view(), name='check_code_language')
]
