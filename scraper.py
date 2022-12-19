from selenium import webdriver
from selenium.webdriver.chrome.options import Options

nse_url ='https://www.nseindia.com/market-data/live-equity-market'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage--')
  chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
  driver = webdriver.Chrome(options=chrome_options)
  return driver


if __name__ == "__main__":
  print('Creating driver..')
  driver = get_driver()
  
  print('Reading NSE page..')
  driver.get(nse_url)

  print(driver.title)