import sys
import network
import usocket
from consrant import ssid, password, port, conns


def get_wifi_error():
   return {
       network.STAT_WRONG_PASSWORD: 'wrong password',
       network.STAT_NO_AP_FOUND: 'wifi AP not found',
       -1: 'due to other problems',
   }


def connect_to_wifi():
   # connect to Wi-Fi
   
   print('Connecting to WiFi...')
   wifi = network.WLAN(network.STA_IF)
   wifi.active(True)
   wifi.connect(ssid, password)
   while wifi.status() == network.STAT_CONNECTING:
       pass

   if wifi.status() != network.STAT_GOT_IP:
       print('Failed to connect:', get_wifi_error().get(wifi.status(), get_wifi_error()[-1]))
       sys.exit()

   print('Connected.')
   s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
   print("Binding to port",port)
   s.bind(('', port))
   s.listen(conns)
   print("listning to conns",conns)
   print('Web server started on', 'http://{}:{}'.format(wifi.ifconfig()[0], port))
   return s
