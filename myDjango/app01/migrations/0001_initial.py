# Generated by Django 3.1.6 on 2021-02-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
    ]
