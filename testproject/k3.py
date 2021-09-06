import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)

text_input = driver.find_element_by_id("title")
error_message = driver.find_element_by_xpath("/html/body/form/span")
text_error_message_illegal = "Only a-z and 0-9 characters allewed"
text_error_message_length = "Title should be at least 8 characters; you entered 4."

test_data = ["abcd1234", "teszt233@", "abcd"]


def fill_and_return_error(text):
    time.sleep(2)
    text_input.clear()
    text_input.send_keys(text)
    return error_message.text

#* Helyes kitöltés esete:
#    * title: abcd1234
#    * Nincs validációs hibazüzenet
def test_positive():
    assert fill_and_return_error(test_data[0]) == ""

#* Illegális karakterek esete:
#    * title: teszt233@
#    * Only a-z and 0-9 characters allewed.
def test_illegal():
    assert fill_and_return_error(test_data[1]) == text_error_message_illegal
#* Tul rövid bemenet esete:
#    * title: abcd
#    * Title should be at least 8 characters; you entered 4.

def test_short():
    assert fill_and_return_error(test_data[2]) == text_error_message_length
