from django.db import models


class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    number_of_players = models.IntegerField()
    maker = models.CharField(max_length=30)
    skill_level = models.IntegerField()