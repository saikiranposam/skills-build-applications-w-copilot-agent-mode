from rest_framework import viewsets
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def api_urls(self, request):
        codespace_url = "https://symmetrical-space-parakeet-65vw5rpwpwc5jj5-8000.app.github.dev"
        return Response({
            'users': f'{codespace_url}/api/users/',
            'teams': f'{codespace_url}/api/teams/',
            'activities': f'{codespace_url}/api/activities/',
            'workouts': f'{codespace_url}/api/workouts/',
            'leaderboard': f'{codespace_url}/api/leaderboard/',
        })

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
