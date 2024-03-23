from os import getenv
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

username = getenv("DB_USERNAME")
password = getenv("DB_PASSWORD")
database = getenv("DB_DATABASE")
host = getenv("DB_HOST")
port = getenv("DB_PORT")

Base = declarative_base()

url = URL.create(
    drivername="postgresql",
    username=username,
    password=password,
    database=database,
    port=port,
    host=host,
)
print(f"connect url: {url}")

engine = SQLAlchemy(model_class=Base)
session = engine.session


def create_all():
    engine.create_all()


@dataclass
class Task(engine.Model):
    __tablename__ = "tasks"
    id: str
    name: str
    completed: bool

    id = Column(String(), primary_key=True)
    name = Column(String(), nullable=False)
    completed = Column(Boolean(), default=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now)
