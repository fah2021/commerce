# Generated by Django 3.2.7 on 2021-10-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_watchlist_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.AuctionListing'),
        ),
    ]
