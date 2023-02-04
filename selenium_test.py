from selenium import webdriver
import openpyxl

url = "https://www.gpw.pl"

driver = webdriver.Chrome()
driver.get(url)

div = driver.find_element("xpath", "//div[@class='table gpw_style margin-bottom-0']")
text = div.text
print(text)
driver.close()

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = text

workbook.save("content_of_the_website.xlsx")


#page_source = driver.page_source
##print(page_source)
#driver.close()

#workbook = openpyxl.Workbook()
#sheet = workbook.active
#sheet['A1'] = page_source




