from django.db import models
from django.contrib.auth.models import User


"""Yetakchilar uchum model"""
class Lead(models.Model):
    NEW = 'Yangi'
    CONTACTED = 'ALOQA QILGAN'
    INPROGRESS = 'JARAYONDA'
    LOST = "YO'QOTILGAN"
    WON = 'YUTUQ'
    CHOICES_STATUS = (
        (NEW, 'Yangi'),
        (CONTACTED, 'ALOQA QILGAN'),
        (INPROGRESS, 'JARAYONDA'),
        (LOST, "YO'QOTILGAN"),
        (WON, 'YUTUQ')
    )

    LOW = "PAST"
    MEDIUM = 'OʻRTA'
    HIGH = 'YUQORI'
    CHOICES_PRIORITY = (
        (LOW, "PAST"),
        (MEDIUM, 'OʻRTA'),
        (HIGH, 'YUQORI')
    )

    company = models.CharField(max_length=255, verbose_name='Kompaniya')
    contact_person = models.CharField(max_length=255, verbose_name="Shaxs bn bog'lanish")
    email = models.EmailField(verbose_name="Elektron manzil")
    phone = models.CharField(max_length=20, verbose_name="Telefon nomer")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vebsayit")
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True, verbose_name='Taxminiy qiymat')
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=50, choices=CHOICES_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Lead"
