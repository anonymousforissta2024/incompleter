#Source: https://stackoverflow.com/questions/67339396/typeerror-in-string-requires-string-as-left-operand-not-type
import requests
import json
import wikipedia
#from datetime import datetime

response = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
meteorite_page = json.loads(response.text)

# Helper Functions
def get_meteorites(type = "all"):   
    if type == "all":
        names = [mtrt["name"] for mtrt in meteorite_page]
    else:
        names = [mtrt["name"] for mtrt in meteorite_page if type in mtrt["recclass"]]
        
    return names

def sort_by_feature(type):
    if type == "year":
        feature = [mtrt["year"] for mtrt in meteorite_page]   
    else:
        feature = [mtrt["mass"] for mtrt in meteorite_page]
        
    return feature
    
# Choice functions
def print_all():
    all_names = get_meteorites(type)
    for index, name in enumerate(all_names):
        print(f"{index + 1}: {name}")
    print(all_names)
    
def print_by_class():
    type = input("Enter a class (See this page for classification names/details --> stackoverflow made me take out this link): ").upper()
    all_names = get_meteorites(type)
    print(f"All {type} meteorites: ")
    for index, name in enumerate(all_names):
        print(f"{index + 1}: {name}")
    
def sort_by_year():
    all_years = sort_by_feature("year")
    for index, year in enumerate(all_years):
        print(f"{index + 1}: {year}")
    print(all_years)
    
def sort_by_mass():
    all_masses = sort_by_feature("mass")
    for index, mass in enumerate(all_masses):
        print(f"{index + 1}: {mass}")
    print(all_masses)
        
def meteorite_data():
    
    meteorite_name = input("Enter the name of a meteorite: ")
    
    for mtrt in meteorite_page:
        if meteorite_name in mtrt['name']:
            for key in mtrt:
                print(f"{key}: {mtrt[key]}")
    
    print("Wikipedia Summary: ")
    try:
        print(wikipedia.summary(f"{meteorite_name} (meteorite)"))
    except:
        print("No Wikipedia page could be found.")

# User interface
def start_interface():

    print("Meteorite Data Explorer")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
   
    while True:
        print("̲M̲e̲n̲u̲ ̲")
        print("1. List the names of all Earth meteorite landings")
        print("2. See all meteorites in one class")
        print("3. Organize meteorites from oldest to newest")
        print("4. Organize meteorites from biggest to smallest")
        print("5. Access the data of an individual meteorite")
        print("0. Quit")
        choice = input("Select an option: ")
        
        if choice == "1":
            print_all()
        elif choice == "2":
            print_by_class()
            print('')
        elif choice == "3":
            sort_by_year()
            print('')
        elif choice == "4":
            sort_by_mass()
            print('')
        elif choice == "5":
            meteorite_data()
            print('')
        elif choice == "0":
            print("Exit")
            break
        else:
            print("That is not an option.")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        

if __name__ == "__main__":
    start_interface()