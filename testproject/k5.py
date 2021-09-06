import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
bingo_body = driver.find_element_by_id("bingo-body")
numbers_list = driver.find_element_by_id("numbers-list")
button_play = driver.find_element_by_id("spin")
button_init = driver.find_element_by_id("init")
messages = driver.find_element_by_id("messages")


# A feladatod az alábbi tesztesetek lefejlesztése:
# * Az applikáció helyesen megjelenik:
#    * A bingo tábla 25 darab cellát tartalmaz
#    * A számlista 75 számot tartalmaz
def test_count():
    assert len(bingo_body.find_elements_by_name("number")) == 25
    assert len(numbers_list.find_elements_by_css_selector("li")) == 75


# * Bingo számok ellenőzrzése:
#    * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#    * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki

def test_validity():
    while len(messages.find_elements_by_css_selector("li")) == 0:
        time.sleep(0.3)
        button_play.click()

    assert True


# * Új játékot tudunk indítani
#    * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#    * új bingo szelvényt kapunk más számokkal.

def test_restart():
    counter_table = 0
    counter_numbers = 0

    button_init.click()
    for x in bingo_body.find_elements_by_name("number"):
        if x.get_attribute("selected"):
            counter_table += 1

    for x in numbers_list.find_elements_by_css_selector("li"):
        if x.get_attribute("selected"):
            counter_numbers += 1

    assert counter_table == 1
    assert counter_numbers == 0
