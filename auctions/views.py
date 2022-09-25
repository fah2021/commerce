from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateListing,CreateComment,CreateBid,AddWatchlist
from .models import AuctionListing, Watchlist, Comment,Bid,Category
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "auctions/index.html", {
        "ActiveListings": AuctionListing.objects.all()
    })

@login_required(login_url='/login')
def create_listing(request):

    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            Addlisting = form.save(commit=False)
            Addlisting.seller_id = user.id
            if Addlisting.header_image == "":
                Addlisting.header_image = "images/placeholder_img.jpg"
            Addlisting.save()

            messages.success(request, 'Form has been submitted successfully.')
            return redirect('/create_listing')

        return render(request, "auctions/create_listing.html", {
            'form': form
    })
    else:
        return render(request, "auctions/create_listing.html", {
            "form": CreateListing(),
        })

def auctionListing(request, auctionListing_id):
    
    auctionListing = AuctionListing.objects.get(pk=auctionListing_id)
    #get listing owner info
    listing_owner = AuctionListing.objects.get(pk=auctionListing.id)
    watchlist = Watchlist.objects.filter(user=request.user.id,item_id_id=auctionListing_id)

    if not auctionListing.status:  
        latest_bids = Bid.objects.filter(listing_id=auctionListing_id).latest('bid_amount')
        return render(request, "auctions/auctionListing.html", {
        "auctionListing": auctionListing,
        "listing_owner":listing_owner,
        "watchlist":watchlist,
        'latest_bids': latest_bids
    })


    return render(request, "auctions/auctionListing.html", {
        "auctionListing": auctionListing,
        "listing_owner":listing_owner,
        "watchlist":watchlist,
       
    })

def watchlist(request):
    user = User.objects.get(id=request.user.id)
    watch_list=Watchlist.objects.filter(user=user)
    return render(request, "auctions/watchlist.html", {
        "watch_list": watch_list,
       

    })

@login_required(login_url='/login')
def Addwatchlist(request, auctionListing_id):
    watch_list_item = AuctionListing.objects.get(pk=auctionListing_id)
    user = User.objects.get(id=request.user.id)
    my_watchlist=Watchlist.objects.create(user=user,item_id=watch_list_item)
    return watchlist(request)

def Removewatchlist(request, auctionListing_id):
    watch_list_item = Watchlist.objects.get(user=request.user.id,item_id=auctionListing_id)
    remove = Watchlist.objects.get(id=watch_list_item.id).delete()
    return watchlist(request)

def Deletelisting(request, auctionListing_id):
    deleted = AuctionListing.objects.get(pk=auctionListing_id).delete()
    return watchlist(request)

@login_required(login_url='/login')
def AddComment(request, auctionListing_id):
    user = User.objects.get(id=request.user.id)
    auctionListing = AuctionListing.objects.get(pk=auctionListing_id)
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            AddComment = form.save(commit=False)
            AddComment.user = user
            AddComment.save()
            auctionListing.comments.add(AddComment)
            auctionListing.save()

            return HttpResponseRedirect(reverse('auctionListing', args=(auctionListing.id,)))
        else:
            return render(request, "auctions/comment.html", {
                "form": form,
                "auctionListing_id": auctionListing.id,
            })
    else:
        return render(request, "auctions/comment.html", {
            "form": CreateComment(),
            "auctionListing_id": auctionListing.id
        })

@login_required(login_url='/login')
def MakeBid(request,auctionListing_id):
    user = User.objects.get(id=request.user.id)
    auctionListing = AuctionListing.objects.get(pk=auctionListing_id)
    makebid = Bid.objects.all()
    

    if request.method == "POST":
        
        bid_amounts = float(request.POST["bid_amount"])
        form = CreateBid(request.POST)
    
        if form.is_valid():
            form.save()
           
            if user.id != AuctionListing.seller:
                if bid_amounts > auctionListing.starting_bid:

                    makebid=form.save(commit=False)
                    makebid.user_id = user.id
                    makebid.listing_id_id= auctionListing_id
                    makebid.save()
                    auctionListing.starting_bid = bid_amounts
                    auctionListing.save()
            
                    messages.success(request, 'Bid entered successfully')
                    return HttpResponseRedirect(reverse('auctionListing', args=(auctionListing.id,)))
        
                else:
                    messages.warning(request, 'Please Note: Your Bid cannot be less than the Current Price')
                    return HttpResponseRedirect(reverse('auctionListing', args=(auctionListing.id,)))

            return render(request,"auctions/bid.html",{
                'form':form,
            }) 
        return render(request,"auctions/bid.html",{
                'form':form,
            }) 
    
    return render(request,"auctions/bid.html",{
                'form':CreateBid,
                
                
            }) 
                                                    
        
 
    
def CloseBid(request,auctionListing_id):
    user = User.objects.get(id=request.user.id)
    auctionListing = AuctionListing.objects.get(pk=auctionListing_id)
    #upadting a database object
    auctionListing.status=False
    auctionListing.save()
    #bid = Bid.objects.get(pk=auctionListing_id)
    bid = Bid.objects.filter(listing_id=auctionListing_id).latest('bid_amount')
    bid.winner=True
    bid.save()

    return render(request, "auctions/index.html", {
        "ActiveListings": AuctionListing.objects.all(),
        "bid_winner": bid
    })

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories,
    })


def category(request, cats):
    category_auction = AuctionListing.objects.filter(category=cats)
    return render(request, 'auctions/category.html', {
        'category': cats,
        'ActiveListings': category_auction
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        current_user=user
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
