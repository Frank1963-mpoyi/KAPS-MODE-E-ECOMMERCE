# Generated by Django 3.2.4 on 2021-11-11 16:03

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import kapshop.core.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KapsAdmin',
            fields=[
                ('street_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street Name')),
                ('house_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number')),
                ('post_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Postal Code')),
                ('area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Area')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='DATE UPDATED')),
                ('time_updated', models.TimeField(blank=True, null=True, verbose_name='TIME UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('publish', models.DateField(blank=True, null=True)),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('email1', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Admin. Email')),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Account Email')),
                ('email3', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Branch Email')),
                ('email4', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Legal Email')),
                ('phone1', models.CharField(max_length=30, unique=True, verbose_name='Phone 1')),
                ('phone2', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Phone 2')),
                ('phone3', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Phone 3')),
                ('phone4', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Phone 4')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=kapshop.core.utils.randcode_gen, max_length=100, verbose_name='CODE')),
                ('bool_active', models.BooleanField(blank=True, default=False, null=True, verbose_name='IS ACTIVE')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='admins', to='locations.location')),
            ],
            options={
                'verbose_name_plural': 'kps_admins',
                'db_table': 'kps_admins',
            },
        ),
    ]
