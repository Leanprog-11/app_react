import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/hack_react'
    SQLALCHEMY_TRACK_MODIFICATIONS= False