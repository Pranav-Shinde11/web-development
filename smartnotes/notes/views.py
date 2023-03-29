from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect

#for class based view
from django.views.generic import  CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit  import DeleteView
#fro authentication & to keep privacy
from django.contrib.auth.mixins import LoginRequiredMixin
 
 
 # calling form class from notes
from  .forms import NotesForm
from . models import notes

class NotesDeleteView(DeleteView):
    model = notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = notes
    success_url = '/smart/notes'
    # calling form class from notes
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self,form):
        self.object =form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())





class NoteListView(LoginRequiredMixin,ListView):
    model = notes
    context_object_name = "notes"
    # optional
    template_name = "notes/notes_list.html"
    login_url = "/admin"


    def get_queryset(self):
        return self.request.user.notes.all()





class NoteDetailView(DetailView):
    model = notes
    context_object_name = "note"
    













'''
def list (request):
    all_notes = notes.objects.all()
    return render (request,'notes/notes_list.html',{'notes':all_notes} )

def detail(request,pk):
    try:
       note = notes.objects.get(pk=pk)
    except notes.DoesNotExist:
        raise Http404(" note does not exist")
    return render (request, 'notes/notes_detail.html',{'note':note})
'''