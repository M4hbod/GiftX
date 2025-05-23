from django.shortcuts import render
from django.views import View
from django.db.models import Q
from gift_cards.models import GiftCard, BrandCategory

class GiftCardCategoryView(View):
    def get(self, request, category_id=None):
        gift_cards = GiftCard.objects.all()

        if category_id:
            gift_cards = gift_cards.filter(category_id=category_id)

        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")
        if min_price:
            gift_cards = gift_cards.filter(price__gte=min_price)
        if max_price:
            gift_cards = gift_cards.filter(price__lte=max_price)

        country_ids = request.GET.get("countries")
        if country_ids:
            ids = [int(cid) for cid in country_ids.split(",") if cid.isdigit()]
            if ids:
                gift_cards = gift_cards.filter(country_id__in=ids)

        context = {
            "gift_cards": gift_cards
        }
        return render(request, "gift_cards/gift_card_category_detail.html", context)


class BrandCategoryListView(View):
    def get(self, request):
        categories = BrandCategory.objects.prefetch_related("brands").all()
        return render(request, "gift_cards/brand_category_list.html", {"categories": categories})
