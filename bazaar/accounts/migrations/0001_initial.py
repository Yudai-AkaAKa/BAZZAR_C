# Generated by Django 4.1.3 on 2022-12-01 02:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('userid', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True, verbose_name='userid')),
                ('username', models.CharField(max_length=20, verbose_name='name')),
                ('usertype', models.BooleanField(default=True, verbose_name='usertype')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('mail', models.EmailField(max_length=40, verbose_name='mail')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='tel')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0)], verbose_name='age')),
                ('adress', models.CharField(blank=True, max_length=80, null=True, verbose_name='adress')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='lastlogin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'CustomUser',
            },
        ),
    ]
