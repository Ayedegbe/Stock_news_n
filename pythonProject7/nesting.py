#Nesting
capitals ={
 #   "France": "Paris,"
  #  "Germany": "Berlin",
}
# list in a dictionary
#travel_log = {
   # "France": ["Paris", "Lille", "Dijon"],
    #"Germany":["Berlin","Hamburg", "Stuttgart",]
#}
#nesting a dictionary in a dictionary
#travel_log = {
#    "France":{ "cities_visited":["Paris", "Lille", "Dijon"],"total_visit": = "5"}
 #   "Germany":["Berlin","Hamburg", "Stuttgart",]
#}
#nesting dictionary in a list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def new_country(country_visited,times_visited,cities_visited):
    new_country = {}
    new_country["country"] =  country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    print(travel_log)
new_country("Russia",5,"Moscow , Saint Petersburg")