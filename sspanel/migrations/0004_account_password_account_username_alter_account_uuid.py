# Generated by Django 4.1.7 on 2023-03-18 08:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sspanel', '0003_rename_account_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=128, null=True, verbose_name='temp password'),
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=128, null=True, verbose_name='temp username'),
        ),
        migrations.AlterField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='V2ray-core client uuid', unique=True, verbose_name='UUID'),
        ),
    ]
