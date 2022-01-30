import requests
from django.shortcuts import render


# Create your views here.


def index(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"

    pokemons = requests.get(url)
    pokemons = pokemons.json()['results']

    context = {"pokemons": pokemons}

    return render(
        request,
        'pokedex/index.html',
        context=context
    )


def details(request, poke_id):
    url = "https://pokeapi.co/api/v2/pokemon/"

    poke_id = poke_id
    poke_url = url + str(poke_id) + '/'

    poke_details = requests.get(poke_url).json()

    context = {"poke_id": poke_id, "poke_details": poke_details}

    return render(
        request,
        'pokedex/details.html',
        context=context
    )
