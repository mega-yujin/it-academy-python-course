from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse

from .serializers import NoteSerializer
from notes.models import Note, Tag, NoteFile
from django.core.files.uploadedfile import SimpleUploadedFile


class NoteAPITest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser123',
        )
        self.tag = Tag.objects.create(name='Job')

        self.note = Note.objects.create(
            title='Test Note',
            content='Test note content',
            owner=self.user,
        )
        self.file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'test file content',
            content_type='text/plain',
        )
        auth_resp = self.client.post(
            reverse('token_obtain_pair'),
            {
                'username': 'testuser',
                'password': 'testuser123',
            }
        )
        self.token = auth_resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # self.client.force_authenticate(user=self.user)

    def test_get_notes(self):
        response = self.client.get(reverse('note-list'))
        notes = Note.objects.filter(owner=self.user)
        serializer = NoteSerializer(notes, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], serializer.data)

    def test_create_note_with_file(self):
        data = {
            'title': 'Note with File',
            'content': 'Content',
            'files': [self.file]
        }
        response = self.client.post(
            reverse('note-list'),
            data,
            format='multipart',
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(NoteFile.objects.count(), 1)

    def test_unauthorized_access(self):
        self.client.credentials()
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, 401)
