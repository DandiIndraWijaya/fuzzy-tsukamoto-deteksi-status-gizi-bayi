# Generated by Django 3.2.5 on 2021-07-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gizibayi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bayi',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('x', 'laki-laki'), ('y', 'perempuan')], default='', max_length=60, verbose_name='gender'),
        ),
    ]
