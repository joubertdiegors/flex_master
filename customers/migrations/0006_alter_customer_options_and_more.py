# Generated by Django 4.2.13 on 2024-07-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_customer_type_alter_customer_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='financial_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='general_email',
            new_name='other_email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='national_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]