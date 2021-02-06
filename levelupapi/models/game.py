from django.db import models


class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    numbers_of_players = models.IntegerField()