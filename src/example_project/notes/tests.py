from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from django.utils.datastructures import MultiValueDict

from unittest.mock import patch, Mock

from .models import Note, Tag, NoteFile
from .forms import NoteForm


class NoteModelTest(TestCase):
    """Тест проверяет модель Note."""
    def setUp(self) -> None:
        # self.client = Client()
        self.user = User.objects.create(
            username='testuser',
            password='testpass123',
        )
        self.note = Note.objects.create(
            title='Test note',
            content='Test note content',
            owner=self.user,
        )
        self.tag = Tag.objects.create(
            name='Job',
            description='job notes',
        )
        self.note.tags.add(self.tag)

    def test_note_creation(self):
        """Note creation test."""
        self.assertEqual(self.note.title, 'Test note')
        self.assertEqual(self.note.content, 'Test note content')
        self.assertEqual(self.note.owner, self.user)
        self.assertIn(self.tag, self.note.tags.all())
        self.assertFalse(self.note.is_favorite)

    def test_note_str(self):
        """Note str test."""
        self.assertEqual(str(self.note), 'Test note')


class NoteViewTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='testuser',
            password='testpass123',
        )
        permission = Permission.objects.get(codename='can_mark_as_fav')
        self.user.user_permissions.add(permission)

        # self.client.login(username='testuser', password='testpass123')
        self.client.force_login(user=self.user)

        self.note = Note.objects.create(
            title='Test note',
            content='Test note content',
            owner=self.user,
        )
        self.tag = Tag.objects.create(
            name='Job',
            description='job notes',
        )
        self.note.tags.add(self.tag)

    def test_index_view(self):
        """Home page test."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')
        self.assertContains(response, 'Test note')

    def test_note_detail(self):
        """note detail page test."""
        response = self.client.get(
            reverse('note_detail', kwargs={'pk': self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_create_note(self):
        """Note creation test."""
        response = self.client.post(
            reverse('note_create'),
            {
                'title': 'New test note',
                'content': 'New test note content',
            }
        )
        self.assertEqual(Note.objects.count(), 2)
        new_note = Note.objects.get(title='New test note')
        self.assertEqual(new_note.owner, self.user)


class NoteFormTest(TestCase):

    def setUp(self) -> None:
        self.tag = Tag.objects.create(
            name='Job',
            description='job notes',
        )
        self.valid_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'test file content',
            content_type='text/plain',
        )

        self.invalid_file = SimpleUploadedFile(
            name='test_file.xyz',
            content=b'test file content',
            content_type='text/plain',
        )

    def test_valid_form(self):
        form_data = {
            'title': 'Test note',
            'content': 'Test note content',
            'tags': [self.tag]
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'content': 'Test note content',
            'tags': [self.tag]
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_file_upload(self):
        form_data = {
            'title': 'Test note with file',
            'content': 'Test note content',
        }
        file_data = MultiValueDict({'files': [self.valid_file]})
        form = NoteForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())

    def test_invalid_file_upload(self):
        form_data = {
            'title': 'Test note with file',
            'content': 'Test note content',
        }
        file_data = MultiValueDict({'files': [self.invalid_file]})
        form = NoteForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())


class ShareNoteView(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='testuser',
            password='testpass123',
        )
        self.note = Note.objects.create(
            title='Test note',
            content='Test note content',
            owner=self.user,
        )
        self.client.force_login(user=self.user)

    @patch('logging.info')
    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_share_note_success(self, mock_send: Mock, mock_log_info: Mock):
        url = reverse('share_note', args=[self.note.pk])
        data = {
            'email': 'recipient@example.com',
            'message': 'Test message'
        }

        # mock_send.return_value = 1

        response = self.client.post(url, data)
        self.assertTrue(mock_send.called)
        mock_log_info.assert_called_once_with('Заметка успешно отправлена на recipient@example.com')

    @patch('logging.warning')
    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_share_note_failure(self, mock_send: Mock, mock_log_warning: Mock):
        url = reverse('share_note', args=[self.note.pk])
        data = {
            'email': 'recipient@example.com',
            'message': 'Test message'
        }
        mock_send.side_effect = Exception('Email sanding failed')
        response = self.client.post(url, data)
        self.assertTrue(mock_send.called)
        mock_log_warning.assert_called_once_with('Произошла ошибка при отправке заметки Email sanding failed. Попробуйте позже.')
