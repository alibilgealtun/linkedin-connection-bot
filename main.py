from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/login')

# Enter your LinkedIn credentials
username = "username"
password = "password"

username_field = driver.find_element("id", "username")
password_field = driver.find_element("id", "password")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

# Navigate to the page
driver.get('https://www.linkedin.com/mynetwork/')

for i in range(0, 200): # Weekly invitation limit
    try:
        print(f"Attempt {i + 1}")
        connect_button = driver.find_element(By.XPATH,
                                             "//button//span[@class='artdeco-button__text'][normalize-space()='Connect']")
        connect_button.click()
        print("Connect  button clicked successfully")

        send_button = driver.find_element(By.XPATH, "//span[normalize-space()='Send']")
        send_button.click()
        print("Send  button clicked successfully")

    except Exception as e:
        print(f"Error: {e}")

# Close the browser window when done
driver.quit()
