# Generated by Django 3.2.5 on 2021-09-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210917_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
