from django.contrib import admin

from gift_cards.models import GiftCard, GiftCardCategory, GiftCardCode, GiftCardCountry


@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "country", "price")
    search_fields = ("title",)
    list_filter = ("category", "country")
    ordering = ("-created_at",)
    list_per_page = 20


@admin.register(GiftCardCategory)
class GiftCardCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)
    ordering = ("-created_at",)
    list_per_page = 20


@admin.register(GiftCardCountry)
class GiftCardCountryAdmin(admin.ModelAdmin):
    list_display = ("country_code", "description")
    search_fields = ("country_code",)
    ordering = ("-created_at",)
    list_per_page = 20


@admin.register(GiftCardCode)
class GiftCardCodeAdmin(admin.ModelAdmin):
    list_display = ("gift_card", "code", "created_at", "used_at")
    search_fields = ("code",)
    ordering = ("-created_at",)
    list_per_page = 20
