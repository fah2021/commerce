# Generated by Django 3.2.7 on 2021-10-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_watchlist_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, to='auctions.AuctionListing'),
        ),
    ]