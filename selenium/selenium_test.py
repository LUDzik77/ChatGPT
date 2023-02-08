from selenium import webdriver
import openpyxl

url = "https://www.gpw.pl"

driver = webdriver.Chrome()
driver.get(url)

query = driver.find_element("xpath", "//div[@class='table gpw_style margin-bottom-0']")
query_text= query.text
print(query_text)
driver.close()

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = query_text

workbook.save("content_of_the_website.xlsx")




#whole http
#query_text = driver.page_source

# name+assetprice+percchange+capitalisation
#query = driver.find_element("xpath", "//div[@class='table gpw_style margin-bottom-0']")
#query_text= query.text