import requests
import logging

# Setting up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

APP_URL = 'http://localhost:your-port'
EXPECTED_STATUS = 200

def check_app_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == EXPECTED_STATUS:
            logging.info(f'Application is running: {response.status_code}')
        else:
            logging.warning(f'Application might be down: {response.status_code}')
    except requests.RequestException as error:
        logging.error(f'Error checking application health: {error}')

def main():
    check_app_health()

if __name__ == '__main__':
    main()
