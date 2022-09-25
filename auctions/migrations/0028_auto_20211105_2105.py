# Generated by Django 3.2.7 on 2021-11-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20211105_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Comment'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.FloatField(max_length=64),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='item', to='auctions.AuctionListing'),
        ),
    ]
