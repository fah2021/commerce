# Generated by Django 3.2.7 on 2021-10-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20211010_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.CharField(default='start', max_length=64),
        ),
    ]
