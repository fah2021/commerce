# Generated by Django 3.2.7 on 2021-11-14 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20211114_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Comment'),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='item', to='auctions.auctionlisting'),
        ),
    ]
