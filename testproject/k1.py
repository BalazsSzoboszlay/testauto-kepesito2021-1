from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
a_input = driver.find_element_by_id("a")
b_input = driver.find_element_by_id("b")
submit_button = driver.find_element_by_id("submit")
result_text = driver.find_element_by_id("result")

init_data = ["", "", False]
test_data_a = ["2", ""]
test_data_b = ["3", ""]
reference_data = ["10", "NaN"]


# * Helyesen jelenik meg az applikáció betöltéskor:
#    * a: <üres>
#    * b: <üres>
#    * c: <nem látszik>
def test_initial():
    assert init_data[0] == a_input.text
    assert init_data[1] == b_input.text
    assert result_text.is_displayed() is init_data[2]


def fill_input(a_data, b_data):
    a_input.clear()
    b_input.clear()
    a_input.send_keys(a_data)
    b_input.send_keys(b_data)
    submit_button.click()


# * Számítás helyes, megfelelő bemenettel
#    * a: 2
#    * b: 3
#    * c: 10
def test_positive():
    fill_input(test_data_a[0], test_data_b[0])
    assert result_text.text == reference_data[0]


# * Üres kitöltés:
#    * a: <üres>
#    * b: <üres>
#    * c: NaN
def test_empty():
    fill_input(test_data_a[1], test_data_b[1])
    assert result_text.text == reference_data[1]
