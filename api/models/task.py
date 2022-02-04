from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base

"""
Base = declarative_base()
FYI:
https://www.python.ambitious-engineer.com/archives/1487

relationship = RelationshipProperty
class RelationshipProperty(StrategizedProperty, Generic[_T_co]):
"""


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    done = relationship("Done", back_populates="task")


"""
About relationship
FYI:
https://www.python.ambitious-engineer.com/archives/1579
"""


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")
