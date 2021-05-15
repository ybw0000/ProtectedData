# Generated by Django 3.2.2 on 2021-05-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('password1', models.CharField(max_length=50, verbose_name='Password')),
                ('password2', models.CharField(max_length=50, verbose_name='Confirm your password')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]