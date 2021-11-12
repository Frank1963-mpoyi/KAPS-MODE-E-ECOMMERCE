# Generated by Django 3.2.4 on 2021-11-11 16:03

from django.db import migrations, models
import django.db.models.deletion
import kapshop.core.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('datetime_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='DATE CREATED')),
                ('datetime_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='DATE UPDATED')),
                ('time_updated', models.TimeField(blank=True, null=True, verbose_name='TIME UPDATED')),
                ('last_updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='LAST UPDATED BY')),
                ('publish', models.DateField(blank=True, null=True)),
                ('bool_deleted', models.BooleanField(default=False, verbose_name='IS DELETED?')),
                ('bool_new', models.BooleanField(default=True, verbose_name='IS NEW')),
                ('bool_baby', models.BooleanField(blank=True, null=True, verbose_name='FOR BABY')),
                ('bool_child', models.BooleanField(blank=True, null=True, verbose_name='FOR CHILD')),
                ('bool_adult', models.BooleanField(blank=True, null=True, verbose_name='FOR ADULT')),
                ('bool_teen', models.BooleanField(blank=True, null=True, verbose_name='FOR TEEN')),
                ('bool_female', models.BooleanField(blank=True, null=True, verbose_name='IS FEMALE PRODUCT')),
                ('bool_male', models.BooleanField(blank=True, null=True, verbose_name='IS MALE PRODUCT')),
                ('uuid_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='TOKEN')),
                ('code', models.CharField(default=kapshop.core.utils.categ_randcode_gen, max_length=100, verbose_name='CODE')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, null=True, verbose_name='DESCRIPTION')),
                ('sub', models.BooleanField(default=False, verbose_name='SUB-CATEGORY')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='categories.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
    ]
