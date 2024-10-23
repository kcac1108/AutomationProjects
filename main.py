#import subprocess
# Executa o script name.py
#subprocess.run(["python3", "name.py"])
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pytz


def get_driver():

  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable_automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def save_to_file(data):
  """Save data to a file with the format year-day-month.hora-minuto-segundo"""
  timezone = pytz.timezone("America/Sao_Paulo")  # Defina o fuso horário correto
  current_time = datetime.now(timezone)
  # Format: year-day-month.hora-minuto-segundo
  filename = current_time.strftime("%Y-%d-%m.%H-%M-%S") + ".txt"

  with open(filename, "w") as file:
      file.write(f"Temperature: {data}\n")
  print(f"Saved to {filename}")


def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(1)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2)
  print(driver.current_url)

  while True:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return_value = clean_text(element.text)
    print(return_value)
    save_to_file(return_value)

  
  driver.quit() 

main()  # Sem print