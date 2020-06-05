# Generated by Django 3.0.6 on 2020-06-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoatelier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('price', models.CharField(max_length=255, null=True)),
            ],
        ),

    ]
