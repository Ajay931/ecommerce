# Generated by Django 2.2.7 on 2019-11-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
