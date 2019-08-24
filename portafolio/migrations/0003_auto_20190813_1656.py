# Generated by Django 2.2.3 on 2019-08-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_auto_20190807_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.TextField(blank=True, db_column='Player', null=True)),
                ('position', models.TextField(blank=True, db_column='Position', null=True)),
                ('games', models.IntegerField(blank=True, db_column='Games', null=True)),
                ('win_rate', models.TextField(blank=True, db_column='Win_Rate', null=True)),
                ('kda', models.TextField(blank=True, db_column='KDA', null=True)),
                ('avg_kills', models.TextField(blank=True, db_column='AVG_Kills', null=True)),
                ('avg_deaths', models.TextField(blank=True, db_column='AVG_Deaths', null=True)),
                ('avg_assists', models.TextField(blank=True, db_column='AVG_Assists', null=True)),
                ('csm', models.TextField(blank=True, db_column='CSM', null=True)),
                ('gpm', models.IntegerField(blank=True, db_column='GPM', null=True)),
                ('dmg', models.TextField(blank=True, db_column='DMG', null=True)),
                ('avg_dpm', models.IntegerField(blank=True, db_column='AVG_DPM', null=True)),
                ('vspm', models.TextField(blank=True, db_column='VSPM', null=True)),
                ('avg_wpm', models.TextField(blank=True, db_column='AVG_WPM', null=True)),
                ('avg_wcpm', models.TextField(blank=True, db_column='AVG_WCPM', null=True)),
                ('avg_vwpm', models.TextField(blank=True, db_column='AVG_VWPM', null=True)),
                ('gd15', models.IntegerField(blank=True, db_column='GD15', null=True)),
                ('csd15', models.IntegerField(blank=True, db_column='CSD15', null=True)),
                ('xpd15', models.IntegerField(blank=True, db_column='XPD15', null=True)),
                ('fb', models.TextField(blank=True, db_column='FB', null=True)),
                ('fb_victim', models.TextField(blank=True, db_column='FB_Victim', null=True)),
                ('penta_kills', models.IntegerField(blank=True, db_column='Penta_Kills', null=True)),
                ('solo_kills', models.IntegerField(blank=True, db_column='Solo_Kills', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]