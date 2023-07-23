# webpage template
from consrant import right_lamp_state
from pinSetup import right_lamp


def get_http():
   return """
<!DOCTYPE html>
<html>
   <head>
       <title>ESP8266 Web Server</title>
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <link rel="icon" href="data:," />
       <style>
           body {
           background-color: Moccasin;
           }
           h1 {
           color: SaddleBrown;
           }
           h2 {
           color: Olive;
           }
       </style>
   </head>
   <body>
       <center>
           <h1>ESP8266 Web Server</h1>
           <h2>LED status: <!--led_status--></h2>
           <form methon="GET" action="">
               <p><input id="led_on" type="submit" name="led" value="On" /></p>
               <p><input id="led_off" type="submit" name="led" value="Off" /></p>
           </form>
       </center>
   </body>
</html>
"""


def get_get_http():
   # add HTTP response headers
   return 'HTTP/1.1 200 OK\r\n' + \
          'Content-Type: application/json\r\n' + \
          'Connection: close\r\n\r\n'


def web_page():
   led_status = 'ON' if right_lamp.value() == 0 else 'OFF'
   html = get_get_http() + ''.join([line.strip() for line in get_http().split('\n')])
   return html.replace('<!--led_status-->', led_status)


# extract url parameters from HTTP request
def get_paras(get_str: str):
   para_dict = {}
   q_pos = get_str.find('/?')
   if q_pos > 0:
       http_pos = get_str.find('HTTP/')
       para_list = get_str[q_pos + 2: http_pos - 1].split('//')
       print("para_list",para_list)
       for para in para_list:
           para_tmp = para.split('=')
           print("para_tmp",para_tmp)
           para_dict.update({para_tmp[0]: para_tmp[1] if len(para_tmp)> 1 else ""})
   return para_dict


def router(paras: dict):
   if "right_lamp" in paras:
       return  get_get_http() + ''.join([line.strip() for line in toggle_right_lamp(paras.get("right_lamp", None)).split('\n')])
   elif "get_state" in paras:
       return get_get_http() + ''.join([line.strip() for line in get_state().split('\n')])
   return get_get_http() + "{}"


def toggle_right_lamp(state):
   if state == "true":
       right_lamp.value(1)
       right_lamp_state = "true"
   else:
       right_lamp.value(0)
       right_lamp_state = "false"
   return """{
       right_lamp: """ + right_lamp_state + """
   }"""


def get_state():
   return """{
       right_lamp: """ + right_lamp_state + """
   }"""


