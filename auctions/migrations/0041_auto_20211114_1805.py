# Generated by Django 3.2.7 on 2021-11-14 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_auto_20211114_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Comment'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='item', to='auctions.auctionlisting'),
        ),
    ]
