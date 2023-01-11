from rest_framework.viewsets import ModelViewSet
from .models import Team
from .serializers import UserSerialezer, TeamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):

        return self.queryset.filter(members__in=[self.request.user]).first()

    print("AAAAAAAAAAa", queryset)

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()


@api_view(['GET'])
def get_my_team(request):
    """Jamoa azolarini filter qilish """
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(['POST'])
def add_member(request):
    """Jamoaga a'zolar qo'shish"""

    team = Team.objects.filter(members__in=[request.user]).first()
    email = request.data['email']
    print('Email===========', email)
    user = User.objects.get(username=email)
    team.members.add(user)
    team.save()
    return Response()