from django.db import models
from django.contrib.auth.models import Game, Gamers

class Event(models.Model):

        event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
        game = models.OnetoManyField(Game, on_delete=models.CASCADE)
        location = models.CharField()