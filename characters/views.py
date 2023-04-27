from django.http import JsonResponse

from .models import PlayerCharacter
from .serializers import PlayerCharacterSerializer

def getAllPlayer(request):
    players = PlayerCharacter.objects.all()

    ser = PlayerCharacterSerializer(players, many=True)

    return JsonResponse(ser.data,  safe=False)


def getPlayer(request, id):
    actualCharacter = PlayerCharacter.objects.get(id=id)

    serializedCharacter = PlayerCharacterSerializer(actualCharacter, many=False)
    
    return JsonResponse(serializedCharacter.data)

