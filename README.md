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

Change current working directory to the directory where requirements.txt is located and run the following cone in your shell.

```python
cd InvoiceApi
pip3 install -r requirements.txt
```

