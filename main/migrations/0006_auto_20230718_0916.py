# Generated by Django 3.2.8 on 2023-07-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_team_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
