#Nesting

capital = {
    "France":"Paris",
    "Germany":"Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France":{
        "cities_visited": ["Paris", "lille", "Dijon"],
        },
    "Germany":["Berlin", "Hamburg", "Stuttgart"],
    }

# Nesting a dictionary in a dictionary
travel_log = {
    "France":{
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visits" : 12,
        },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5,
        },
    "Dominican Republic":{
        "cities_visited":["La Romana", "Santo Domingo", "Punta Cana"],
        "total_visits": "too many",
        }
        }

# Nesting a Dictionary in a List
travel_log = [
    {
        "country" : "France",
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visits" : 12
    },

    {
       "country" : "France",
       "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
       "total_visits" : 5
    },

    {

    },
]
