# Generated by Django 2.2.3 on 2019-08-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0008_auto_20190816_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]