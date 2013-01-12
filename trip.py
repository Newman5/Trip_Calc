##A simple calculator to figure out gas costs for a roadtrip
##by Newman Lanier 1/11/2013
##possible expansion:
##    using the google maps api to find distance between two points
##    using a gas price finder api to find the gas price on route
##    using the NPR api to find radio stations on the route
##    putting on the web using stuff learned in the Udacity web app class
##Note:
##    Why do silly little practices like this?  To find little holes in your understanding
##    like the difference between float() and int()
##


def get_distance(a,b):
    #Maybe figure with google map API?
    return distance

#what about an API to find the price along the route?
gas_gal = raw_input("How much is gas per gallon?")
mile_gal= raw_input("What is the MPG of your car?")
distance= raw_input("How far do you want to travel?")

def calc_trip_gals(distance, mile_gal):
    #divide the total trip distance by the MPG
    trip_gals = int(distance)/int(mile_gal)
    return float(trip_gals)

def calc_trip_cost(trip_gals,gas_gal):
    trip_cost = float(trip_gals)* float(gas_gal)
    return trip_cost

trip_gals = calc_trip_gals(distance,mile_gal)

print "the number of gallons:", trip_gals
print "the cost in fuel for the trip:", calc_trip_cost(trip_gals,gas_gal)


