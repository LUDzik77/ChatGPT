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

#url = "https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1"
#response = requests.get(url)
#html_content = response.text
#print(html_content)



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
        #url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page=100000"
        response = requests.get(url)
        html_content = response.text
        new_docs = re.findall(r'documentId=([\w\d]+)', html_content)
        if new_docs == []:
            return(documentIds)
        else:
            documentIds += new_docs
    return(documentIds)



def create_json_db():
    with open('sejm_interpellations_documents.json', 'a', encoding='utf-8') as outfile:
        subpage_number = 0
        result = {}
        while True:
            print(f"processing page nr: {subpage_number+1}")
            subpage_number += 1
            url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page={subpage_number}"            
            response = requests.get(url)
            html = response.text
            pattern = r'documentId=([\w\d]+)&amp;view=1">(.*?)<\/a><\/td><\/tr><tr><td><strong>(\d+)<\/strong>'
            matches = re.findall(pattern, html)
            if matches == [] or subpage_number == 10:
                result2 = json.dumps(result) 
                outfile.write(result2)
                #print(json.loads(result2))
                break
            for match in matches:
                doc_id = match[0]
                title = match[1]
                request_nr = match[2]
                result[request_nr] = {"tytuł": title, "documentId": doc_id}    

def update_json_db(pages_to_process=10):
    with open('sejm_interpellations_documents.json', 'r+', encoding='utf-8') as outfile:
        #subpage_number = 0
        ##result = {}
        #json_db = json.load(outfile)
        #json_db['40090'] = {'s':'x'} #WORKS FINE  CONTINUE HERE
        #outfile.seek(0)
        #json.dump(json_db, outfile)
        #outfile.truncate()
        
        
        while True:
            print(f"processing page nr: {subpage_number+1}")
            subpage_number += 1
            url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page={subpage_number}"            
            response = requests.get(url)
            html = response.text
            pattern = r'documentId=([\w\d]+)&amp;view=1">(.*?)<\/a><\/td><\/tr><tr><td><strong>(\d+)<\/strong>'
            matches = re.findall(pattern, html)
            if matches == [] or subpage_number > pages_to_process:
                break
            for match in matches:
                doc_id = match[0]
                title = match[1]
                request_nr = match[2]
                json_db[request_nr] = {"tytuł": title, "documentId": doc_id}
                outfile.seek(0)
                json.dump(json_db, outfile)
                outfile.truncate()                 
            
    
 
            #while True:
                #print(f"processing page nr: {subpage_number+1}")
                #subpage_number += 1
                #url = f"https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1&page={subpage_number}"            
                #response = requests.get(url)
                #html = response.text
                #pattern = r'documentId=([\w\d]+)&amp;view=1">(.*?)<\/a><\/td><\/tr><tr><td><strong>(\d+)<\/strong>'
                #matches = re.findall(pattern, html)
                #if matches == [] or subpage_number > pages_to_process:
                    #result2 = json.dumps(result) 
                    #outfile.write(result2)
                    ##print(json.loads(result2))
                    #break
                #for match in matches:
                    #doc_id = match[0]
                    #title = match[1]
                    #request_nr = match[2]
                    #result[request_nr] = {"tytuł": title, "documentId": doc_id}               
            
            
            
            
    #else:
        #with open('sejm_interpellations_documents.json', 'r') as outfile:
            #loaded_file = json.load(outfile)
            #print(json.dumps(loaded_file, indent=2))
            

def read_documentID_from_json(number_of_querries):
    pass



#https://www.sejm.gov.pl/sejm9.nsf/interpelacja.xsp?documentId=F1ACCA92B611D87EC1258918004D9B60

if __name__ == "__main__":
    print("Start...")
    if os.path.isfile('sejm_interpellations_documents.json') == False:
        print("Creating json db it might take a while...")
        create_json_db()
    querry = run()
    #print(querry)
    #number_of_pages = querry//30 +1
    #list_of_documentIDs = scrap_for_all_documentId(querry)
    
    #update_json:
    #documentID & number on the first page and update accordingly
    #get querry number
    #compare

    #add_to_json_documentID("s")
    #add_to_json_documentID("x")
    
    
    #creation of what for script to operate
    #update json_DB with every run
    #show_interpelation_by

    update_json_db(pages_to_process=10)
    
    with open('sejm_interpellations_documents.json', 'r') as outfile:
        print(outfile)
        print(json.loads(outfile.read()))  #THAT IS WORKING#
        
