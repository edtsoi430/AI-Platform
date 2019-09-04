from Tkinter import *  #GUI
from selenium import webdriver #Firefox
from time import sleep 

usr = ""
pwd = ""

driver = webdriver.Chrome() 
driver.get('https://www.facebook.com/') 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
driver.quit() 
