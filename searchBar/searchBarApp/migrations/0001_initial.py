# Generated by Django 2.1.2 on 2018-11-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=264, unique=True)),
                ('category', models.CharField(default='', max_length=264)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(default='', max_length=528)),
                ('date', models.DateField(blank=True, default='', null=True)),
                ('About', models.TextField(default='')),
            ],
        ),
    ]
