# Generated by Django 4.1.2 on 2022-10-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_company_jobpostings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='Title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default='', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
