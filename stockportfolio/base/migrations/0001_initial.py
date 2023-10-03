# Generated by Django 4.2.5 on 2023-09-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_symbol', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
    ]