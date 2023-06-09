# Generated by Django 3.2.18 on 2023-04-03 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lezioni', '0008_auto_20230403_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presenza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.BooleanField()),
                ('lezione', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lezioni.lezione')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lezioni.persona')),
            ],
            options={
                'verbose_name_plural': 'Presenze',
                'ordering': ['persona', 'lezione'],
            },
        ),
    ]
