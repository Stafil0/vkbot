import subprocess
import time
from app import config
from app import app_start as application

ngrok = config.get_param('exe', 'NGROK')
token = config.get_param('authtoken', 'NGROK')

if __name__ == '__main__':
    with subprocess.Popen([ngrok, 'authtoken', token]) as ngrok_auth:
        with subprocess.Popen([ngrok, 'http', config.port],
                              creationflags=subprocess.CREATE_NEW_CONSOLE) as ngrok_process:
            time.sleep(5)
            application.app.run(port=config.port)