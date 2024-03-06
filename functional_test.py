from selenium import webdriver

# specify the path to your geckodriver
geckodriver_path = "/usr/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

browser = webdriver.Firefox(service=driver_service)
# browser = webdriver.Firefox() # Originial Example
browser.get("http://localhost:8000")

assert 'The install worked' in browser.title

