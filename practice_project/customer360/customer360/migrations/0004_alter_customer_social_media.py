# Generated by Django 5.2.4 on 2025-07-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0003_alter_customer_social_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='social_media',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
