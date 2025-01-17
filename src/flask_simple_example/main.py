from flask import Flask, render_template
from dataclasses import dataclass
from uuid import uuid4, UUID
from datetime import datetime


@dataclass
class Note:
    id: UUID
    title: str
    content: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_favorite: bool = False


note_1 = Note(
    id=uuid4(),
    title='Погода',
    content='Weather is bad',
    created_at='2025-01-15'
)

note_2 = Note(
    id=uuid4(),
    title='Расписание',
    content='Сеголня занятие',
    created_at='2025-01-15'
)

note_3 = Note(
    id=uuid4(),
    title='Чего купить',
    content='Чупа-чупс',
    created_at='2025-01-14'
)

notes: dict[UUID, Note] = {
    uuid4(): note_1,
    uuid4(): note_2,
    uuid4(): note_3,
}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', notes=notes.values())


@app.route('/add_note')
def add_note():
    return render_template('add_note.html')


if __name__ == '__main__':
    app.run(debug=True)
