from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class Note:
    id: UUID
    title: str
    content: str
    created_at: datetime = datetime.now()
    is_favorite: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> 'Note':
        return cls(
            id=UUID(data['id']),
            title=data['title'],
            content=data['content'],
            created_at=datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S"),
            is_favorite=bool(data['is_favorite'])
        )

    def to_dict(self) -> dict:
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'is_favorite': self.is_favorite
        }
