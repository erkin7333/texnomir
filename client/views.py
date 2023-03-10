from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from team.models import Team
from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer


class ClentViewSet(ModelViewSet):
    """..Clientlarni malumotini chiqarish uchun ModelViewSet.."""
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        """Jamoa azolarini filter qilish"""

        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)


class NoteViewSet(ModelViewSet):
    """Eslatmalarni ko'rish uchum ModelViewSet.."""

    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        """Jamoa azolarini filter qilish"""

        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')
        return self.queryset.filter(team=team, client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']
        serializer.save(team=team, created_by=self.request.user, client_id=client_id)
