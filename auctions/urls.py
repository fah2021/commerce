from django.urls import path

from auctions.forms import CreateBid

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:auctionListing_id>", views.auctionListing, name = "auctionListing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("AddComment/<int:auctionListing_id>", views.AddComment,name ="AddComment"),
    path("MakeBid/<int:auctionListing_id>", views.MakeBid,name ="MakeBid"),
    path("CloseBid/<int:auctionListing_id>", views.CloseBid, name="CloseBid"),
    path("categories", views.categories, name="categories"),
    path("category/<str:cats>", views.category, name = "category"),
    path("Addwatchlist/<int:auctionListing_id>", views.Addwatchlist, name="Addwatchlist"),
    path("Removewatchlist/<int:auctionListing_id>", views.Removewatchlist, name="Removewatchlist"),
    path("Deletelisting/<int:auctionListing_id>", views.Deletelisting, name="Deletelisting"),
]
