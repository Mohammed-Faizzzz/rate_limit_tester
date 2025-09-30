from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_chatbot():
    
    # Replace with the URL of the chatbot web app (or use environment variable)
    URL = ""

    driver = webdriver.Chrome()
    driver.get(URL)
    wait = WebDriverWait(driver, 20) # wait 20s for the page to load

    # input box
    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Ask Anything...'])[last()]"))
    )

    # send "button"
    send_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Ask Anything...'])[last()]/following::img[1]"))
    )

    for i in range(121): # send 121 messages (adjust as necessary)
        msg = f"Test prompt #{i}"

        driver.execute_script("arguments[0].value = arguments[1];", input_box, msg) # set input box value via JS
        # driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", input_box) 

        send_icon.click()  # click the send button

        print(f"Sent: {msg}")
        time.sleep(20)  # wait for chatbot reply (adjust as necessary)
        

test_chatbot()
