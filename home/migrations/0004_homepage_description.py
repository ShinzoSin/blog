# Generated by Django 3.2.12 on 2022-02-01 23:03

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_call_to_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
