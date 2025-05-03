from djongo import models

# User model
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.email

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list, blank=True)
    def __str__(self):
        return self.name

# Activity model
class Activity(models.Model):
    activity_id = models.IntegerField(unique=True)
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    distance = models.FloatField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.type}"

# Workout model
class Workout(models.Model):
    workout_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

# Leaderboard model
class Leaderboard(models.Model):
    leaderboard_id = models.IntegerField(unique=True)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.points}"
