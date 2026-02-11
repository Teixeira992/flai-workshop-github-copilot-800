from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Mightiest Heroes of Earth protecting the universe'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League defending truth and justice'
        )

        self.stdout.write('Creating users...')
        users_data = [
            # Marvel Heroes
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'hero_name': 'Iron Man', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'cap@marvel.com', 'hero_name': 'Captain America', 'team': 'Team Marvel'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'hero_name': 'Black Widow', 'team': 'Team Marvel'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'hero_name': 'Hulk', 'team': 'Team Marvel'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'hero_name': 'Thor', 'team': 'Team Marvel'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'hero_name': 'Spider-Man', 'team': 'Team Marvel'},
            {'name': 'Wanda Maximoff', 'email': 'scarletwitch@marvel.com', 'hero_name': 'Scarlet Witch', 'team': 'Team Marvel'},
            {'name': 'Carol Danvers', 'email': 'captainmarvel@marvel.com', 'hero_name': 'Captain Marvel', 'team': 'Team Marvel'},
            # DC Heroes
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'hero_name': 'Superman', 'team': 'Team DC'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'hero_name': 'Batman', 'team': 'Team DC'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'hero_name': 'Wonder Woman', 'team': 'Team DC'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'hero_name': 'The Flash', 'team': 'Team DC'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'hero_name': 'Aquaman', 'team': 'Team DC'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'hero_name': 'Green Lantern', 'team': 'Team DC'},
            {'name': 'Victor Stone', 'email': 'cyborg@dc.com', 'hero_name': 'Cyborg', 'team': 'Team DC'},
            {'name': 'Oliver Queen', 'email': 'greenarrow@dc.com', 'hero_name': 'Green Arrow', 'team': 'Team DC'},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(**user_data)
            users.append(user)

        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Boxing', 'Yoga', 'Martial Arts', 'Climbing']
        
        for user in users:
            # Each hero gets 5-10 random activities over the past 30 days
            num_activities = random.randint(5, 10)
            for _ in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(30, 120)  # 30-120 minutes
                distance = round(random.uniform(3, 20), 2) if activity_type in ['Running', 'Swimming', 'Cycling'] else None
                calories = random.randint(200, 800)
                activity_date = date.today() - timedelta(days=random.randint(0, 30))
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=activity_date
                )

        self.stdout.write('Creating leaderboard entries...')
        for user in users:
            user_activities = Activity.objects.filter(user_email=user.email)
            total_activities = user_activities.count()
            total_calories = sum(a.calories for a in user_activities)
            total_duration = sum(a.duration for a in user_activities)
            
            Leaderboard.objects.create(
                user_email=user.email,
                hero_name=user.hero_name,
                team=user.team,
                total_activities=total_activities,
                total_calories=total_calories,
                total_duration=total_duration,
                rank=0  # Will be calculated based on total_calories
            )

        # Update ranks based on total_calories
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()

        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity full-body workout inspired by Captain America',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 600,
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Web-Slinger Cardio',
                'description': 'Agility and cardio workout for spider-like reflexes',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 450,
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Asgardian Strength',
                'description': 'Power lifting and strength training fit for a god',
                'difficulty': 'Hard',
                'duration': 75,
                'calories_estimate': 700,
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Arc Reactor Circuits',
                'description': 'High-tech circuit training with tech-enhanced movements',
                'difficulty': 'Medium',
                'duration': 50,
                'calories_estimate': 500,
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Kryptonian Power Hour',
                'description': 'Superhuman strength and endurance training',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 650,
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Speed Force Sprints',
                'description': 'Lightning-fast interval training for maximum speed',
                'difficulty': 'Hard',
                'duration': 40,
                'calories_estimate': 550,
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Bat-Cave Boot Camp',
                'description': 'Elite tactical training combining strength and strategy',
                'difficulty': 'Hard',
                'duration': 70,
                'calories_estimate': 680,
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Ancient warrior training for strength and grace',
                'difficulty': 'Medium',
                'duration': 55,
                'calories_estimate': 520,
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Atlantean Aquatics',
                'description': 'Swimming and water-based resistance training',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 400,
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Hero Recovery Yoga',
                'description': 'Restorative yoga for post-battle recovery',
                'difficulty': 'Easy',
                'duration': 30,
                'calories_estimate': 150,
                'recommended_for': 'All Teams'
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workout suggestions')
