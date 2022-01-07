from django.urls import reverse
from rest_framework.test import APITestCase


from api.models import Invoice, Contact

class InvoiceCreateAPITest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('invoice_create')

    def test_create_invoice(self):
        self.assertEquals(
            Invoice.objects.count(),
            0
        )

        data = {
            '_id': '_id',
            'organization': 'organization'
        }

        invoice = Invoice(_id=data['_id'], organization=data['organization'])
        invoice.save()

        self.assertEquals(
            Invoice.objects.count(),
            1
        )
        invoice = Invoice.objects.first()
        self.assertEquals(
            invoice._id,
            data['_id']
        )
        self.assertEquals(
            invoice.organization,
            data['organization']
        )

class ContactUpdateAPITest(APITestCase):
    def setUp(self) -> None:
        self.contact = Contact(_id='_id', iban='iban', name='name', organization='organization')
        self.contact.save()
        self.url = reverse('contact_update', kwargs={'pk': self.contact.pk})

    def test_update_contact(self):
        old_contact = Contact.objects.get(_id=self.contact.pk)
        new_contact = Contact(_id=old_contact['_id'], iban='new_iban', name='new_name', organization='new_organization')
        new_contact.save()
        contact = Contact.objects.first()
        self.assertEquals(
            contact.iban,
            'new_iban'
        )
        self.assertEquals(
            contact.name,
            'new_name'
        )
        self.assertEquals(
            contact.organization,
            'new_organization'
        )

