# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth ,\
                    Top5AirportsFreightByOrigin,\
                    Top5AirportsFreightByDestination,\
                    Top5AirportsMailByOrigin,\
                    Top5AirportsMailByDestination,\
                    Top5AirportsDistanceByOrigin,\
                    Top5AirportsDistanceByDestination,\
                    TopPassengerByMonth,\
                    TopAirlineByfreight,\
                    TopAirlineByPassenger,\
                    TopAirlineByMail,\
                    TopAirlineByDistance,\
                    TopCityPairsByLogestDistance,\
                    RankPassengerByMonth,\
                    AvgPassengerByAirport,\
                    AvgVolFreightByAirport,\
                    TopCityPairsMaxMailMinDistance       


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
  path('top5freightorigin/', 
        Top5AirportsFreightByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ),
        name="top5freightorigin"),
    path('top5freightdestination/', 
        Top5AirportsFreightByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ),
        name="top5freightdestination"),

    path('top5mailbyorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailbyorigin"),   

    path('top5maildestination/', 
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5maildestination"),
    path('top5distanceorigin/', 
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5distanceorigin"),
    path('top5distancedestination/', 
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5distancedestination"),
    path('toppassenger_month/',  
        TopPassengerByMonth.as_view(
            extra_context={'title': "Top Passenger by Month"}
        ), 
         name="toppassenger_month"),
     path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('topairline_freight/',  
        TopAirlineByfreight.as_view(
            extra_context={'title': "Top Airline by Freight"}
        ), 
        name="topairline_freight"),
    path('topairline_passenger/',  
        TopAirlineByPassenger.as_view(
            extra_context={'title': "Top Airline by Passenger"}
        ), 
        name="topairline_passenger"),
    path('topairline_mail/',  
        TopAirlineByMail.as_view(
            extra_context={'title': "Top Airline by Mail"}
        ), 
        name="topairline_mail"),
    path('topairline_distance/',  
        TopAirlineByDistance.as_view(
            extra_context={'title': "Top Airline by longest flight distance"}
        ), 
        name="topairline_distance"),
    path('rankpassenger_month/',  
        RankPassengerByMonth.as_view(
            extra_context={'title': "Top  Passengers Carried by Month"}
        ), 
        name="rankpassenger_month"),
    path('avg_passenger_airport/',  
        AvgPassengerByAirport.as_view(
            extra_context={'title': " Average number of passengers for flights "}
        ), 
        name="avg_passenger_airport"),
    path('avg_vol_freight_airport/',  
        AvgVolFreightByAirport.as_view(
            extra_context={'title': " Average number of passengers for flights into"}
        ), 
        name="avg_vol_freight_airport"),
    path('topcitypairs_longest_distance/',  
        TopCityPairsByLogestDistance.as_view(
            extra_context={'title': "City pairs represent the most freight carried for the longest distance"}
        ), 
        name="topcitypairs_longest_distance"),
    path('topcitypairs_max_mail_min_distance/',  
        TopCityPairsMaxMailMinDistance.as_view(
            extra_context={'title': "City pairs represent the most mail carried for the shortest distance"}
        ), 
        name="topcitypairs_max_mail_min_distance"),
]