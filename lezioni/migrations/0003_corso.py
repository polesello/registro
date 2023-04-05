# Generated by Django 3.2.18 on 2023-04-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lezioni', '0002_auto_20230330_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=400)),
                ('codice', models.CharField(max_length=20)),
                ('data_inizio', models.DateField()),
                ('data_fine', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Corsi',
                'ordering': ['-data_inizio'],
            },
        ),
    ]
