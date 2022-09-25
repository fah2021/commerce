from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

from django.utils import timezone


class User(AbstractUser):
    pass

class Comment(models.Model):
    commentbody = models.TextField(max_length=80)
    commentedDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return f" {self.user} : {self.commentedDate}  "


class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f" {self.name}  "

class AuctionListing(models.Model):
    seller = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    header_image = models.ImageField(upload_to="images/", default = "images/placeholder_img.jpg" )
    description = models.TextField(max_length=200)
    starting_bid = models.FloatField(max_length=64)
    category = models.CharField(max_length=64, null=True, blank=True, )
    dateCreated = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name="comments")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.title}  "

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name="watchlist")
    item_id = models.ForeignKey(AuctionListing,on_delete=models.PROTECT,related_name="item_id",default = None)
    def __str__(self):
        return f" {self.user} : {self.item_id}  "

class Bid(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, )
    bid_amount = models.FloatField()
    BidDate = models.DateTimeField(auto_now_add=True)
    listing_id = models.ForeignKey(AuctionListing,on_delete=models.PROTECT,related_name="listing_id", null=True)
    winner = models.BooleanField(default=False)
    def __str__(self):
        return f" {self.user} : {self.listing_id}  "
