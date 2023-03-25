import requests
import json
import re

url = "https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1"

response = requests.get(url)
html_content = response.text

interpelacje = re.findall(r'<a href="/sejm9.nsf/interpelacja.xsp\?documentId=.*?"\s*?id="[^"]*">(.*?)</a></td><td><nobr>(.*?)</nobr></td><td>(.*?)</td>', html_content)
print(len(interpelacje))
output = []

for interpelacja in interpelacje:
    output.append({"tytul": interpelacja[0], "data": interpelacja[1], "autor": interpelacja[2]})

with open('interpelacje.json', 'w') as outfile:
    json.dump(output, outfile)

print("Zapisano interpelacje do pliku interpelacje.json")