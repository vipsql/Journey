# Generated by Django 2.0.4 on 2019-05-31 08:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20190530_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('98a466b4-8f70-4fe4-91b1-cc1bb1cd6f00'), verbose_name='用户jwt加密秘钥'),
        ),
    ]