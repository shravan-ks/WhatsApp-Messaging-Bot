from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Intialize Geck Chrome web browser
bot = webdriver.Chrome()

# Loading url to browser
bot.get('https://web.whatsapp.com/')

# Login / validate
def login():
  # if login is succesfull after scanning Qr code
  try:
    print('Login to Whats App \n')
    time.sleep(3)
    bot.find_element_by_xpath('//*[@id="app"]/div/div[@tabindex="-1"]')
    print('Login Succesfull')
    print('~' * 50)

  # if not logged in 
  except NoSuchElementException:
      print("You have not logged in !! \n")
      print("Please can QR Code !!")
      print('*' * 50)     
      time.sleep(3)
      login()  

# send message Args to = user who Recive of message (should exact of saved contact name), message = Actual message 
def send_message(to,message):
  # try to send message if every values is correct
  try:
    receiver = bot.find_element_by_xpath('//span[@title = "{}"]'.format(to))
    receiver.click()
    messageBox = bot.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div[2 and @contenteditable="true"]')
    messageBox.send_keys(message)
    messageBox.send_keys(Keys.RETURN)
    print('Message Successfully Sent !! \n' + '-' * 50 )

  # if sending message failed !
  except NoSuchElementException:
    print('Reciver not found in Contacts Or Path Problem \n' + '-' * 50 )

  return

# call login function
login()

# loop call through send_message Fucntion 
while True :
  send_message(
  to = input("Enter the reciver Name : "),
  message = input("Enter the message to be sent : ")
  )