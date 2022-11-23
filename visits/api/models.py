from django.db import models

# Create your models here.

class Api:
    def __init__(self, req, res):
        self.req = req
        self.res = res