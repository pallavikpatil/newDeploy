# Generated by Django 2.2.3 on 2019-07-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'faculty_info',
            },
        ),
    ]