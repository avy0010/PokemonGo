import os
import json

# Get the current directory where the script is executed
current_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_directory, "pokemon_icons")
output_json = os.path.join(current_directory, "pokedex.json")

# Initialize dictionary to store Pokédex data
pokedex_data = {}

# Read all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):  # Ensure it's an image file
        # Extract Pokédex number and Pokémon name (assuming format: "0001_Bulbasaur.png")
        parts = filename.replace(".png", "").split("_", 1)
        if len(parts) == 2:
            pokedex_number, pokemon_name = parts
            pokedex_data[pokedex_number] = pokemon_name

# Save data to JSON file in the current directory
with open(output_json, "w", encoding="utf-8") as json_file:
    json.dump(pokedex_data, json_file, indent=4, ensure_ascii=False)

print(f"✅ Saved {len(pokedex_data)} Pokémon to {output_json}")

