from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """Yetakchilar malumotini olish uchun serializer"""
    class Meta:
        model = Lead
        read_only_fields = ('created_by', 'created_at', 'modified_af'),
        fields = ('id', 'company', 'contact_person', 'email',
                  'phone', 'website', 'confidence', 'estimated_value',
                  'status', 'priority',)