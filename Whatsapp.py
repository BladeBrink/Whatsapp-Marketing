from random import randint
from time import time
import selenium
import csv
from selenium import webdriver
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import null


driver = webdriver.Chrome('/Users/bladebrink/Library/Mobile Documents/com~apple~CloudDocs/SchoolofIT/Whatsapp/chromedriver')

with open ("HannahErrorFile.csv", "r", ) as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
                    if row[3].startswith("0") == True:
                        cellnum = row[3]
                        newcell = cellnum[1:]
                        print(newcell)
                        driver.get(f'https://web.whatsapp.com/send?phone=27{newcell}&text&app_absent=0')
                        print(f'https://web.whatsapp.com/send?phone=27{newcell}&text&app_absent=0')
                    else:
                        driver.get(f'https://web.whatsapp.com/send?phone=27{row[3]}&text&app_absent=0')
                        print(f'https://web.whatsapp.com/send?phone=27{row[3]}&text&app_absent=0')
                    print(row[3])
                    #print("No 0")
                    if count == 0:
                        time.sleep(20)
                        count = 1
                    try:
                        randomnumber = randint(1,2)
                        print(randomnumber)
                        if randomnumber == 1:
                            inputxpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                            #send = driver.find_element_by_xpath(inputxpath)
                            input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputxpath)))
                            name = row[2]
                            firstname = name.split(" ")
                            input_box.send_keys(f"Dear {firstname[0]}, I hope you are well. My name is Hannah & I work for Tyson Properties. I will be doing updated valuations in the area next week and I would love to add your property to the list. I look forward to hearing from you. Warm regards, Hannah de Villiers, Tyson Properties | Atlantic Seaboard ")
                            send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span') #change this to the enter button, stops it from clicking something else by mistake
                            send.click()
                            time.sleep(5)
                            
                        elif randomnumber == 2:
                            inputxpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                            #send = driver.find_element_by_xpath(inputxpath)
                            input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputxpath)))
                            name = row[2]
                            firstname = name.split(" ")
                            input_box.send_keys(f"Dear {firstname[0]}, It's Hannah here from Tyson Properties. I hope you're well. This is just a courtesy message to let you know I’ll be doing valuations in the area next week. Please let me know if you’d like an updated valuation. I look forward to hearing from you. Warm regards, Hannah de Villiers, Tyson Properties | Atlantic Seaboard ")
                            send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span') #change this to the enter button, stops it from clicking something else by mistake                         
                            send.click()
                            time.sleep(5)


                        # elif randomnumber == 3:
                        #     inputxpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
                        #     #send = driver.find_element_by_xpath(inputxpath)
                        #     input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inputxpath)))
                        #     name = row[2]
                        #     firstname = name.split(" ")
                        #     if row[11] != "":
                        #         input_box.send_keys(f"Dear {firstname[0]}, I trust you're well. I tried calling you earlier in the week to find out if we can assist you with an updated valuation report on your apartment in Son Vida. The requests have been for selling, as well as rental potential for the area. Please let me know if I’m able to assist in any way. My contact details are, Cell: 076 109 1815, Email: hannah.devilliers@tysonprop.co.za. Warm regards, Hannah de Villiers. Tyson Properties | Atlantic Seaboard")
                        #     else:
                        #         input_box.send_keys(f"Dear {firstname[0]}, I trust you're well. I tried calling you earlier in the week to find out if we can assist you with an updated valuation report on your apartment in Son Vida. The requests have been for selling, as well as rental potential for the area. Please let me know if I’m able to assist in any way. My contact details are, Cell: 076 109 1815, Email: hannah.devilliers@tysonprop.co.za. Warm regards, Hannah de Villiers. Tyson Properties | Atlantic Seaboard")
                        
                        #     send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span') #change this to the enter button, stops it from clicking something else by mistake
                        #     send.click()
                    except:
                        print("Fail")
                        with open ("HannahErrorFile2.csv", "a") as file:
                            writer = csv.writer(file)
                            writer.writerow(row)
                    time.sleep(3)
                    
                
                    
        
    

                

