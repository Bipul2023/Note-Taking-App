
from django.urls import path
from .views import CreateNote, NotesDetail ,SearchNote, UpdateNote, NotesList


urlpatterns = [
    path("notes", NotesList.as_view(), name = "notes_list"),
    path("create-note", CreateNote.as_view() , name="create_note"),
    path("note/<uuid:pk>", NotesDetail.as_view(), name="note_detail"),
    path("search-notes", SearchNote.as_view(), name= "search_note"),
    path("update-note/<uuid:pk>", UpdateNote.as_view(), name= "update_note" ),
]
