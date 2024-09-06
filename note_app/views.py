from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import NoteSerializer
from .models import Note


# Create your views here.


class NotesList(APIView):
    def get(self, request):
        notes = Note.objects.all()
        notes_ser = NoteSerializer(notes, many = True)
        return Response(notes_ser.data, status=status.HTTP_200_OK)



class CreateNote(APIView):

    def post(self, request):
        data = request.data
        note_ser = NoteSerializer(data = data)
        if note_ser.is_valid():
            note_ser.save()
            return Response(note_ser.data, status= status.HTTP_201_CREATED)
        return Response(note_ser.errors, status= status.HTTP_400_BAD_REQUEST)
    

class NotesDetail(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note_ser = NoteSerializer(note)
        return Response(note_ser.data)
    

class SearchNote(APIView):

    def get(self,request):
        title = request.query_params.get('title', None)
        if title:
            notes = Note.objects.filter(title__icontains = title)
            if notes:
                notes_ser = NoteSerializer(notes, many = True)
                return Response(notes_ser.data, status= status.HTTP_200_OK)
            return Response({'detail': 'Not Found'}, status= status.HTTP_404_NOT_FOUND)

        return Response({'detail': "Provide title query"}, status= status.HTTP_400_BAD_REQUEST)
    
class UpdateNote(APIView):

    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note_ser = NoteSerializer(note, data = request.data)
        if note_ser.is_valid():
            note_ser.save()
            return Response(note_ser.data)
        return Response(note_ser.errors, status=status.HTTP_400_BAD_REQUEST)
