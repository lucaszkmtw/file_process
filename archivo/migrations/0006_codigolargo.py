# Generated by Django 3.2.7 on 2021-11-09 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('archivo', '0005_auto_20211109_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoLargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=550, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
