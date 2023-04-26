from sqlalchemy import Integer, String, Text, delete
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from config.database import get_session

Base = declarative_base()


class ChatHistory(Base):
    __tablename__ = 'ChatHistory'  # noqa

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question: Mapped[str] = mapped_column(String(300))
    answer: Mapped[str] = mapped_column(Text())
    role: Mapped[str] = mapped_column(String(255))

    @classmethod
    def create(cls, question: str, answer: str, role: str):
        with get_session() as session:
            chat = cls(question=question, answer=answer, role=role)
            session.add(chat)
            session.commit()
            return chat

    @classmethod
    def get_old_messages(cls, role: str, limit: int):
        with get_session() as session:
            query = select(cls).filter_by(role=role).order_by(cls.id.desc()).limit(limit)
            result = session.execute(query)
            # data = []
            # for row in result.scalars().all():
            #     data.append({'role': 'user', 'content': row.question})
            #     # data.append({'role': 'assistant', 'content': row.answer})
            # return data
            context = ''
            result = result.scalars().all()
            for row in result:
                context += f'User: {row.question}\n{row.role.capitalize()}: {row.answer} '
            if len(result) >= limit:
                last_id = result[-1].id
                session.execute(delete(cls).filter(cls.id < last_id, cls.role == role))
                session.commit()
            return context
