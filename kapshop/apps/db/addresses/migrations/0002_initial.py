# Generated by Django 3.2.4 on 2021-11-11 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='ORDER'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='locations.location'),
        ),
    ]
