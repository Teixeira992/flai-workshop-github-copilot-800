from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.hero_name} ({self.name})"


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in kilometers
    calories = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.user_email} - {self.activity_type} ({self.date})"


class Leaderboard(models.Model):
    user_email = models.EmailField()
    hero_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']

    def __str__(self):
        return f"{self.hero_name} - Rank {self.rank}"


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    recommended_for = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.name} ({self.difficulty})"
