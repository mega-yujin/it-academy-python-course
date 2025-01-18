from flask import Flask, render_template, request, redirect, url_for, jsonify
from uuid import uuid4
from datetime import datetime
from database import NotesDatabase
from models import Note

app = Flask(__name__)
db = NotesDatabase()


@app.route('/')
def index():
    notes = db.get_all_notes()
    return render_template('index.html', notes=[note.to_dict() for note in notes])


@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = Note(
            id=uuid4(),
            title=request.form['title'],
            content=request.form['content'],
            created_at=datetime.now()
        )
        db.add_note(note)
        return redirect(url_for('index'))
    return render_template('add_note.html')


@app.route('/toggle_favorite/<uuid:note_id>')
def toggle_favorite(note_id):
    db.toggle_favorite(note_id)
    return redirect(url_for('index'))


@app.route('/favorites')
def favorites():
    favorite_notes = db.get_favorite_notes()
    return render_template('favorites.html', notes=[note.to_dict() for note in favorite_notes])


@app.route('/delete/<uuid:note_id>')
def delete_note(note_id):
    db.delete_note(note_id)
    return redirect(url_for('index'))


@app.route('/api/notes', methods=['GET'])
def api_get_notes():
    notes = db.get_all_notes()
    return jsonify([note.to_dict() for note in notes]), 200


@app.route('/api/notes', methods=['POST'])
def api_add_note():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Необходимы поля title и content'}), 400

    note = Note(
        id=uuid4(),
        title=data['title'],
        content=data['content'],
        created_at=datetime.now()
    )
    db.add_note(note)
    return jsonify(note.to_dict()), 201


@app.route('/api/notes/<uuid:note_id>', methods=['PATCH'])
def api_update_note(note_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Отсутствуют данные для обновления'}), 400

    if db.update_note(note_id, data):
        return jsonify({'message': 'Заметка обновлена'}), 200
    return jsonify({'error': 'Заметка не найдена'}), 404


@app.route('/api/notes/<uuid:note_id>', methods=['DELETE'])
def api_delete_note(note_id):
    if db.delete_note(note_id):
        return jsonify({'message': 'Заметка удалена'}), 200
    return jsonify({'error': 'Заметка не найдена'}), 404


if __name__ == '__main__':
    app.run(debug=True)
