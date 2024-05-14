#Source: https://stackoverflow.com/questions/50348992/django-attributeerror-module-clients-has-no-attribute-models
from django.db import models
import datetime
import calendar
import clients.models
from django.core.urlresolvers import reverse


# Create your models here.


class PartnerInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    price = models.IntegerField()


class NewPartnerLead(models.Model, LeadStage):
    new_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    lead_stage = LeadStage.lead_stage()


class Booking(models.Model, ClientLead):
    number_of_bookings = models.IntegerField()
    clients_name = ClientLead.client_name()
    clients_phone = ClientLead.phone_number()
    clients_email = ClientLead.email_address()

    class BookingDetail(Booking):
        start_date = datetime.datetime.date()
        end_date = datetime.datetime.date()
        destination = models.CharField(max_length=50)

        @static
        def number_of_days(self, start_date, end_date):

            return end_date-start_date


class Payment(models.Model, PartnerInfo.price, Booking.BookingDetail.number_of_days):
    cash_out = models.IntegerField()

    @static
    def client_payment(self, number_of_days, price):
        return price*number_of_days

    @static
    def provider_cut(self, client_payment):
        provider_cut = 0.8*client_payment
        return provider_cut

    @static
    def balance(self, provider_cut):
        provider_cut-cash_out

class Action(Actions):
    status = Actions.status()
    action = Actions.action()