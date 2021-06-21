#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):

    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False, unique=True)
    cities = relationship('City', back_populates='cities')

    @property
    def cities(self):
        from models import storage
        c = storage.all(City).values()
        return [val for val in c if val.state_id == self.id]
