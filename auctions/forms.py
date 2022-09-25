from django import forms
from django.db.models.base import Model
from django.db.models.fields import Field
from .models import AuctionListing, Bid, Category, Comment, Watchlist

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CreateListing(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ["title","starting_bid", "category", "header_image", "category", "description"]
        labels = {'title': "Title",'startPrice': "Start Price", 'Category': "Category", 'description': "Description"}

        widgets = {
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Description'}),
           
        }

class CreateComment(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ["commentbody"]
        labels= {'comment':"comment"}

        widgets = {
            'commentbody':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Comment'}),


        }

class CreateBid(forms.ModelForm):
    class Meta:
        model= Bid
        fields= ["bid_amount"]
        labels= {'bid_amount':"bid_amount"}

        widgets = {
            'bid_amount':forms.NumberInput(attrs={'class': 'form-control'}),

        }

class AddWatchlist(forms.ModelForm):
    class Meta:
        model= Watchlist
        fields= ["item_id"]






        