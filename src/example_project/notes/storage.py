from uuid import UUID

from notes.dto_models import Note
from uuid import uuid4

note_1 = Note(
    id=uuid4(),
    title='Погода',
    content='Weather is bad',
)

note_2 = Note(
    id=uuid4(),
    title='Расписание',
    content='Сеголня занятие',
)

note_3 = Note(
    id=uuid4(),
    title='Чего купить',
    content='Чупа-чупс',
)

NOTES_STORAGE: dict[UUID, Note] = {
    note_1.id: note_1,
    note_2.id: note_2,
    note_3.id: note_3,
}
