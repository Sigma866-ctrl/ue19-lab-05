from turtledemo.clock import setup

import requests
import json


def get_joke():
    """
    Récupère et affiche une blague aléatoire de JokeAPI (v2.jokeapi.dev).
    """
    # Point de terminaison (endpoint) pour une blague aléatoire dans n'importe quelle catégorie.
    # Nous spécifions le français (lang=fr) et blacklistons les blagues potentiellement offensantes.
    API_URL = "https://official-joke-api.appspot.com/random_joke"

    print("Fetching a joke from the JokeAPI...")

    try:

        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()


        if data.get("error"):
            print("Erreur de l'API : Impossible de récupérer la blague.")
            # Afficher le message d'erreur si disponible
            if "message" in data:
                print(f"Message: {data['message']}")
            return

        joke_type = data.get("type")
        joke = data.get("setup")
        punchline = data.get("punchline")

        print(f"blague de registre {joke_type}")
        print(joke)
        guess = input("votre reponse : ")

        if guess == punchline:
            print("pfffff... azy t'es pas drôle")
        elif guess != punchline:
            print(punchline)

    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de connexion ou les erreurs HTTP
        print(f"\n Erreur lors de la requête API : {e}")
    except json.JSONDecodeError:
        # Gérer les erreurs si la réponse n'est pas un JSON valide
        print("\n Erreur de décodage JSON dans la réponse de l'API.")


if __name__ == "__main__":
    get_joke()
