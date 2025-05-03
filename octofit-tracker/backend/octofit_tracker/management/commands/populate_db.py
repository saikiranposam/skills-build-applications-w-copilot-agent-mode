from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activity, leaderboard, and workouts collections.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data (example, adapt as needed)
        users = [
            {"email": "alice@example.com", "name": "Alice", "age": 16, "team": "Red"},
            {"email": "bob@example.com", "name": "Bob", "age": 17, "team": "Blue"},
            {"email": "carol@example.com", "name": "Carol", "age": 16, "team": "Red"},
        ]
        teams = [
            {"name": "Red", "members": ["alice@example.com", "carol@example.com"]},
            {"name": "Blue", "members": ["bob@example.com"]},
        ]
        activities = [
            {"activity_id": 1, "user": "alice@example.com", "type": "run", "distance": 2.5, "points": 25},
            {"activity_id": 2, "user": "bob@example.com", "type": "walk", "distance": 1.0, "points": 10},
            {"activity_id": 3, "user": "carol@example.com", "type": "strength", "reps": 30, "points": 30},
        ]
        leaderboard = [
            {"leaderboard_id": 1, "team": "Red", "points": 55},
            {"leaderboard_id": 2, "team": "Blue", "points": 10},
        ]
        workouts = [
            {"workout_id": 1, "name": "Morning Run", "description": "2.5km run around the track."},
            {"workout_id": 2, "name": "Pushups", "description": "30 pushups."},
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data.'))
