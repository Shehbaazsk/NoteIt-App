from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'notes/home.html'

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Note
    template_name = "notes/create.html"
    fields = ['note_title','note_body']
    success_url = reverse_lazy('notes:notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NotesView(LoginRequiredMixin,ListView):
    model=Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    login_url=reverse_lazy('accounts:login')

    def get_queryset(self):
        return Note.objects.all().filter(user=self.request.user).order_by("-updated_at")

class NotesDetailView(LoginRequiredMixin,DetailView):
    model=Note
    template_name = 'notes/details.html'
    context_object_name='note'

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = "notes/update.html"
    fields = ['note_title','note_body']
    success_url = reverse_lazy('notes:notes')

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = "notes/delete.html"
    success_url = reverse_lazy('notes:notes')
    context_object_name = 'note'
