# Generated by Django 4.0.2 on 2022-07-13 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_contact_shippingaddress_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.orderitem'),
        ),
    ]
