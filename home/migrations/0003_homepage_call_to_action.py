# Generated by Django 3.2.12 on 2022-02-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='call_to_action',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
