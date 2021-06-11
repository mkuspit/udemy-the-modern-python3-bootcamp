print("How many kilomoters have you run today?")
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2)

print(f"Your {kms} km run is equal to {miles} miles.")