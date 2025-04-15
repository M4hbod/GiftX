from django.urls import path

from products.views import GiftCardCategoryView, BrandCategoryListView

app_name = "products"

urlpatterns = [
    path("brand-category/", BrandCategoryListView.as_view(), name="brand_category_list"),
    path("<str:category_id>/", GiftCardCategoryView.as_view(), name="gift_card_category_detail"),
]
