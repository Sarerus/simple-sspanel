# Generated by Django 4.1.7 on 2023-03-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_proxynode_traffic_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxynode',
            name='token',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Token'),
        ),
    ]
