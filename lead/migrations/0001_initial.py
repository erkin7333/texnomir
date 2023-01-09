# Generated by Django 4.1.5 on 2023-01-09 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, verbose_name='Kompaniya')),
                ('contact_person', models.CharField(max_length=255, verbose_name="Shaxs bn bog'lanish")),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron manzil')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon nomer')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Vebsayit')),
                ('confidence', models.IntegerField(blank=True, null=True)),
                ('estimated_value', models.IntegerField(blank=True, null=True, verbose_name='Taxminiy qiymat')),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('ALOQA QILGAN', 'ALOQA QILGAN'), ('JARAYONDA', 'JARAYONDA'), ("YO'QOTILGAN", "YO'QOTILGAN"), ('YUTUQ', 'YUTUQ')], default='Yangi', max_length=50)),
                ('priority', models.CharField(choices=[('PAST', 'PAST'), ('OʻRTA', 'OʻRTA'), ('YUQORI', 'YUQORI')], default='OʻRTA', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_ad', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lead',
            },
        ),
    ]
