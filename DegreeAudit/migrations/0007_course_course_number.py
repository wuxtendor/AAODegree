# Generated by Django 4.2.6 on 2023-12-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DegreeAudit', '0006_course_subject_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(default=1),
        ),
    ]