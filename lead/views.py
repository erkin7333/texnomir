from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer
from team.models import Team


class LeadViewSet(ModelViewSet):
    """..Yetakchilarni malumotini chiqarish uchun ModelViewSet"""

    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, createc_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

