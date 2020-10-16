# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum,Min, Sum, Avg
from django.db.models import Q , F

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"


# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFreightByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="freight_by_origin.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFreightByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','dest_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="freight_by_destination.html"

# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="mail_by_origin.html"
# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','dest_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="mail_by_destination.html"
# What are the top 5 airports in terms of: Distance mail by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="distance_by_origin.html"


# What are the top 5 airports in terms of: Total Distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','dest_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="distance_by_destination.html"

# Which airport reported the most passenger by month
class TopPassengerByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passenger_month.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Sum('passengers')) \
                .order_by('-total_passengers')[0:1]

            month_list.append(queryset)

        # return list
        return month_list

# Which airline reported the most freight carried?
class TopAirlineByfreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(sum_freight=Sum('freight'))\
                        .order_by('-sum_freight')[0:1]
    template_name="top_airline_by_freight.html"

# Which airline reported the most passenger carried?

class TopAirlineByPassenger(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(sum_passengers=Sum('passengers'))\
                        .order_by('-sum_passengers')[0:1]
    template_name="top_airline_by_passengers.html"

# Which airline reported the most mail carried?

class TopAirlineByMail(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(sum_mail=Sum('mail'))\
                        .order_by('-sum_mail')[0:1]
    template_name="top_airline_by_mail.html"

# Which airline reported the longest flight distance?

class TopAirlineByDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(max_distance=Sum('distance'))\
                        .order_by('-max_distance')[0:1]
    template_name="top_airline_by_distance.html"

# Rank order passengers carried, by month 
class RankPassengerByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_passenger_month.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('month','carrier_name') \
                .filter(month__exact=month) \
                .filter(carrier_name__in = ['American Airlines Inc.','Alaska Airlines Inc.','Delta Air Lines Inc.','United Air Lines Inc.','Southwest Airlines Co.']) \
                .annotate(total_passengers=Sum('passengers')) \
                .order_by('-total_passengers')[0:1]
            

            month_list.append(queryset)

        # return list
        return month_list


# Find the average number of passengers for flights into given airports 
class AvgPassengerByAirport(ListView):

    context_object_name = "airport_list"
    queryset = MarketData.objects \
                         .values('dest_city_name','dest_iata_code') \
                         .filter(dest_iata_code__in = ['LAX','SFO','DFW','ATL','ORD']) \
                         .annotate(avg_passengers=Avg('passengers')) \
                         .order_by('-avg_passengers')[0:5]

    template_name="avg_passenger_airport.html"

# Find the average volume of freight for flights departing from given airports 
class AvgVolFreightByAirport(ListView):

    context_object_name = "airport_list"
    queryset = MarketData.objects \
                         .values('orig_city_name','orig_iata_code') \
                         .filter(dest_iata_code__in = ['MIA','MEM','JFK','ANC','SDF']) \
                         .annotate(avg_freight=Avg('freight')) \
                         .order_by('-avg_freight')[0:5]
    print("TEST",type(queryset))

    template_name="avg_freightvol_depart.html"

# What city pairs represent the most freight carried for the longest distance?

class TopCityPairsByLogestDistance(ListView):
    context_object_name = "airport_list"
    template_name="top_city_pairs_by_longest_distance.html"

    def get_queryset(self):

        city_pair_list = []
        queryset = MarketData.objects \
                        .values('id','orig_city_name','dest_city_name','freight','distance') \
                        .annotate(max=Max (F('distance') + F('freight')))\
                        .order_by('-max','id','orig_city_name','dest_city_name','freight','distance').first()
        city_pair_list.append(queryset)


        return city_pair_list
    
# What city pairs represent the most mail carried for the shortest distance?

class TopCityPairsMaxMailMinDistance(ListView):
    context_object_name = "airport_list"
    template_name="top_city_pairs_by_maxmail_mindistance.html"

    def get_queryset(self):

        city_pair_list = []
        queryset = MarketData.objects \
                        .values('id','orig_city_name','dest_city_name','mail','distance') \
                        .annotate(max=Max (F('mail') )+ Min(F('distance')))\
                        .order_by('-max','id','orig_city_name','dest_city_name','mail','distance').first()
        city_pair_list.append(queryset)

        return city_pair_list