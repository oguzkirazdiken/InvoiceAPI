from rest_framework import serializers, fields
from api.models import Invoice, Contact
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer


class ContactSerializer(DocumentSerializer):
    _id = serializers.CharField()

    class Meta:
        model = Contact
        fields = '__all__'


class InvoiceSerializer(DocumentSerializer):
    _id = serializers.CharField()
    contact = ContactSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        contact_data = validated_data['contact']
        invoice = Invoice.objects.create(**validated_data)
        Contact.objects.create(**contact_data)
        return invoice
