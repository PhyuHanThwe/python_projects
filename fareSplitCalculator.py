def split_fare(fare, passengers, feature_cost):

    share = fare/passengers
    print (f"Splitting the ${fare} fare between {passengers} passengers...")

    share_cost = share + feature_cost
    print (f"Adding a ${feature_cost} feature_cost...")
    return share_cost

fare_cost = 50
passengers = int(input("Enter the number of passengers: "))
feature_cost = 0.5

share_cost = split_fare(fare_cost, passengers, feature_cost)

print("Each pays: ${}".format(share_cost))