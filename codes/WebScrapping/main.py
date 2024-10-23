#import subprocess
# Executa o script name.py
#subprocess.run(["python3", "name.py"])
import time
from selenium import webdriver


def get_driver():

  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable_automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  i = 1
  ok = True
  driver = get_driver()  # Movido para fora do loop para não reiniciar o driver a cada iteração
  while ok:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return_value = clean_text(element.text)
    print(return_value)
    if return_value == 20:
      ok = False
    i += 1
  driver.quit()  # Certifique-se de fechar o driver ao final

main()  # Sem print


  #driver = get_driver()
  #time.sleep(2)
  #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  #return clean_text(element.text)

#print(main())