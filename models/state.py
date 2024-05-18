#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablname__ = "states"
    name = Column(String(128), nullable=False)
