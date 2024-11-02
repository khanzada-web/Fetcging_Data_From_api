from django.shortcuts import render
from django.http import HttpRequest
from Team.models import Team_Member
import requests

def Index(request):
    return render(request,"index.html")

def Team(request):
    Team_Data=Team_Member.objects.all()
    Data={
        "Team_Data":Team_Data
    }

    return render(request,"Team.html",Data)

def Collection(request):
        urls = [
            "https://api-mainnet.magiceden.dev/v2/ord/btc/tokens?collectionSymbol=ordinal-pizza-og&showAll=true&limit=100&sortBy=inscriptionNumberAsc",
            "https://api-mainnet.magiceden.dev/v2/ord/btc/tokens?collectionSymbol=ordinal-pizza-og&showAll=true&limit=100&offset=100&sortBy=inscriptionNumberAsc",
            "https://api-mainnet.magiceden.dev/v2/ord/btc/tokens?collectionSymbol=ordinal-pizza-og&showAll=true&limit=100&offset=200&sortBy=inscriptionNumberAsc",
            "https://api-mainnet.magiceden.dev/v2/ord/btc/tokens?collectionSymbol=ordinal-pizza-og&showAll=true&limit=100&offset=300&sortBy=inscriptionNumberAsc"
        ]

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer 4cba3122-0874-4276-a271-1bf2f432daf5"
        }
        Collection_Data = []
        for url in urls:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                Collection_Data.extend(response.json().get('tokens', []))
            else:
                print(f"Failed to fetch data from {url}, status code: {response.status_code}")
        Data = {
            'Collection_Data': Collection_Data
        }

       
        
        return render(request,"Collection.html",Data)

def Faq(request):
    return render(request,"Faq.html")



