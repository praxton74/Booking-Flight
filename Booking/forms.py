from django.forms import ModelForm
from Booking.models import Flight, Ticket

class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields=['code','origin','destination','date','time']

class TicketForm(ModelForm):
    class Meta:
        model=Ticket
        fields=['first_name','last_name','email','contact','address']
