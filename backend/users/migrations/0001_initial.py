# Generated by Django 4.2.6 on 2023-10-12 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile/%Y/%m/')),
                ('introduce_me', models.TextField()),
                ('fullname', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('job', models.CharField(max_length=50)),
                ('religion', models.CharField(choices=[('PROTESTANTISM', 'Protestantism'), ('BUDDHISM', 'Buddhism'), ('CATHOLICISM', 'Catholicism'), ('OTHERS', 'Others'), ('NO_RELIGION', 'No Religion')], max_length=20)),
                ('my_character', models.TextField()),
                ('purpose_to_join', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
