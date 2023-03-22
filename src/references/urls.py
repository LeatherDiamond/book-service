from django.urls import path
from . import views

app_name = "references"
urlpatterns = [

    #Authors URLs

    path('author_preview/<int:pk>/', views.ShowAuthor.as_view(), name='author_detail'),
    path('author_create/', views.CreateAuthor.as_view(), name='author_create'),
    path('author_update/<int:pk>/', views.UpdateAuthor.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', views.DeleteAuthor.as_view(), name='author_delete'),
    path('authors_list/', views.ShowAuthors.as_view(), name='authors_list'),
]