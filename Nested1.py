animals = [
    {
        "animal" : {
            "type" : "bunny"
        }
    },

    {
        "animal" : {}
    },

    {}
]

g = lambda x: x.get

# WE need something that uses short words and can allow it to be used as .get
# Maybe we can create an object.


print(animals[0].get("animal").get("type"))
print(animals[1])
print(animals[2])

d = dict()


class my_module():
    def __init__(self, function, dictionary):
        self.d = dictionary
        self.f = function
    
    def do_this(self, key1):
        return self.f(self.d, key1)


class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None

        for key in keys:
            pass

# my_dict = my_module(lambda x,y: x.get(x,y), {"a":"A", "b":"B"})

# print(my_dict.do_this("a"))

# Continue here please.
# And finish all the videos as well please.
# Learning your own servers from scratch.
# The with function



# Tables.
# Step one: Check type of the object itself.


"""
from requests import get
from contextlib import closing
from datetime import datetime
import csv
import os
import locale
from datetime import date, timedelta
import os.path
import pandas as pd
import pysftp
import codecs
import sys


"""