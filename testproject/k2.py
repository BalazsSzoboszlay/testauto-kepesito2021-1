import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
text_random_color = driver.find_element_by_id("randomColor")
text_random_color_name = driver.find_element_by_id("randomColorName")
text_test_color = driver.find_element_by_id("testColor")
text_test_color_name = driver.find_element_by_id("testColorName")
text_result = driver.find_element_by_id("result")
button_start = driver.find_element_by_id("start")
button_stop = driver.find_element_by_id("stop")


# * Helyesen jelenik meg az applikáció betöltéskor:
#    * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#    <szín neve> [     ] == [     ]

def test_initial():
    assert text_random_color_name.text is not ""
    assert text_random_color.value_of_css_property('background-color') is not 'rgb(255,255,255)'
    assert text_test_color.text == '[     ]'


# * El lehet indítani a játékot a `start` gommbal.
# * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
def test_start_stop():
    init_text = text_test_color_name.text
    button_start.click()
    time.sleep(2)
    assert text_test_color_name.text != init_text
    init_text = text_test_color_name.text
    button_stop.click()
    assert text_test_color_name.text == init_text
