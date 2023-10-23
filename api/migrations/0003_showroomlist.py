# Generated by Django 4.2.6 on 2023-10-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_carlist_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowroomList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=50)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
    ]