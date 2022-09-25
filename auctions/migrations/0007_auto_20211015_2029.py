# Generated by Django 3.2.7 on 2021-10-15 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auctionlisting_starting_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='expiryDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image_url',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]