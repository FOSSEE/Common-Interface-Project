from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import os

# Loading the .env file
load_dotenv()

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', '')
GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD', '')

# Set up the WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

def login_with_github():
    driver.get('http://localhost/#/login')  # Replace with your actual login page URL

    try:
        print("Waiting for the GitHub login button to be clickable...")
        github_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div/button[2]/span[1]'))
        )
        print("GitHub login button is clickable now.")
        github_button.click()
        print("Clicked the GitHub login button.")

        print("Waiting for GitHub login page to load...")
        wait.until(
            EC.presence_of_element_located((By.ID, 'login_field'))
        )
        print("GitHub login page loaded.")

        username_field = driver.find_element(By.ID, 'login_field')
        username_field.send_keys(GITHUB_USERNAME)

        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(GITHUB_PASSWORD)

        sign_in_button = driver.find_element(By.NAME, 'commit')
        sign_in_button.click()
        print("Submitted GitHub login form.")

        # Wait for the 2FA page
        try:
            print("Waiting for the 2FA page...")
            wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="otp"]'))
            )
            print("2FA page loaded. Please complete the 2FA process manually.")

            # Pause the script until the user completes the 2FA process
            input("Complete the 2FA process and press Enter to continue...")

            # Verification process should be completed by now
            print("2FA process completed.")

        except Exception as e:
            print("No 2FA page detected or an error occurred:", e)

        print("Waiting for authorization page to load...")
        authorize_button = wait.until(
            EC.element_to_be_clickable((By.NAME, 'authorize'))
        )
        authorize_button.click()
        print("Clicked authorize button.")

    except Exception as e:
        print(f"An error occurred during GitHub login: {e}")

def wait_for_gallery_load():
    try:
        # Wait until the `window.loadGalleryComplete` flag is set to true
        wait.until(lambda driver: driver.execute_script('return window.loadGalleryComplete === true;'))
        print("Gallery has fully loaded.")
    except Exception as e:
        print(f"Error waiting for gallery load: {e}")

def main():
    login_with_github()
    # After logging in, navigate to the gallery page
    driver.get("http://localhost/#/gallery")

    try:
        # Wait until the gallery page is loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[target='_blank'][href*='/editor?id=']")))

        # Find all "Launch in Editor" buttons
        buttons = driver.find_elements(By.CSS_SELECTOR, "a[target='_blank'][href*='/editor?id=']")

        # Click each "Launch in Editor" button and save
        for button in buttons:
            button.click()
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the newly opened editor tab/window

            # Wait for the page to load and the Save button to be clickable
            save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/div[2]/button[3]')))

            # Wait for the gallery to fully load
            wait_for_gallery_load()

            # Click the "Save" button
            ActionChains(driver).move_to_element(save_button).click().perform()

            # Optionally, you can verify the snackbar message if needed
            snackbar_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiSnackbar-root")))
            print(snackbar_message.text)

            # Verify the share button is displayed
            share_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/header/div[1]/button[2]')))
            print("Share button is displayed, diagram has been saved.")

            # Verify the "last saved" text is displayed
            last_saved_text = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/header/div[1]/p')))
            print("Last saved text:", last_saved_text.text)

            # Close the editor tab/window and switch back to the gallery
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        # Keep the browser window open
        print("All 'Launch in Editor' buttons have been clicked and saved. The browser will remain open.")

    finally:
        # Keep the browser open until manually closed
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == "__main__":
    main()
