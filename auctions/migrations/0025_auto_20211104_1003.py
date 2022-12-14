# Generated by Django 3.2.7 on 2021-11-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20211103_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.AddField(
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
