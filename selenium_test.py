from selenium import webdriver
import openpyxl

url = "https://www.gpw.pl"

driver = webdriver.Chrome()
driver.get(url)
page_source = driver.page_source
print(page_source)
driver.close()

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = page_source


workbook.save("content_of_the_website.xlsx")




