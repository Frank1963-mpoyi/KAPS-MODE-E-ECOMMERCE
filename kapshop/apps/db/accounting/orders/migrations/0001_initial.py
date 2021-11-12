# Generated by Django 3.2.4 on 2021-11-11 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kapshop.core.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('payments', '0001_initial'),
        ('coupons', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('datetime_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='DATE UPDATED')),
                ('time_updated', models.TimeField(blank=True, null=True, verbose_name='TIME UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('publish', models.DateField(blank=True, null=True)),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('code_currency', models.CharField(choices=[('CDF', 'CDF'), ('EUR', 'EUR'), ('USD', 'USD'), ('GBP', 'GBP'), ('ZAR', 'ZAR')], default='CDF', max_length=3, verbose_name='CURRENCY')),
                ('exchange_rate', models.DecimalField(decimal_places=5, default=1, max_digits=9, verbose_name='EXCHANGE RATE')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='COMMENT')),
                ('cancel_note', models.CharField(blank=True, max_length=200, null=True, verbose_name='CANCEL NOTE')),
                ('ordered', models.BooleanField(default=False, verbose_name='ORDERED')),
                ('refund_request', models.BooleanField(default=False, verbose_name='REFUND REQUESTED')),
                ('datetime_ordered', models.DateTimeField(auto_now_add=True, null=True, verbose_name='DATE ORDERED')),
                ('datetime_delivered', models.DateTimeField(blank=True, null=True, verbose_name='DATE DELIVERED')),
                ('datetime_refund_req', models.DateTimeField(blank=True, null=True, verbose_name='DATE REQUESTED')),
                ('datetime_refund_res', models.DateTimeField(blank=True, null=True, verbose_name='DATE RESPONSE')),
                ('datetime_cancelled', models.DateTimeField(blank=True, null=True, verbose_name='DATE CANCELLED')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=kapshop.core.utils.order_randcode_gen, max_length=100, verbose_name='CODE')),
                ('transaction_id', models.CharField(blank=True, default=kapshop.core.utils.transaction_id_randcode_gen, max_length=120, verbose_name='TRANSACTION ID')),
                ('complete', models.BooleanField(default=False, verbose_name='COMPLETE')),
                ('being_delivered', models.CharField(blank=True, max_length=120, null=True)),
                ('received', models.CharField(blank=True, max_length=120, null=True)),
                ('refund_requested', models.CharField(blank=True, max_length=120, null=True)),
                ('refund_granted', models.CharField(blank=True, max_length=120, null=True)),
                ('order_type', models.CharField(choices=[('D', 'Delivery'), ('S', 'Shipment'), ('P', 'Pick up')], max_length=2, null=True, verbose_name='ORDER TYPE')),
                ('payment_type', models.CharField(choices=[(1, 'Mobile Money'), (2, 'Credit Card'), (3, 'Debit Card'), (4, 'Bank Transfer'), (5, 'Paypal'), (6, 'Skrill')], max_length=2, null=True, verbose_name='PAYMENT TYPE')),
                ('billing_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='addresses.address')),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='coupons.coupon')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='locations.location')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='payments.payment')),
                ('shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='addresses.address')),
            ],
            options={
                'verbose_name_plural': 'orders',
                'db_table': 'Order',
            },
        ),
    ]
