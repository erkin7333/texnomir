from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(ModelViewSet):
    """..Yetakchilarni malumotini chiqarish uchun ModelViewSet.."""

    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        # team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(created_by=self.request.user)

    # def perform_update(self, serializer):
    #     obj = self.get_object()
    #     member_id = self.request.data['assigned_at']
    #     if member_id:
    #         user = User.objects.get(pk=member_id)
    #         serializer.save(assigned_at=user)
    #     else:
    #         serializer.save()



