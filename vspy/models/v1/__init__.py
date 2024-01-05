from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from vspy.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, index=True)
    subject = Column(String, index=True)
    complete = Column(Boolean, default=False)
    created = Column(Integer, default=lambda: datetime.utcnow().timestamp())
    modified = Column(Integer)
