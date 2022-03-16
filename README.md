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

### Installation

To get the project up and running in your local, go to the file location you want to install and run the following command.

```python
git clone https://github.com/oguzkirazdiken/InvoiceAPI.git
```

It is highly recommended to run on virtual environment. Firstly, set your virtual env and activate it.

```python
python3 -m venv env
source env/bin/activate
```

Change current working directory to the directory where requirements.txt is located and run the following code in your shell.

```python
cd InvoiceApi
pip3 install -r requirements.txt
```
If you previously installed MongoDB and started to run a database on your local, the mongoengine itself starts a database instance automatically when you give the runserver command. To be sure, please check if you installed MongoDB and you have a running database. Helpful documentation [here](https://mongoing.com/docs/tutorial/install-mongodb-on-os-x.html).

The mongoengine doesn't require any migration process like other MongoDB Connectors. But we have an spare SQLite database. So it is good to start with initial migration before running our Django Rest API.

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

```python
python3 manage.py runserver
```

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

```python
def create(self, validated_data):
    contact_data = validated_data['contact']
    invoice = Invoice.objects.create(**validated_data)
    Contact.objects.create(**contact_data)
    return invoice
```

Invoice creating process takes 63ms on average.


Example payload for creating and updating contact:

```json
{
    "_id": "845ec3d17501",
    "iban": "DE88100500001310032358",
    "name": "Oguz Kirazdiken New",
    "organization": "bc93b755a48f"
}
```
Updating contact takes 118ms on average.

Updating and creating contact has the same payload type but should be requested for different URLs with different methods.

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




