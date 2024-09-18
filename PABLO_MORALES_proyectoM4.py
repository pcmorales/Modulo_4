import requests  # Se importa el módulo para hacer solicitudes HTTP.
import json  # Se importa el módulo para trabajar con datos JSON.
import os  # Se importa el módulo para interactuar con el sistema operativo.

# Se crea la carpeta "pokedex" si no existe.
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")  # Se crea la carpeta "pokedex" para almacenar archivos JSON.

# Función para validar que la entrada sea solo letras.
def validarNombre(nombrePokemon):
    return nombrePokemon.isalpha()  # Se verifica si el nombre del Pokémon contiene solo letras.

# Función para obtener los datos del Pokémon.
def obtenerPokemon(nombrePokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombrePokemon.lower()}"  # Se construye la URL de la API con el nombre del Pokémon en minúsculas.
    
    response = requests.get(url)  # Se hace una solicitud GET a la API para obtener datos del Pokémon.
    
    if response.status_code == 200:  # Si la solicitud fue exitosa y el Pokémon existe.
        pokemonData = response.json()  # Se convierte la respuesta JSON en un diccionario.
        
        # Se extrae la información que queremos mostrar.
        nombre = pokemonData['name']  # Se obtiene el nombre del Pokémon.
        peso = pokemonData['weight']  # Se obtiene el peso del Pokémon.
        altura = pokemonData['height']  # Se obtiene la altura del Pokémon.
        imagenUrl = pokemonData['sprites']['front_default']  # Se obtiene la URL de la imagen del Pokémon.
        tipos = [tipo['type']['name'] for tipo in pokemonData['types']]  # Se obtiene la lista de tipos del Pokémon.
        
        # Se muetra la información.
        print(f"\nPokémon: {nombre.capitalize()}")  # Se muestra el nombre del Pokémon con la 1ra letra en mayúscula.
        print(f"Peso: {peso}")  # Se muestra el peso del Pokémon.
        print(f"Altura: {altura}")  # Se muestra la altura del Pokémon.
        print(f"Tipos: {', '.join(tipos)}")  # Se muestra los tipos del Pokémon.
        print(f"Imagen: {imagenUrl}")  # Se muestra la URL de la imagen del Pokémon.
        
        # Se guarda la información en un archivo JSON.
        datos = {
            'nombre': nombre,
            'peso': peso,
            'altura': altura,
            'tipos': tipos,
            'imagen': imagenUrl
        }
        
        with open(f"pokedex/{nombre}.json", "w") as archivo:  # Se abre un archivo para escribir los datos del Pokémon en formato JSON.
            json.dump(datos, archivo, indent=4)  # Se guardan los datos en el archivo JSON.
        print(f"\nDatos de {nombre.capitalize()} guardados en pokedex/{nombre}.json")  # Se confirma que los datos se han guardado.
    else:
        print("\nPokémon no encontrado. Verifica el nombre.")  # Se informa si el Pokémon no fue encontrado.

# Función principal.
def main():
    while True:  # Ciclo infinito para permitir múltiples intentos de entrada.
        nombrePokemon = input("Introduce el nombre de un Pokémon: ")  # Se solicita al usuario que ingrese el nombre de un Pokémon.
        
        # Se valida que solo se ingresen letras.
        if validarNombre(nombrePokemon):
            obtenerPokemon(nombrePokemon)  # Obtener y mostrar la información del Pokémon si la entrada es válida.
            break  # Salir del ciclo si se ingresa un nombre válido.
        else:
            print("Entrada inválida. Solo se permiten letras. Inténtalo de nuevo.")  # Informar si la entrada no es válida.

# Se ejecuta el programa.
main()  # Se llama a la función principal para iniciar el programa.