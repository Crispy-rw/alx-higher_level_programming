#!/usr/bin/python3
"""
Safe from MySQL injections
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
