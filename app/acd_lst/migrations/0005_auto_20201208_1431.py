# Generated by Django 3.1.3 on 2020-12-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acd_lst', '0004_auto_20201208_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofinanceiraficha',
            name='valor',
            field=models.CharField(max_length=20),
        ),
    ]