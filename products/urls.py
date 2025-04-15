from django.urls import path

from products.views import GiftCardBrandProductsView, BrandCategoryListView

app_name = "products"

urlpatterns = [
    path("brand-category/", BrandCategoryListView.as_view(), name="brand_category_list"),
    path("<str:brand_id>/", GiftCardBrandProductsView.as_view(), name="gift_card_brand_products_detail"),
]
