# Generated by Django 3.1.7 on 2021-04-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('login', models.TextField(unique=True)),
                ('token', models.TextField()),
                ('avatar_url', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
