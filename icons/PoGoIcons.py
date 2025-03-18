import os
import requests
from bs4 import BeautifulSoup
import re

#####################################
#  CREDITS -> https://pokemondb.net
#####################################


# Function to sanitize filenames
def sanitize_filename(name):
    name = re.sub(r'[^\w\s-]', '', name)  # Remove special characters
    name = name.replace(' ', '_')  # Replace spaces with underscores
    return name.strip()

def download_pokemon_icons():
    # URL of the National Pokédex list
    pokedex_url = "https://pokemondb.net/pokedex/national"
    response = requests.get(pokedex_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Create folder if it doesn't exist
    folder = "pokemon_icons"
    os.makedirs(folder, exist_ok=True)

    # Dictionary to store Pokémon name → Pokédex number mapping
    pokedex_dict = {}

    # Get all Pokémon info from the National Dex page
    for pokemon in soup.select(".infocard"):
        name = pokemon.select_one(".ent-name").text.strip()
        number = pokemon.select_one(".infocard-lg-data small").text.strip().replace("#", "").zfill(4)
        pokedex_dict[name] = number

    # URL of the Pokémon icon sprites page
    sprites_url = "https://pokemondb.net/sprites"
    response = requests.get(sprites_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all Pokémon icon images
    for img_tag in soup.select("img.icon-pkmn"):
        image_url = img_tag["src"]
        name = img_tag["alt"].strip()

        # Get the correct Pokédex number from the dictionary
        number = pokedex_dict.get(name, "0000")

        # Sanitize name for filename
        clean_name = sanitize_filename(name)
        image_path = os.path.join(folder, f"{number}_{clean_name}.png")

        # Download and save image
        img_data = requests.get(image_url).content
        with open(image_path, "wb") as f:
            f.write(img_data)

        print(f"✅ Downloaded: {number}_{clean_name}.png")

if __name__ == "__main__":
    download_pokemon_icons()
