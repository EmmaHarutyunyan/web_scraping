from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:/Selenium/chromedriver.exe" 
driver = webdriver.Chrome()

url = "http://books.toscrape.com/"
driver.get(url)
time.sleep(2) 
books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")

with open("books.txt", "w", encoding="utf-8") as file:
    for i, book in enumerate(books[:10], start=1):
        full_title = book.get_attribute("title") 
        file.write(f"{i}. {full_title}\n")
        print(f"{i}. {full_title}")

driver.quit()
print("Done! First 10 book titles saved in books.txt")
