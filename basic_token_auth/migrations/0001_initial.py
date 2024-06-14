# Generated by Django 3.2 on 2024-06-14 11:16

import basic_token_auth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('expiry', models.DateTimeField(blank=True, default=basic_token_auth.models.get_token_expiry, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('key', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('auth_token', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='refresh_token', to='basic_token_auth.token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refresh_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
