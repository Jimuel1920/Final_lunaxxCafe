# Generated by Django 4.0.2 on 2022-03-03 13:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 3, 13, 19, 30, 381675, tzinfo=utc)),
        ),
    ]
