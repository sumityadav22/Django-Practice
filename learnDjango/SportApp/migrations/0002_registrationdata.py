# Generated by Django 3.0.3 on 2020-03-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
