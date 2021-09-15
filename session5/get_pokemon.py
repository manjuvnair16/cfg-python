import requests

pokemon_id = input('Enter the pokemon id: ')
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)

response = requests.get(url)
pokemon_data = response.json()
#print(pokemon_data.keys())
print(pokemon_data['height'])
print(pokemon_data['weight'])
print(pokemon_data['name'])
pokemon_moves = pokemon_data['moves']
for each_move in pokemon_moves:
    print(each_move['move']['name'])
