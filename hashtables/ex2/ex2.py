#  Hint:  You may not need all of these.  Remove the unused functions.
# need to create a cache to store flight info
# then need to create list to store all of the flights/routes

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flight_cache = {}

# Create empty route list
    route = []

# Put all destinations in the cache
    for ticket in tickets:
        flight_cache[ticket.source] = ticket.destination

    # set first flight to NONE / initialize
    current_flight = flight_cache["NONE"]
    # while it's not the last flight
    # go ahead and append current flight
    while current_flight != "NONE":
        route.append(current_flight)
        current_flight = flight_cache[current_flight]
    route.append(current_flight)

    return route
