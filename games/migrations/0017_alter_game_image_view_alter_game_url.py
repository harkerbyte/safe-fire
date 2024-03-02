# Generated by Django 5.0.1 on 2024-02-19 11:18

import games.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_alter_game_js_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='Image_View',
            field=models.ImageField(default='media_file/default/game.png', upload_to='media_files/', validators=[games.models.validate_image_view]),
        ),
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.CharField(max_length=90),
        ),
    ]