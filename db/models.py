from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)

    workouts = relationship("Workout", back_populates="user")

class WorkoutType(Base):
    __tablename__ = 'workout_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    workouts = relationship("Workout", back_populates="type")

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    duration = Column(Integer)
    calories = Column(Integer)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    type_id = Column(Integer, ForeignKey('workout_types.id'))

    user = relationship("User", back_populates="workouts")
    type = relationship("WorkoutType", back_populates="workouts")