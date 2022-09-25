# Generated by Django 3.2.7 on 2021-10-10 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_user_bids_buyer_bidder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bids',
            new_name='bid',
        ),
        migrations.RenameModel(
            old_name='auctionListings',
            new_name='auctionListing',
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=80)),
                ('commentedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
