# Generated by Django 4.2.6 on 2023-12-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DegreeAudit', '0009_alter_grade_letter_alter_section_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassStatus',
            fields=[
                ('status', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'da_pass_status',
            },
        ),
    ]
