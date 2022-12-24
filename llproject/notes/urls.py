from django.urls import path

from . import views

urlpatterns = [
      path('notes', views.NoteListView.as_view(), name="notes.list"),
      #path('notes/<int:pk>', views.detail),
      path('notes/<int:pk>', views.NoteDetailView.as_view(),name="notes.detail" ),
      path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(),name="notes.update" ),
      #
      path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(),name="notes.delete" ),
      path('notes/new', views.NotesCreateView.as_view(),name="notes.new" ),
]
