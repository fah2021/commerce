# Generated by Django 3.2.7 on 2021-10-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_watchlist_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='expiryDate',
        ),
        migrations.RemoveField(
            model_name='auctionlisting',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='item', to='auctions.AuctionListing'),
        ),
    ]
