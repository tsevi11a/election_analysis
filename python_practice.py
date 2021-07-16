counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(i)

counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in len(counties_tuple):
      print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, votes in counties_dict.items():
    print(f"{county} county has {votes:,} registered voters")

