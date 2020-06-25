from django.core.management.base import BaseCommand
from test_bank_task2.models import LostDocument, DocumentType
import json
import requests
from pprint import pprint
from requests_html import HTMLSession



class Command(BaseCommand):
    help = 'Add post'
    # изначально был другой парсер, он был больше по ТЗ но я несмог довести доконца(можно посмотреть в pars_json).
    session = HTMLSession()
    url = session.get('https://data.gov.ua/dataset/41d166e9-d1b8-4a54-8e0a-363b02e2f11d/')
    spisok_link = url.html.xpath('//*[@id="dataset-resources"]/ul//a//@href')
    main_url = []
    for i in spisok_link:
        if i.startswith('https') and not i.endswith('shema.json'):
            main_url.append(i)
    url = main_url[0]
    response = requests.get(url)
    total_save = response.json()

    def handle(self, *args, **options):
        for i in self.total_save[:2]:
            identifier = i['ID']
            serial_number_doc = i['D_SERIES']
            number_doc = i['D_NUMBER']
            document_type = DocumentType.objects.get(pk=1)
            status = i['D_STATUS']
            date_incident = i['INSERT_DATE']
            date_recording = i['THEFT_DATA']
            ovd = i['OVD']


            LostDocument.objects.create(
                identifier=identifier, serial_number_doc=serial_number_doc, number_doc=number_doc,
                document_type=document_type, status=status, date_incident=date_incident,
                date_recording=date_recording, ovd=ovd
            )

            self.stdout.write('Success add posts')