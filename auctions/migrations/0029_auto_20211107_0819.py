# Generated by Django 3.2.7 on 2021-11-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_auto_20211105_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='user',
            new_name='seller',
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Comment'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='item', to='auctions.AuctionListing'),
        ),
    ]
