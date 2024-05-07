import urequests2 as requests2

def get_gwei():
    chaper_url = 'https://www.oklink.com/zh-hans/eth/gas-price'
    chaper_el = '<span class=\"color-yellow-600 index_gasPrice__584Ji\">'
    chaper_el_end = ' Gwei</span>'
    # chaper_url = 'https://www.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    #res = requests2.get(url=chaper_url, headers=headers).text
    #res = requests2.get("https://www.baidu.com", headers=headers)
    res = requests2.get(url=chaper_url, headers=headers)
    data = res.receive(256)
    gas_prev = str(data, 'utf8')
    gas_price = None
    while True:
        data = res.receive(256)
        if data:
            gas_next = str(data, 'utf8')
            print(gas_next)
            gas = gas_prev + gas_next
            g_begin = gas.find(chaper_el) + len(chaper_el)
            g_end = gas.find(chaper_el_end)
            if g_begin > len(chaper_el) and g_end > g_begin:
                gas_price = gas[g_begin:g_end]
                print(gas, end='\r\n')
                print('gas_price: ',gas_price)
                res.close()
                return gas_price
            else:
                gas_prev = gas_next
        else:
            break
    res.close()
    return gas_price






