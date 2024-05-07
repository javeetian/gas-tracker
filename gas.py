import usocket

def http_get(url):
    print("Fetching:", url)
    try:
        proto, _, host, path = url.split("/", 3)
    except ValueError:
        proto, _, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443

    addr = usocket.getaddrinfo(host, port)[0][-1]
    s = usocket.socket()
    s.connect(addr)
    if proto == "https:":
        s = ussl.wrap_socket(s, server_hostname=host)
    s.write(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.read(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
    
chaper_url = 'https://etherscan.io/gastracker'
#chaper_url = 'https://www.baidu.com'
http_get(chaper_url)
