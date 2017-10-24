import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains

class TestToDo(object):

    @staticmethod
    def initStartTime():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __init__(self , driver):
        self.webdriver = driver
        self.elementsToAdd = []
        self.webAdress = 'http://localhost:9090/'
        self.delay = .5
        self.listName = 'todo'
        print("{} - initialized driver:{}".format(self.initStartTime(),self.webdriver))

    def inicializeWeb(self):
        self.webdriver.get(self.webAdress)
        assert True == self.webdriver.find_element_by_id('todoapp').is_displayed()
        print("{} - web opened".format(self.initStartTime()))

    def find_element_class_nameIe(self, elementName):
        return self.webdriver.find_element_by_class_name(elementName)

    def findElement(self,  specifiedElementTxt):
        zwracany=''
        list = self.webdriver.find_elements_by_class_name( self.listName )
        # print("%r" %list)
        for element in list:
            # print ("jeden   "  + element.text )
            if element.text == specifiedElementTxt:
                # print(element.text)
                zwracany = element
                break
        print("{} - Zaznaczono element .{}. added".format(self.initStartTime(), specifiedElementTxt))
        return zwracany.find_element_by_class_name('check').click()

    def moveToElement(self , line):
        ActionChains(self.webdriver).move_to_element( self.findElement( line)).perform()
        self.find_element_class_nameIe('check').click()

    def add_element(self , elementName):
        self.webdriver.find_element_by_id('new-todo').send_keys(elementName)
        time.sleep(.5)
        assert True == self.webdriver.find_element_by_class_name('ui-tooltip-top').is_displayed()
        print("{} - element .{}. added".format(self.initStartTime(),elementName))
        self.webdriver.find_element_by_id('new-todo').send_keys('\n')

    def clearList(self):
        self.find_element_class_nameIe('todo-clear').click()
        print("{} - list cleared".format(self.initStartTime()))

    def quitProcess(self):
        # time.sleep( self.delay )
        self.webdriver.close()
        self.webdriver.quit()
        print("{} - process ended".format(self.initStartTime()))

