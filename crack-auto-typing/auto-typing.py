from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get('https://www.livechatinc.com/typing-speed-test/#/')

# ret = driver.execute_script('(function(){alert()})();')
hasTime = True
elem = driver.find_element_by_class_name('test-input')
while hasTime:
    timer = driver.find_element_by_class_name('timer')
    if int(timer.text) > 0:
        ret = driver.execute_script(open(r'./queryElements.js').read())
        print(ret)
        if len(ret) == 0:
            break

        for item in ret:
            elem.send_keys(item)
            elem.send_keys(" ")
    else:
        hasTime = False
