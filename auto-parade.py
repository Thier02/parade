import logging
import os

from playwright.sync_api import sync_playwright
from twilio.rest import Client

MY_SERVICE_URL = "https://services.rmc.ca/apex/f?p=RMCC_CMRC:101&p_lang=fr-ca"

# Set the environment variables
UNAME = os.environ['RMC_ID']  # Pas obligatoire, tu peux juste mettre ton username ici
PWD = os.environ['RMC_PASS']  # Pas obligatoire, tu peux juste mettre ton password ici
TWILIO_AUTH_TOKEN = os.environ['TWILIO']

# Configure the logging module
logging.basicConfig(filename='auto-parade.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Also log to the console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)


def send_sms(message):
    """Utilise l'API de Twilio pour envoyer un SMS(facultatif, c'est juste pour être notifié)"""
    account_sid = 'TWILIO_SID'
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='ton-numero-twilio',
        to='ton-numero-de-cellulaire',
        body=message
    )

    logging.info(f"SMS sent successfully.")


# J'utilise Playwright pour automatiser le processus
def run():
    logging.info(f"Starting the script.")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Access the page
        page = context.new_page()
        page.goto("https://services.rmc.ca/apex/f?p=RMCC_CMRC:101&p_lang=fr-ca")

        # Login
        page.fill("#P101_USERNAME", UNAME)
        page.fill("#P101_PASSWORD", PWD)
        page.click("//button[text()='Connexion']")

        logging.info(f"Logged in successfully.")

        # Wait for the page to be loaded
        page.wait_for_load_state("networkidle")

        # Navigate to Parade State
        page.goto("https://services.rmc.ca/php_apps/forms/index.php/en/cadet/update_status")

        # Select the desired option (Present, MIR, etc.)
        page.locator("#statusSelector").select_option("Present")

        page.click("#statusEvenBtn")  # Save the changes

        # Wait for 2 seconds so that the page can send the update to the server
        page.wait_for_timeout(2000)

        logging.info(f"Parade State updated successfully.")

        # Send the SMS ( Uncomment si tu as un compte Twilio )
        # time_now = time.strftime("%I:%M %p")
        # send_sms(f"[{time_now}] Le Parade State a été mis à jour avec succès !")

        # Close the browser
        context.close()
        browser.close()

if __name__ == "__main__":
    run()
