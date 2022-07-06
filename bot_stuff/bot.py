from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.implicitly_wait(5)



browser.get('https://www.facebook.com/')
sleep(5)

email_input=browser.find_element(By.ID, "email")
sleep(1)
email_input.send_keys("<enter email>")
sleep(1)
user_password=browser.find_element(By.ID, "pass")
sleep(1)
user_password.send_keys("<enter password>")
sleep(1)

login_button=browser.find_element(By.NAME, "login")
login_button.click()
sleep(5)

try:
    search_field=browser.find_element(By.CLASS_NAME,"oajrlxb2.f1sip0of.hidtqoto.e70eycc3.hzawbc8m.ijkhr0an.pvl4gcvk.sgqwj88q.b1f16np4.hdh3q7d8.dwo3fsh8.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.br7hx15l.h2jyy9rg.n3ddgdk9.owxd89k7.rq0escxv.oo9gr5id.mg4g778l.buofh1pr.g5gj957u.ihxqhq3m.jq4qci2q.hpfvmrgz.lzcic4wl.l9j0dhe7.iu8raji3.l60d2q6s.dflh9lhu.hwnh5xvq.scb9dxdr.qypqp5cg.aj8hi1zk.kd8v7px7.r4fl40cc.m07ooulj.mzan44vs")
    sleep(5)
    search_field.click()
    sleep(2)
    query='bars in NYC'
    search_field.send_keys(query)
    sleep(5)
    search_field.send_keys(Keys.RETURN)
    sleep(5)
    
    find_schools=browser.find_elements(By.CSS_SELECTOR,"a")
    schoolList=[]
    for item in find_schools:
        schoolList.append(item.get_attribute('href'))
    for item in schoolList:
        print(item)
except:
    print('Na, this did not work')
    

try:
    profile_icon_div_tag=browser.find_element(By.TAG_NAME,"image")
    sleep(1)
    profile_icon_div_tag.click()
    sleep(1)
    logout_button=browser.find_element(By.XPATH,"//span[text()='Log Out']")
    sleep(3)
    logout_button.click()
except:
    print('you messed up; try again')

sleep(20)
browser.close()

