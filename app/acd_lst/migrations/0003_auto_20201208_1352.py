# Generated by Django 3.1.3 on 2020-12-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acd_lst', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoCadastroFicha',
            fields=[
                ('ano', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('orgao', models.CharField(max_length=10)),
                ('nomeorgao', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=10)),
                ('codigogrupocargo', models.CharField(max_length=5)),
                ('codigocargo', models.CharField(max_length=5)),
                ('classe', models.CharField(max_length=5)),
                ('padrao', models.CharField(max_length=5)),
                ('sigla', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InfoFinanceiraFicha',
            fields=[
                ('ano', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('orgao', models.CharField(max_length=10)),
                ('codigorubrica', models.CharField(max_length=10)),
                ('nomerubrica', models.CharField(max_length=50)),
                ('rendimento', models.CharField(max_length=5)),
                ('sequencia', models.CharField(max_length=5)),
                ('datapag', models.CharField(max_length=8)),
                ('valor', models.FloatField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]