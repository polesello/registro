# Generated by Django 3.2.18 on 2023-04-03 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lezioni', '0005_auto_20230403_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('corso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lezioni.corso')),
            ],
            options={
                'verbose_name_plural': 'Moduli',
            },
        ),
    ]
