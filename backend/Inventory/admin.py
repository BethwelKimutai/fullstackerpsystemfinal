from django.contrib import admin
from .models import (
    ProductCategory, ProductTemplate, Product, ReplenishOrder,
    Inventory, Receipt, Delivery, InternalTransfer, PhysicalInventory, Scrap,
    LandedCost, ProductAttribute, UnitOfMeasureCategory, ProductPackaging,
    ReorderingRule, BarcodeNomenclature
)

# Define custom admin classes
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

class ProductTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

class ReplenishOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number')  # Adjust the fields as necessary

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number')  # Adjust the fields as necessary

class InternalTransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number')  # Adjust the fields as necessary

class PhysicalInventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class ScrapAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class LandedCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

class UnitOfMeasureCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

class ProductPackagingAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class ReorderingRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary

class BarcodeNomenclatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Adjust the fields as necessary

# Register the models with the custom admin classes
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductTemplate, ProductTemplateAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ReplenishOrder, ReplenishOrderAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(InternalTransfer, InternalTransferAdmin)
admin.site.register(PhysicalInventory, PhysicalInventoryAdmin)
admin.site.register(Scrap, ScrapAdmin)
admin.site.register(LandedCost, LandedCostAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(UnitOfMeasureCategory, UnitOfMeasureCategoryAdmin)
admin.site.register(ProductPackaging, ProductPackagingAdmin)
admin.site.register(ReorderingRule, ReorderingRuleAdmin)
admin.site.register(BarcodeNomenclature, BarcodeNomenclatureAdmin)
