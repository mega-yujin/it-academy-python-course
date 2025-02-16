from rest_framework import serializers
from notes.models import Note, NoteFile, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'description')


class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteFile
        fields = ('id', 'file', 'uploaded_at')


class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    files = NoteFileSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'created_at', 'is_favorite', 'owner', 'tags', 'files')
        read_only_fields = ('created_at', 'owner')


class NoteCreateSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)
    files = serializers.ListField(
        child=serializers.FileField(max_length=1000000, allow_empty_file=False),
        required=False,
        write_only=True,
    )

    class Meta:
        model = Note
        fields = ('title', 'content', 'is_favorite', 'tags', 'files')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        files_data = validated_data.pop('files', [])
        note = Note.objects.create(**validated_data)

        if tags_data:
            note.tags.set(tags_data)

        for file in files_data:
            NoteFile.objects.create(note=note, file=file)

        return note

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        files_data = validated_data.pop('files', [])

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        if tags_data:
            instance.tags.set(tags_data)

        for file in files_data:
            NoteFile.objects.create(note=instance, file=file)

        return instance
