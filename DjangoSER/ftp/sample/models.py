from django.db import models
import os
# Create your models here.
class PathItem:
    name = ""
    parent = ""
    url = ""
 
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.url = "http://10.236.144.60:7777/folder/" + os.path.join(parent, name)
 
 
class FileItem:
    name = ""
    parent = ""
    url = ""
    canRead = True
 
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.url = "http://10.236.144.60:7777/file/" + os.path.join(parent, name)
