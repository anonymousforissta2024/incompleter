#Source: https://stackoverflow.com/questions/72341946/typeerror-not-supported-between-instances-of-str-and-float
import requests

def get_ids():
    url = "https://retro.umoiq.com/service/publicJSONFeed?command=vehicleLocations&a=sf-muni&t=0"
    response = requests.get(url).json()

    id_list = []

    for id in response['vehicle']:
        lat = id['lat']
        lon = id['lon'] 
        
        if (lat <= 37.769754 and lat >= 37.748554): 
            if (lon >= -122.427050 and lon <= -122.404535):
                id_list.append(id['id'])
    
    return id_list

def main():
    print(get_ids())

if __name__ == "__main__":
    main()