# Generated by Django 5.0.1 on 2024-01-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_options_game_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='supports',
            field=models.CharField(choices=[('Android And Pc', 'Mobile And Pc'), ('Pc only', 'Pc Only'), ('Mobile only', 'Mobile Only')], default='Android And Pc', max_length=14),
        ),
    ]