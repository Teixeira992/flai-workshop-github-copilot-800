from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['hero_name', 'name', 'email', 'team', 'created_at']
    search_fields = ['name', 'email', 'hero_name', 'team']
    list_filter = ['team', 'created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']
    search_fields = ['user_email', 'activity_type']
    list_filter = ['activity_type', 'date', 'created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'hero_name', 'user_email', 'team', 'total_activities', 'total_calories', 'total_duration', 'updated_at']
    search_fields = ['user_email', 'hero_name', 'team']
    list_filter = ['team', 'updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration', 'calories_estimate', 'recommended_for', 'created_at']
    search_fields = ['name', 'description', 'difficulty', 'recommended_for']
    list_filter = ['difficulty', 'recommended_for', 'created_at']
