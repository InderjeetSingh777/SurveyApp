# Generated by Django 2.1.7 on 2019-03-02 19:59

import AccountDetails.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('people_contacted', models.IntegerField(default=0)),
                ('reviews_collected', models.IntegerField(default=0)),
                ('education_rating', models.IntegerField(validators=[AccountDetails.models.validate_rating])),
                ('health_rating', models.IntegerField(validators=[AccountDetails.models.validate_rating])),
                ('electricity_rating', models.IntegerField(validators=[AccountDetails.models.validate_rating])),
                ('transport_rating', models.IntegerField(validators=[AccountDetails.models.validate_rating])),
                ('employment_rating', models.IntegerField(validators=[AccountDetails.models.validate_rating])),
            ],
        ),
    ]
