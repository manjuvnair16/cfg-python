place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

location_details = place['location']
print(location_details)
print(location_details['longitude'])
print(location_details['latitude'])



print(place['name'])
print(place['post_code'])
print(place['street_number'])