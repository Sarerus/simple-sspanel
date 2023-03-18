# Generated by Django 4.1.7 on 2023-03-18 07:09

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=128, null=True, verbose_name='Remark')),
                ('status', models.IntegerField(default=0, verbose_name='Status')),
                ('enable', models.BooleanField(default=True, verbose_name='Enable')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('uuid', models.UUIDField(help_text='V2ray-core client uuid', unique=True, verbose_name='UUID')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='User Level')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='System Account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]