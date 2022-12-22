from selenium import webdriver
import time

# Replace YOUR_USERNAME and YOUR_PASSWORD with the actual username and password
USERNAME = "apollotestuserg317@biberk.com"
PASSWORD = "ApolloTest12"

# Open the web browser
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://biberk-apollo-qa.azurewebsites.net/")

# Find the username and password input fields
username_field = driver.find_element_by_id("Username")
password_field = driver.find_element_by_id("Password")

# Enter the username and password
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Find the login button and click it
login_button = driver.find_element_by_css_selector(".btn.btn-primary.btn-block")
login_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# You are now logged in!
time.sleep(60)

