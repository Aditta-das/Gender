# Generated by Django 2.2.7 on 2020-04-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200403_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
