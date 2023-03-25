#I am mocking functionality or maybe whole script from polish journalist:
#https://wyborcza.biz/biznes/7,177150,29579541,hej-joe-czyli-jak-chatgpt-zaoszczedzil-mi-14-tysiecy-zlotych.html?disableRedirects=true
#time_elapsed=3

#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
import json
import re
import os
#from collections import OrderedDict


def run():
    print("started")
    while True:
        user_input = input("Ile ostatnich interpelacji poselskich chcesz zobaczyć: ")
        if user_input.isdigit() and 1 <= int(user_input) <= 1200:
            return user_input
        else:
            user_input = input("wprowadz liczbę między 1 a 1200")
    

#def scrap_for_all_documentId(page_to_process=2):
    #subpage_number=0
    #documentIds = []
    #while subpage_number<page_to_process:
        #print(f"processing page nr: {subpage_number+1}")
        #subpage_number += 1
        #try:
            #url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view={subpage_number}"
            #response = requests.get(url)
            #html_content = response.text
            #documentIds += re.findall(r'documentId=([\w\d]+)', html_content)
        #except:
            #pass
    #return(documentIds)

def scrap_for_all_documentId(page_to_process=2):
    subpage_number=0
    documentIds = []
    while subpage_number<int(page_to_process):
        print(f"processing page nr: {subpage_number+1}")
        subpage_number += 1
        url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page={subpage_number}"
        url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page=100000"
        response = requests.get(url)
        html_content = response.text
        new_docs = re.findall(r'documentId=([\w\d]+)', html_content)
        if new_docs == []:
            return(documentIds)
        else:
            documentIds += new_docs
    return(documentIds)
    

def add_to_json_documentID(documentID):
    if os.path.isfile('/sejm_interpellations_documents.json') == None:
        with open('sejm_interpellations_documents.json', 'w') as outfile:
            outfile.write("{}")
    else:
        with open('sejm_interpellations_documents.json', 'r') as outfile:
            loaded_file = json.load(outfile)
            print(json.dumps(loaded_file, indent=2))
            

def read_documentID_from_json(documentID):
    pass



#https://www.sejm.gov.pl/sejm9.nsf/interpelacja.xsp?documentId=F1ACCA92B611D87EC1258918004D9B60

if __name__ == "__main__":
    print("start")
    #querry = run()
    #print(querry)
    number_of_pages = querry//30 +1
    #list_of_documentIDs = scrap_for_all_documentId(querry)
    
    #add_to_json_documentID("s")
    #add_to_json_documentID("x")
    
    