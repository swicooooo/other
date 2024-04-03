from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from time import sleep

browser=webdriver.Chrome()

def simulate():
    try:
        browser.get('https://www.baidu.com')
        input=browser.find_element(By.ID, 'kw')
        input.send_keys('python')
        input.send_keys(Keys.ENTER)
        
        sleep(5)

        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)

    finally:
        browser.close()


def behavior():
    try:
        browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        sleep(5)
        browser.switch_to.frame('iframeResult')

        source=browser.find_element(By.ID, 'draggable')
        target=browser.find_element(By.ID, 'droppable')

        action=ActionChains(browser)
        action.drag_and_drop(source, target)
        action.perform()
    finally:
        browser.close()

def js():
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    sleep(5)

def attr():
    # browser.implicitly_wait(10)
    url = 'https://spa2.scrape.center/'
    browser.get(url)
    sleep(5)
    input = browser.find_element(By.CLASS_NAME,'logo-title')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)

def wait():
    browser.get('https://www.taobao.com/')
    wait=WebDriverWait(browser, 10)
    input=wait.until(EC.presence_of_element_located((By.ID, 'q')))
    btn=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-search')))
    print(input, btn)

def backOrForword():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    browser.get('https://antispider1.scrape.center/')
    sleep(5)
    # browser.get('https://www.taobao.com/')
    # browser.get('https://www.python.org/')
    # browser.back()
    # sleep(1)
    # browser.forward()

def main():
    backOrForword()

if __name__=='__main__':
    main()