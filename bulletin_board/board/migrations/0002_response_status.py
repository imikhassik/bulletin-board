# Generated by Django 4.2.1 on 2023-05-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='status',
            field=models.CharField(choices=[('A', 'Accepted'), ('D', 'Denied')], max_length=1, null=True),
        ),
    ]
