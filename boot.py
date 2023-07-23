import network
import usocket

from main import get_paras, web_page, router
from wifiConnect import connect_to_wifi

socket = connect_to_wifi()

while True:
    # wait for client
    client, addr = socket.accept()
    print('Client connected from', addr[0])
    request = client.recv(1024)
    print("request received")
    # extractt_paras(request_text)    
    #url parameters
    request_text = request.decode('utf-8')
    print("request text",request_text)
    paras = get_paras(request_text)
    print("paras",paras)
    response = router(paras)
    print("response",response)
    client.send(response)
    client.close()

