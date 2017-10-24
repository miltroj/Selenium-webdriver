import time
from selenium import webdriver
from test_class import TestToDo

tableElements = ['Pierwszy' , 'Drugi', "Trzeci", "Czwarty", "Piąty"]
driver_1 = webdriver.Chrome("C:\Programy\Selenium\Chrome\chromedriver.exe")
# driver_2 = webdriver.Firefox("C:\Programy\Selenium\Firefox\geckodriver.exe")

def slowDownProcess():
    time.sleep(2)

def runTestOnDrive(drive):
    klasa = TestToDo(drive)
    klasa.inicializeWeb()

    for element in tableElements:
        klasa.add_element(element)

    slowDownProcess()

    for element in tableElements:
        klasa.findElement(element)

    slowDownProcess()

    klasa.clearList()

    slowDownProcess()

    klasa.quitProcess()

if __name__ == "__main__":

    runTestOnDrive( driver_1 )
