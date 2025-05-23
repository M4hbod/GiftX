from django.urls import path
from gift_cards.views import GiftCardCategoryView, BrandCategoryListView

app_name = "gift_cards"

urlpatterns = [
    path("category/", GiftCardCategoryView.as_view(), name="gift_card_all"),  # همه گیفت‌کارت‌ها
    path("category/<int:category_id>/", GiftCardCategoryView.as_view(), name="gift_card_category_detail"),  # بر اساس دسته
    path("brand-category/", BrandCategoryListView.as_view(), name="brand_category_list"),  # برندها
]
