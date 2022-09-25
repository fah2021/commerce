# Generated by Django 3.2.7 on 2021-11-04 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20211104_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='buyer_bidder',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='date',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidding', to='auctions.bid'),
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