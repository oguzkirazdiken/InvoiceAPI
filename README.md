### InvoiceAPI

In this project, I have created a RESTful web service that can store the Invoice and Contact information on [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2-deutm_source=google&utm_campaign=gs_emea_germany_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624524&adgroup=115749704783&gclid=CjwKCAiA5t-OBhByEiwAhR-hm9zKdGkvYYW893fru0AJFUi7a59PVdXMhFLSSXOr7HQ54r7sU8bqfRoCnUkQAvD_BwE) and suggest possible Contacts according to partial inputs.

API Views, TestCases are developed on [Django Rest Framework](https://www.django-rest-framework.org/) and the data model is provided with the help of [mongoengine](http://mongoengine.org/) connector.

The following table shows overview of the REST APIs:

|    Methods    |         Urls           |                    Actions                      |
| ------------- | ---------------------  | ----------------------------------------------- |
|     POST      | api/invoiceCreate/     |              create new Invoice                 |
|     POST      | api/contactCreate/     |              create new Contact                 |
|     PUT       | api/contactUpdate/_id  |            update existing Contact              |
|     GET       | api/contactSuggest/    | suggest existing Contacts with confidence ratio |


### Data Ingestion

Example payload for creating invoice:

```json
{
    "_id": "be015d569de9",
    "organization": "bc93b755a48f",
    "createdAt": "2021-10-11T09:53:31.339Z",
    "updatedAt": "2021-11-29T13:15:19.500Z",
    "amount": {
        "currencyCode": "EUR",
        "value": 26.3
    },
    "contact": {
        "_id": "845ec3d17501",
        "iban": "DE88100500001310032358",
        "name": "Oguz Kirazdiken",
        "organization": "bc93b755a48f"
    },
    "invoiceDate": "2021-10-11T00:00:00.000Z",
    "invoiceId": "c8b6299890f3"
}
```
So the data model should be capable of storing collections that's why mongoengine is a better option for MongoDB connector.

The Invoice payload also consists of contact information. Additional `create` method is added to `InvoiceSerializer` to extract that data and store it in the contact collections.

Example payload for creating and updating contact:

```json
{
    "_id": "845ec3d17501",
    "iban": "DE88100500001310032358",
    "name": "Oguz Kirazdiken New",
    "organization": "bc93b755a48f"
}
```

|    Methods    |         Urls                    |
| ------------- | ------------------------------  |
|     POST      | api/contactCreate/              |
|     PUT       | api/contactUpdate/845ec3d17501/ |


### Contact Suggestion
Payload for the contact suggestion endpoint needs to have two parts. `contactName` can be a partial input for any name and `organization` is a company representitive Id string. The aim of the endpoint is returning the most equivalent contacts with some certain confidence ratio.

|    Methods    |         Urls           |                    Actions                      |
| ------------- | ---------------------  | ----------------------------------------------- |
|     GET       | api/contactSuggest/    | suggest existing Contacts with confidence ratio |


GET Request Payload:

```json
{
    "contactName": "Kirazdiken",
    "organization": "bc93b755a48f"
}
```

Response:

```json
[
    {
        "suggestedContact": "Ayla Kirazdiken",
        "confidence": 0.5
    },
    {
        "suggestedContact": "Oguz Kirazdikene",
        "confidence": 0.5
    }
]
```

### Test Cases

Two different databases are defined for MongoDB. `is_test()` method converts the default database to test before running test cases.

```python
MONGODB_DATABASES = {
    "default": {
        "name": "invoice_database",
        "host": "localhost",
        "port": 27017
    },
    "test": {
        "name": "invoice_database_test",
        "host": "localhost",
        "port": 27017,
    }
}
```

There are two different case classes at `tests.py`. 
`InvoiceCreateAPITest` is checking the insert operations for invoice collection.
`ContactUpdateAPITest` checks whether the update operation performed is correct.

```python
python3 manage.py test
```

```bash
Using a test mongo database
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.020s

OK
Destroying test database for alias 'default'...
```




