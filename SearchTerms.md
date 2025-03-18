# Pokémon GO Search Terms
## Table of Contents
- [Basic Search Terms](#basic-search-terms)
- [Type & Move-Based Search Terms](#type--move-based-search-terms)
- [IV & Buddy Search Terms](#iv--buddy-search-terms)
- [Pokémon Age & Event-Based Search Terms](#pokémon-age--event-based-search-terms)
- [Region-Based Search Terms](#region-based-search-terms)
- [Combining & Excluding Search Terms](#combining--excluding-search-terms)


## Basic Search Terms [🔼](#table-of-contents)

| Search Term | Description |
|------------|-------------|
| ```Pikachu``` | All Pokémon of that species |
| ```+Pikachu``` | All Pokémon in that family (Bulbasaur, Ivysaur, Venusaur) |
| ```"Nickname"``` | All Pokémon with that nickname |
| ```1``` | Pokédex #1 |
| ```1-25``` | Pokédex #1 to 25 |
| ```1-``` | Pokédex #1 and above |
| ```-25``` | Pokédex #25 and below |
| ```cp2000``` | All Pokémon with 2000 CP |
| ```cp2000-3000``` | All Pokémon between 2000 and 3000 CP |
| ```cp2000-``` | All Pokémon with 2000 CP and higher |
| ```cp-2000``` | All Pokémon with 2000 CP and lower |
| ```hp200-300``` | All Pokémon with 200 to 300 HP |
| ```Distance10-100``` | All Pokémon caught 10-100 KM away from your current location |
| ```Distance100-``` | All Pokémon caught 100 KM away from your current location |

## Type & Move-Based Search Terms [🔼](#table-of-contents)

| Search Term | Description |
|------------|-------------|
| ```Water``` | All Water-type Pokémon |
| ```@Water``` | All Pokémon with a Water-type move |
| ```@Bite``` | All Pokémon with the move Bite |
| ```@1Water``` | All Pokémon with a Water-type fast attack |
| ```@2Water``` | All Pokémon with a Water-type charged attack |
| ```@3Water``` | All Pokémon with a 2nd Water-type charged attack |
| ```@Move``` | All Pokémon that can learn a 2nd charge move |
| ```!@Move``` | All Pokémon that have learned a 2nd charge move |
| ```@Special``` | All Pokémon with exclusive moves (Legacy, CD) |
| ```@Weather``` | All Pokémon boosted by the weather |
| ```@1Weather``` | All Pokémon with a weather-boosted fast attack |
| ```@2Weather``` | All Pokémon with a weather-boosted charge attack |
| ```@3Weather``` | All Pokémon with a weather-boosted 2nd charge attack |

## IV & Buddy Search Terms [🔼](#table-of-contents)

| Search Term | Description |
|------------|-------------|
| ```0*``` | IVs between 0-49% |
| ```1*``` | IVs between 50-65% |
| ```2*``` | IVs between 66-80% |
| ```3*``` | IVs between 82-98% |
| ```4*``` | IV 100% |
| ```Buddy0``` | No Buddy history |
| ```Buddy1``` | Buddy history but no Good Buddy heart |
| ```Buddy2``` | All Good Buddies |
| ```Buddy3``` | All Great Buddies |
| ```Buddy4``` | All Ultra Buddies |
| ```Buddy5``` | All Best Buddies |

## Pokémon Age & Event-Based Search Terms [🔼](#table-of-contents)

| Search Term | Description |
|------------|-------------|
| ```Age +number``` | Pokémon caught within a certain time frame (e.g., ```Age0``` = last 24 hours, ```Age1``` = 24-48 hours) |
| ```Year +number``` | Pokémon caught in a specific year (e.g., ```2016``` = all Pokémon caught in 2016) |
| ```Costume``` | All 'Costumed' event Pokémon |
| ```Defender``` | Pokémon defending a gym |
| ```Traded``` | All Pokémon that have been traded |
| ```Legendary``` | All Legendary Pokémon |
| ```Mythical``` | All Mythical Pokémon |
| ```Shiny``` | All Shiny Pokémon |
| ```Lucky``` | All Lucky Pokémon |
| ```Shadow``` | All Shadow Pokémon |
| ```Purified``` | All Purified Pokémon |
| ```Hatched``` | All Pokémon hatched from eggs |
| ```Eggsonly``` | Egg-exclusive Pokémon (e.g., Baby Pokémon) |
| ```Evolve``` | All Pokémon that can evolve |
| ```Evolvenew``` | All Pokémon that can evolve and are a new Dex entry |
| ```Tradeevolve``` | Pokémon that evolve for free after being traded |
| ```Item``` | Pokémon that require a special item to evolve |
| ```Female/Male``` | Pokémon of that gender |
| ```Genderunknown``` | Genderless Pokémon |

## Region-Based Search Terms [🔼](#table-of-contents)

| Search Term | Description |
|------------|-------------|
| ```Kanto```, ```Johto```, ```Hoenn```, ```Sinnoh```, ```Unova```, ```Kalos```, ```Alola```, ```Galar``` | All Pokémon from that region/generation (```Kanto``` also includes Alola forms) |

## Combining & Excluding Search Terms [🔼](#table-of-contents)

- **Combine search terms:** Use ```&``` between search words  
  - **Example:**  
    ```plaintext
    Grass & CP2000-3000 & Kanto
    ```

- **Search for multiple terms:** Use ```,``` or ```:``` between multiple search terms (Both operators are same use any of them)
  - **Example using `,`:**  
    ```plaintext
    Water, Grass
    ```
  - **Example using `:`:**  
    ```plaintext
    Fire:Electric
    ```

- **Exclude Pokémon:** Use ```!``` before a term to filter it out  
  - **Example:** Show all Pokémon except traded ones  
    ```plaintext
    !traded
    ```
  - **Example:** Show all Pokémon **except** Legendary  
    ```plaintext
    !Legendary
    ```

- **Range searching:** Use ```-``` before, in between, or after a search term/number  
  - **Example:** Search for Pokémon with CP between **2000 and 3000**  
    ```plaintext
    CP2000-3000
    ```
  - **Example:** Search for Pokémon with **HP below 100**  
    ```plaintext
    hp-100
    ```
  - **Example:** Search for Pokémon with **Pokédex number 25 or below**  
    ```plaintext
    -25
    ```

- **Combine everything:**  
  - **Example:** Show all **Legendary & Lucky Pokémon**, those that are **Shiny**, and those that have **CP between 3000-4000**  
    ```plaintext
    Legendary & Lucky, Shiny, CP3000-4000
    ```
