from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="John Doe",
            email="john@example.com",
            hero_name="The Flash",
            team="Speedsters"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.hero_name, "The Flash")
        self.assertEqual(self.user.team, "Speedsters")

    def test_user_str(self):
        self.assertEqual(str(self.user), "The Flash (John Doe)")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Speedsters",
            description="Fast and furious team"
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Speedsters")
        self.assertEqual(self.team.description, "Fast and furious team")

    def test_team_str(self):
        self.assertEqual(str(self.team), "Speedsters")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="john@example.com",
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            date=date.today()
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user_email, "john@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)
        self.assertEqual(self.activity.calories, 300)


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_email="john@example.com",
            hero_name="The Flash",
            team="Speedsters",
            total_activities=10,
            total_calories=3000,
            total_duration=300,
            rank=1
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user_email, "john@example.com")
        self.assertEqual(self.leaderboard.hero_name, "The Flash")
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name="HIIT Training",
            description="High intensity interval training",
            difficulty="Hard",
            duration=45,
            calories_estimate=500,
            recommended_for="Advanced"
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "HIIT Training")
        self.assertEqual(self.workout.difficulty, "Hard")
        self.assertEqual(self.workout.duration, 45)


class UserAPITest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'hero_name': 'Wonder Woman',
            'team': 'Justice League'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Jane Doe')


class TeamAPITest(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {
            'name': 'Justice League',
            'description': 'Heroes united'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Justice League')


class ActivityAPITest(APITestCase):
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'user_email': 'john@example.com',
            'activity_type': 'Cycling',
            'duration': 60,
            'distance': 15.0,
            'calories': 500,
            'date': str(date.today())
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)


class LeaderboardAPITest(APITestCase):
    def test_create_leaderboard_entry(self):
        url = reverse('leaderboard-list')
        data = {
            'user_email': 'john@example.com',
            'hero_name': 'The Flash',
            'team': 'Speedsters',
            'total_activities': 5,
            'total_calories': 1500,
            'total_duration': 150,
            'rank': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 1)


class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {
            'name': 'Morning Yoga',
            'description': 'Gentle yoga for beginners',
            'difficulty': 'Easy',
            'duration': 30,
            'calories_estimate': 150,
            'recommended_for': 'Beginners'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
