from django.shortcuts import render
from django.views import View

from gift_cards.models import GiftCard, BrandCategory


class GiftCardCategoryView(View):
    def get(self, request, category_id=None):
        gift_cards = GiftCard.objects.filter(category__id=category_id)
        return render(request, "gift_cards/gift_card_category_detail.html", {"gift_cards": gift_cards})


class BrandCategoryListView(View):
    def get(self, request):
        categories = BrandCategory.objects.prefetch_related("brands").all()
        return render(request, "gift_cards/brand_category_list.html", {"categories": categories})
