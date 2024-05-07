# For more details and step by step guide visit: Microcontrollerslab.com
import gastracker
import time
import gc
from machine import Pin,I2C
import ssd1306
import network
import framebuf
import lcdfont as lcdf

led_state = "OFF"
def web_page():
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }
    </style>
</head>

<body>
    <h2>ESP MicroPython Web Server</h2>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"?led_2_on\"><button class="button">LED ON</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"?led_2_off\"><button class="button button1">LED OFF</button></a>
    </p>
</body>

</html>"""
    return html


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)

# while True:
#     try:
#         if gc.mem_free() < 102000:
#             gc.collect()
#         conn, addr = s.accept()
#         conn.settimeout(3.0)
#         print('Received HTTP GET connection request from %s' % str(addr))
#         request = conn.recv(1024)
#         conn.settimeout(None)
#         request = str(request)
#         print('GET Rquest Content = %s' % request)
#         led_on = request.find('/?led_2_on')
#         led_off = request.find('/?led_2_off')
#         if led_on == 6:
#             print('LED ON -> GPIO2')
#             led_state = "ON"
#             led.on()
#         if led_off == 6:
#             print('LED OFF -> GPIO2')
#             led_state = "OFF"
#             led.off()
#         response = web_page()
#         conn.send('HTTP/1.1 200 OK\n')
#         conn.send('Content-Type: text/html\n')
#         conn.send('Connection: close\n\n')
#         conn.sendall(response)
#         conn.close()
#     except OSError as e:
#         conn.close()
#         print('Connection closed')
time.sleep(2)
station = network.WLAN(network.STA_IF)
i2c = I2C(scl=Pin(12), sda=Pin(13), freq=100000)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

led.on()
lcd.text("Gas",0,0)
lcd.text("Gwei",100,0)
lcd.text(station.ifconfig()[0],0,54)
lcd.show()

while True:
    try:
        #led.off()
        if gc.mem_free() < 10000:
            gc.collect()
        gas = int(gastracker.get_gwei())
        print('Gwei:',gas)
        lcd.fill_rect(0,10,128,44,0)
        lcd.show()
        time.sleep(0.5)
        if gas > 100:
            buffer = bytearray(bytes(lcdf.font(int(gas/100))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 16, 10)
            buffer = bytearray(bytes(lcdf.font(int(gas/10%10))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 16+32, 10)
            buffer = bytearray(bytes(lcdf.font(int(gas%10))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 16+64, 10)
        elif gas > 10:
            buffer = bytearray(bytes(lcdf.font(int(gas/10))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 32, 10)
            buffer = bytearray(bytes(lcdf.font(int(gas%10))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 64, 10)
        else:
            buffer = bytearray(bytes(lcdf.font(int(gas))))
            fb = framebuf.FrameBuffer(buffer, 32, 40, framebuf.MVLSB)
            lcd.blit(fb, 48, 10)

        lcd.show()
        #led.on()
    except:
        pass
    print("MEM", gc.mem_free())
    time.sleep(10)





