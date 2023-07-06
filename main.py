from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import threading

def abrir_ventana(proxy):
    # WINDOW_SIZE = "300,400"
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--proxy-server=http://{}'.format(proxy['proxy']))
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.youtube.com/watch?v=8L5Onk6vX1c&t')
    # Encontrar el elemento por clase
    elemento = driver.find_element(By.CLASS_NAME, "ytp-play-button")
    # Hacer clic en el elemento
    elemento.click()
    time.sleep(3720)
    driver.close()

proxy_list = [
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
    {'proxy': 'gate.smartproxy.com:7000'},
]




threads = []
for proxy in proxy_list:
    thread = threading.Thread(target=abrir_ventana, args=(proxy,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
