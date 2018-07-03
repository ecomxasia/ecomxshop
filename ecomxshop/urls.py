"""ecomxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. thAdd an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.apiviews import ProductList, ProductDetail
from commoncode.apiviews import BrandList, BrandDetail, OriginList, OriginDetail
from customer.apiviews import LoginView, UserCreate
from sample.views import PollList, PollDetail, PollViewSet
from sample.views import ChoiceList, CreateVote
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", ProductList.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="products_detail"),
    path("brands/", BrandList.as_view(), name="brands_list"),
    path("brands/<int:pk>/", BrandDetail.as_view(), name="brands_detail"),
    path("origins/", OriginList.as_view(), name="origins_list"),
    path("origins/<int:pk>/", OriginDetail.as_view(), name="origins_detail"),
    path('login/', LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    #path("polls/", PollList.as_view() , name="polls_list"),
    #path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    #path("choices/",ChoiceList.as_view() , name="choice_list"),
    #path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls