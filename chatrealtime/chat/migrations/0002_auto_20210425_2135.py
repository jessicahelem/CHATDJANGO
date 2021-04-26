# Generated by Django 3.2 on 2021-04-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='msg',
        ),
        migrations.AddField(
            model_name='message',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
    ]
