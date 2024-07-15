from django.contrib import admin
from .models import Vendor, RequestForQuotation, PurchaseOrderProduct, PurchaseOrder, RFQProduct, VendorPriceList


# Define custom admin classes
class VendorAdmin(admin.ModelAdmin):
    def display_name_or_company(self, obj):
        if obj.is_individual:
            return obj.name
        else:
            return obj.company_name

    display_name_or_company.short_description = 'Name or Company'  # Custom column header

    list_display = ('id', 'display_name_or_company')


class RequestForQuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference')  # Adjust the fields as necessary


class PurchaseOrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'PurchaseOrderNo')  # Adjust the fields as necessary


class RFQProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')  # Adjust the fields as necessary


class VendorPriceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'product')  # Adjust the fields as necessary


# Register the models with the custom admin classes
admin.site.register(Vendor, VendorAdmin)
admin.site.register(RequestForQuotation, RequestForQuotationAdmin)
admin.site.register(PurchaseOrderProduct, PurchaseOrderProductAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(RFQProduct, RFQProductAdmin)
admin.site.register(VendorPriceList, VendorPriceListAdmin)
