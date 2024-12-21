import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# requirements to wait until specific part of page is open
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
def loginUser():
    # Open your browser, and point it to the login page
    someVariable = getpass.getpass("Press Enter after You are done logging in") #< THIS IS THE SECOND PART
    #Here is where you put the rest of the code you want to execute
options = Options()
#options.add_argument("--lang=en_US")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option("useAutomationExtension", False)
#options.add_argument("disable-infobars")
#windows profile directory
#options.add_argument('user-data-dir=C:/Users/sundar/AppData/Local/Google/Chrome/User Data')
#mac profile dir
options.add_argument('user-data-dir=/Users/sundara_rajan/Library/Application Support/Google/Chrome/')
options.add_argument('profile-directory=Profile 2')
#options.add_argument('--headless') 
options.add_argument('--no-sandbox')
options.add_argument( "--remote-debugging-pipe")
#options.binary_location ='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
#driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe', chrome_options=options)
try:
    with webdriver.Chrome() as browser:
        #browser.switchTo().newWindow(webdriver.WindowType.TAB);
        browser.implicitly_wait(10);
        wait = WebDriverWait(browser, 10)
        #browser = webdriver.Chrome(options) 
        browser.get("https://rewards.bing.com/?ref=rewardspanel")
        time.sleep(3)
        #loginUser()  
        loginelem = browser.find_element(by=By.NAME, value="loginfmt")
        loginelem.send_keys("y2kprabu@hotmail.com" )     
        #loginelem.send_keys("jeffkevinjk@outlook.com" )     
        browser.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)
        pwdelem = browser.find_element(by=By.NAME, value="passwd")
        pwdelem.send_keys("HOTY2KHONDA@" )   
        #pwdelem.send_keys("JEFFY2KPRO@@" )     
        #input()
        signinelem = browser.find_element(By.XPATH, value='//button[text()="Sign in"]')
        wait.until(EC.element_to_be_clickable(signinelem)).click()
        time.sleep(3)
        browser.find_element(By.ID, "acceptButton").click()
        time.sleep(3)

      
        # Setup wait for later
        browser.refresh()
        # Store the ID of the original window
        original_window = browser.current_window_handle

        # Check we don't have other windows open already
        assert len(browser.window_handles) == 1
        # this is where the page is not loading & therefore throwing ElementNotFound exception

    
        #assert "bing" in driver.title
        sourcedata = browser.page_source

        href_links = []
        href_links2 = []

        elems = browser.find_elements(by=By.XPATH, value="//a[contains(@href, 'https://www.bing.com/search')]")
        formElems= browser.find_elements(by=By.XPATH, value="//a[contains(@href, 'https://www.bing.com/?form')]")
        
        elems2 = browser.find_elements(by=By.TAG_NAME, value="a")
        formElemsArray = []
        for elem in formElems:
            formElemsArray.append(elem)
        #create a copy of it to avoid stale elements
        rewElems =[]

        for elem in elems:
            rewElems.append(elem)
        #Getting the searchable elements
        #print(sourcedata)
        try:
            for elem in rewElems:
                l = elem.get_attribute("href")
                if l not in href_links:
                    print(l)
                    try:
                        time.sleep(3)
                        wait.until(EC.element_to_be_clickable(elem)).click()
                        browser.switch_to.window(original_window)
                    except Exception as e:
                        print(f"Exception occured :{e}")
                        continue
                    href_links.append(l)
                    browser.switch_to.window(original_window)
        except Exception as e:
            print(f"Exception occured :{e}")
        #browser.back()
        browser.switch_to.window(original_window)
        input('The first set of links using click option are tried')
        #for elem in elems2:
        #    l = elem.get_attribute("href")
        #    if (l not in href_links2) & (l is not None):
        #        print(l)
        #        href_links2.append(l)

        try:
            for elem in formElems:
                l = elem.get_attribute("href")
                searchstring=elem.get_attribute("aria-label")
                newsearchUrl="https://www.bing.com/search?q="+searchstring
                if l not in href_links:
                    print(l)
                    try:
                        time.sleep(3)
                        #load the form
                        wait.until(EC.element_to_be_clickable(elem)).click()
                        time.sleep(3)
                        #after waiting search the control
                        searchbox = browser.find_element(by=By.TAG_NAME, value="textarea")
                        #wait.until(EC.element_to_be_clickable(searchbox)).click()
                        browser.execute_script("arguments[0].value = 'Your new value';", searchbox)

                        #searchbox.size.setdefault()
                        #searchbox.clear()
                        #searchbox.send_keys("searchstring")     
                       # searchbox.send_keys(searchstring)     
                        searchboxButton = browser.find_element(by=By.NAME, value="go")
                        wait.until(EC.element_to_be_clickable(searchboxButton)).click()
                        browser.switch_to.window(original_window)
                    except Exception as e:
                        print(f"Exception occured :{e}")
                        continue
                    href_links.append(l)
                    browser.switch_to.window(original_window)
        except Exception as e:
            print(f"Exception occured :{e}")
        #browser.back()
        print(len(href_links))  # 360
        for indivlink in href_links:
            time.sleep(3)
            browser.switch_to.new_window('tab')
            browser.get(indivlink)
            browser.switch_to.window(original_window)
            

        input('Press a Key to Close program')
        
except Exception as e:
    print(f"Exception occured : outerloop {e}")
finally:
    if(browser is not (None) ):
        browser.close()
        browser.quit()
    