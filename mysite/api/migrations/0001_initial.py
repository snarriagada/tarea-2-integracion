# Generated by Django 3.1.7 on 2021-05-02 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('albums', models.URLField()),
                ('tracks', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('genre', models.CharField(default='', max_length=200)),
                ('artist', models.URLField()),
                ('tracks', models.URLField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artist')),
            ],
        ),
    ]
