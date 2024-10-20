import json

def transform_data(data):
    transformed_data = []
    
    # Get the first set of keys for the header row
    headers = data.pop('City', None)
    
    # Ensure headers are in the correct format
    if headers:
        headers['City'] = 'City'
        transformed_data.append(headers)
    
    # Iterate through the remaining data
    for city, details in data.items():
        details['City'] = city
        # Check and transform 'Number2' value if necessary
        if details.get('Number2') == 'None':
            details['Number2'] = 'none'
        transformed_data.append(details)
    
    return transformed_data

def main():
    # Read the JSON file
    with open('branches.json', 'r') as f:
        data = json.load(f)
    
    # Transform the data
    transformed_data = transform_data(data)
    
    # Write the transformed data back to a JSON file
    with open('transformed_file.json', 'w') as f:
        json.dump(transformed_data, f, indent=4)

if __name__ == "__main__":
    main()
