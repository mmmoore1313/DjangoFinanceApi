# Generated by Django 3.0 on 2021-04-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
