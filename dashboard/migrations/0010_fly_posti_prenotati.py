# Generated by Django 3.0.1 on 2022-04-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_posto_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='posti_prenotati',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
