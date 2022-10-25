from django.urls import path
from .views import HomeView,NotesView,NotesDetailView,NotesUpdateView,NotesCreateView,NotesDeleteView

app_name = 'notes'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('add/',NotesCreateView.as_view(),name='create'),
    path('notes/',NotesView.as_view(),name='notes'),
    path('notes/<int:pk>/',NotesDetailView.as_view(),name='details'),
    path('edit/<int:pk>/',NotesUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',NotesDeleteView.as_view(),name='delete'),
]
