import sqlite3
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from models import Note


class NotesDatabase:
    def __init__(self, db_name: str = 'notes.db'):
        self.db_name = db_name
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    is_favorite INTEGER DEFAULT 0
                )
            ''')
            conn.commit()

    def _dict_factory(self, cursor: sqlite3.Cursor, row: tuple) -> dict:
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    def get_all_notes(self) -> List[Note]:
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = self._dict_factory
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes')
            return [Note.from_dict(row) for row in cursor.fetchall()]

    def get_favorite_notes(self) -> List[Note]:
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = self._dict_factory
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes WHERE is_favorite = 1')
            return [Note.from_dict(row) for row in cursor.fetchall()]

    def add_note(self, note: Note) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO notes (id, title, content, created_at, is_favorite) VALUES (?, ?, ?, ?, ?)',
                (
                    str(note.id),
                    note.title,
                    note.content,
                    note.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    note.is_favorite
                )
            )
            conn.commit()

    def get_note_by_id(self, note_id: UUID) -> Optional[Note]:
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = self._dict_factory
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes WHERE id = ?', (str(note_id),))
            row = cursor.fetchone()
            return Note.from_dict(row) if row else None

    def toggle_favorite(self, note_id: UUID) -> None:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'UPDATE notes SET is_favorite = NOT is_favorite WHERE id = ?',
                (str(note_id),)
            )
            conn.commit()

    def delete_note(self, note_id: UUID) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM notes WHERE id = ?', (str(note_id),))
            conn.commit()
            return cursor.rowcount > 0

    def update_note(self, note_id: UUID, data: dict) -> bool:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT 1 FROM notes WHERE id = ?', (str(note_id),))
            if not cursor.fetchone():
                return False

            update_fields = []
            params = []
            if 'title' in data:
                update_fields.append('title = ?')
                params.append(data['title'])
            if 'content' in data:
                update_fields.append('content = ?')
                params.append(data['content'])
            if 'is_favorite' in data:
                update_fields.append('is_favorite = ?')
                params.append(1 if data['is_favorite'] else 0)
            
            if update_fields:
                params.append(str(note_id))
                cursor.execute(
                    f'UPDATE notes SET {", ".join(update_fields)} WHERE id = ?',
                    params
                )
                conn.commit()
                return True
            return False
