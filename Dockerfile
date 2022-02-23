FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN pip3 install --upgrade pip
RUN mkdir /invoiceapi
WORKDIR /invoiceapi
COPY . /invoiceapi/
RUN pip3 install -r requirements.txt