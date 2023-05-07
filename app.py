import requests

# pokemon = "Ivysaur"
# pokemon = pokemon.lower() 
# response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
# data = response.json()
# print(data["stats"][0]["base_stat"]) #hp
# print(data["stats"][1]["base_stat"]) #attack
# print(data["stats"][2]["base_stat"]) #defense
# print(data["stats"][3]["base_stat"]) #special_attack
# print(data["stats"][4]["base_stat"]) #special defense
# print(data["stats"][5]["base_stat"]) #speed
# print(data["types"][0]["type"]["name"]) #type
# print(data["types"][1]["type"]["name"]) #type2
# print(data["weight"]) #weight

class App():

    def __init__(self,pokemon):
        self.pokemon = pokemon.lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.pokemon}")
        data = response.json()

        print(f"""
Name: {self.pokemon.capitalize()}

Stats:
- HP: {data["stats"][0]["base_stat"]}
- Attack: {data["stats"][1]["base_stat"]}
- Defense: {data["stats"][2]["base_stat"]}
- Special Attack: {data["stats"][3]["base_stat"]}
- Special Defense: {data["stats"][4]["base_stat"]}
- Speed: {data["stats"][5]["base_stat"]}

Types:
- {data["types"][0]["type"]["name"].capitalize()}
- {data["types"][1]["type"]["name"].capitalize()}
        
        """)

pokemon_name = input("Enter pokemon name: ")
try:
    app = App(pokemon=pokemon_name)
except:
    print("\n We encountered with a problem , check your connection or pokemon name !!!\n")
