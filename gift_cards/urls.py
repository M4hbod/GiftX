from django.urls import path

from gift_cards.views import GiftCardCategoryView, BrandCategoryListView

app_name = "gift_cards"

urlpatterns = [
    path("<str:category_id>/", GiftCardCategoryView.as_view(), name="gift_card_category_detail"),
    path("brand-category/", BrandCategoryListView.as_view(), name="brand_category_list"),
]
