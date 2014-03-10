from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from contacts.models import Contact, Donation

import csv
import datetime

class Command(BaseCommand):
    args = "csv"
    help = "upload_donor <csv> must be download from google checkout"

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("RTFM: " + self.help)
        try:
            self.upload(args[0])
        except IntegrityError, e:
            print e

    def upload(self, csv_file):
        reader = csv.reader(open(csv_file, 'rU'))
        for index, row in enumerate(reader):
            if index == 0:
                continue
            else:
                print row
                if row[4]:
                    contact, created = Contact.objects.get_or_create(email=row[4])
                elif row[12]:
                    contact, created = Contact.objects.get_or_create(phone_primary=row[12])
                else:
                    contact, create = Contact.objects.get_or_create(first_name=row[5])
                print created
                # if created:
                contact.first_name = row[5]
                contact.address = row[6]+row[7]
                contact.state = row[9]
                contact.phone_primary = row[12]
                contact.save()
                print contact.subscriber
                if row[3] == "no" and contact.subscriber:
                    contact.subscriber.is_active = False
                    contact.subscriber.save()

                donation = Donation(amount=row[2],
                                    date=datetime.datetime.strptime(row[0], '%m/%d/%y %H:%M'),
                                    type=u'o',
                                    contact=contact
                                    )
                donation.save()
                contact.donations.add(donation)