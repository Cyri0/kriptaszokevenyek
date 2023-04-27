from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField(default=14)
    attack = models.IntegerField(default=8)
    defense = models.IntegerField(default=8)
    luck = models.IntegerField(default=7)
    magic = models.IntegerField(default=10)

    class Meta:
        abstract: True

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlayerCharacter(Character):
    backpack = models.ManyToManyField(Item)

class EnemyCharacter(Character):
    description = models.TextField()
