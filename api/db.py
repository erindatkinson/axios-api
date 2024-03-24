"""The db module houses the main configuration for the database objects and models."""

from os import getenv
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = SQLAlchemy(model_class=Base)
session = engine.session


def get_db_configs() -> Any:
    """get_db_configs pulls the db configs from the environment and returns
    a SQLAlchemy URL object"""
    username = getenv("DB_USERNAME")
    password = getenv("DB_PASSWORD")
    database = getenv("DB_DATABASE")
    host = getenv("DB_HOST")
    port = getenv("DB_PORT")

    return URL.create(
        drivername="postgresql",
        username=username,
        password=password,
        database=database,
        port=port,
        host=host,
    )


def create_all():
    """create_all is a shim to the flask-sqlalchemy db object's create_all method without having to
    call the full object path"""
    engine.create_all()


@dataclass
class Task(engine.Model):
    """Task is the model class for todolist items"""

    __tablename__ = "tasks"
    id: str
    name: str
    completed: bool

    id = Column(String(), primary_key=True)
    name = Column(String(), nullable=False)
    completed = Column(Boolean(), default=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now)
