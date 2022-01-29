from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder

# Create your views here.
def lobby(request):
    return render(request,'base/lobby.html')

def room(request):
    return render(request,'base/room.html')

def getToken(request):
    appId = "db0e302e89604e739383d9c959d9f5d0"
    appCertificate = "987a8ab2837c4b1b876768e8febcf637"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)