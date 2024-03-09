#!/usr/bin/env bash
""" This module contains the 'Review' class """


from models import BaseModel


class review(BaseModel):
    """ This class inherits from the BaseModel class """
    place_id = ''
    user_id = ''
    text = ''