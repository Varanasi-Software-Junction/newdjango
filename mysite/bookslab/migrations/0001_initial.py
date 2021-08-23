# Generated by Django 3.1.1 on 2021-08-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('subject', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
