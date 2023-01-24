import time
from plyer import notification

if __name__== '__main__':
    while True:
        notification.notify(title = 'Alerta de descanso!', message = 'Estuviste mucho tiempo sentado; parate y despejate unos minutos.', timeout = 10)
        time.sleep(3600)

