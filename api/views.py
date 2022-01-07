from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import InvoiceSerializer, ContactSerializer
from api.models import Invoice, Contact


@api_view(['POST'])
def invoice_create(request):
    invoice_serializer = InvoiceSerializer(data=request.data)

    if invoice_serializer.is_valid():
        invoice_serializer.save()

    return Response(invoice_serializer.data)


@api_view(['POST'])
def contact_create(request):
    contact_serializer = ContactSerializer(data=request.data)

    if contact_serializer.is_valid():
        contact_serializer.save()

    return Response(contact_serializer.data)


@api_view(['PUT'])
def contact_update(request, pk):
    contact = Contact.objects.get(_id=pk)
    contact_serializer = ContactSerializer(contact, data=request.data)
    if contact_serializer.is_valid():
        contact_serializer.save()

    return Response(contact_serializer.data)


@api_view(['GET'])
def contact_suggest(request):
    request_data = JSONParser().parse(request)
    contacts = Contact.objects.filter(name__icontains=request_data['contactName'],
                                      organization=request_data['organization'])

    if not contacts:
        return JsonResponse({'message': 'The contact does not exist'}, status=status.HTTP_404_NOT_FOUND)

    else:
        contacts_serializer = ContactSerializer(contacts, many=True)
        response_data = []
        for i in contacts_serializer.data:
            contact = {"suggestedContact": i['name'], "confidence": 1/len(contacts_serializer.data)}
            response_data.append(contact)
        return Response(response_data)
