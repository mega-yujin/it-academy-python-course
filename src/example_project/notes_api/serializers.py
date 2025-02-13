from rest_framework import serializers
from notes.models import Note, NoteFile, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')
