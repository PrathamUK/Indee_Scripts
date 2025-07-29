# Name : Pratham U K
# Date : 29/07/2025
# USN : ENG22CS0123

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_video_automation():
    # URL and login PIN for the automation platform
    platform_url = "https://indeedemo-fyc.watch.indee.tv/"
    login_pin = "WVMVHWBS"
    
    # Path to ChromeDriver executable - update as per your system configuration
    chrome_driver_path = r"C:\Users\pratham u.k\Desktop\Indee_task\chromedriver.exe"

    # Setup Chrome WebDriver service
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    
    # Maximize the browser window for full visibility
    driver.maximize_window()

    # Configure dynamic wait: wait up to 60 seconds for elements and conditions
    wait = WebDriverWait(driver, 120)

    # Increase page load and script timeouts to handle slower responses
    driver.set_page_load_timeout(120)
    driver.set_script_timeout(120)

    try:
        # Open the login page of the platform
        driver.get(platform_url)
        print("Platform login page loaded successfully.")

        # Wait for the PIN input box to be visible and enter the PIN
        pin_input = wait.until(EC.visibility_of_element_located((By.NAME, "pin")))
        pin_input.send_keys(login_pin)
        pin_input.send_keys(Keys.RETURN)
        print("PIN submitted, logging in...")

        # Wait for the 'All Titles' button and click it to view titles
        all_titles_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Titles')]")))
        all_titles_button.click()
        print("Navigated to 'All Titles' section.")

        # Locate and open the 'Test automation project'
        test_project_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Test automation project')]")))
        test_project_card.click()
        print("Opened 'Test automation project'.")

        # Start video playback by clicking the Play button
        play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']")))
        play_button.click()
        print("Video playback started.")
        # Let the video play for the required 10 seconds
        time.sleep(10)

        # Pause the video after playing
        pause_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Pause']")))
        pause_button.click()
        print("Video paused at 10 seconds.")

        # Resume the video using 'Continue Watching' button
        continue_watching_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Continue Watching')]")))
        continue_watching_button.click()
        print("Resumed video playback using 'Continue Watching'.")
        time.sleep(5)  # Brief playback to demonstrate resume

        # Pause the video again before exiting
        pause_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Pause']")))
        pause_button.click()
        print("Video paused again.")

        # Click the Back button to exit the project screen
        back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Back']")))
        back_button.click()
        print("Exited the project screen.")

        # Click the Logout button to sign out from the platform
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Logout')]")))
        logout_button.click()
        print("Logged out successfully.")

    except Exception as e:
        # Print any exception that occurs during the automation sequence
        print(f"Automation encountered an error: {e}")

    finally:
        # Short pause before closing browser to ensure all actions completed
        time.sleep(2)
        driver.quit()
        print("Browser session ended, script completed.")

if __name__ == "__main__":
    run_video_automation()
