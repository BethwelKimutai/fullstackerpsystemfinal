from rest_framework import serializers

from .models import Vendor, RequestForQuotation, PurchaseOrder, PurchaseOrderProduct, RFQProduct, VendorPriceList


class VendorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = Vendor
        fields = ['id', 'type', 'name', 'company_name', 'contact_street1', 'contact_street2', 'contact_city',
                  'contact_state', 'contact_zip', 'contact_country', 'tax_id', 'job_position', 'phone', 'mobile',
                  'email', 'website', 'title', 'tags', 'vendor_company']


class VendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['type', 'name', 'company_name', 'contact_street1', 'contact_city', 'contact_zip', 'contact_country',
                  'tax_id', 'email', 'phone', 'mobile']

    def validate(self, data):
        if data['type'] == 'individual':
            required_fields = ['name', 'contact_street1', 'contact_city', 'contact_zip', 'contact_country', 'tax_id',
                               'email', 'mobile']
        elif data['type'] == 'company':
            required_fields = ['company_name', 'contact_street1', 'contact_city', 'contact_zip', 'contact_country',
                               'tax_id', 'email', 'phone']
        else:
            raise serializers.ValidationError("Invalid vendor type")

        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} is required for {data['type']}")

        if data['type'] == 'company':
            data['name'] = None

        return data


class RFQProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFQProduct
        fields = ['product', 'quantity', 'unit_price', 'subtotal']


class RequestForQuotationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    products = RFQProductSerializer(many=True)

    class Meta:
        model = RequestForQuotation
        fields = ['id', 'vendor', 'vendor_reference', 'currency', 'order_deadline', 'expected_arrival', 'deliver_to',
                  'taxes', 'tax_excluded', 'total', 'company', 'buyer', 'reference', 'created_at', 'products']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        rfq = RequestForQuotation.objects.create(**validated_data)
        for product_data in products_data:
            RFQProduct.objects.create(rfq=rfq, **product_data)
        return rfq


class PurchaseOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderProduct
        fields = ['product', 'description', 'quantity', 'unit_of_measure', 'direct_unit_cost', 'discount',
                  'allow_invoice_discount', 'vat_identifier', 'amount']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    products = PurchaseOrderProductSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'company', 'vendor', 'order_date', 'expected_arrival', 'currency', 'purchase_order_no',
                  'products', 'description', 'discount', 'subtotal_less_discount', 'tax_rate', 'total_tax', 'shipping',
                  'other_costs', 'grand_total']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        purchase_order = PurchaseOrder.objects.create(**validated_data)
        for product_data in products_data:
            PurchaseOrderProduct.objects.create(purchase_order=purchase_order, **product_data)
        return purchase_order


class VendorPriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPriceList
        fields = '__all__'
