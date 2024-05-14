#Source: https://stackoverflow.com/questions/76331642/python-typeerror-nonetype-object-not-iterable-whats-causing-it
def get_input_data():
    # Some code to retrieve input data
    return input_data

def process_data(data):
    processed_items = []
    for item in data:
        processed_item = item * 2
        processed_items.append(processed_item)
    return processed_items

def main():
    input_data = get_input_data()
    processed_data = process_data(input_data)
    print(processed_data)
    # Rest of the code

if __name__ == "__main__":
    main()