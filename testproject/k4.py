from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)

test_data_ascii = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

ascii_table = driver.find_element_by_xpath("/html/body/div/div/p[3]")
ascii_list = list(test_data_ascii)
text_chr = driver.find_element_by_id("chr")
text_op = driver.find_element_by_id("op")
text_num = driver.find_element_by_id("num")
button_submit = driver.find_element_by_id("submit")
text_result = driver.find_element_by_id("result")


# * Helyesen betöltődik az applikáció:
#    * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#      * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
def test_ascii():
    assert ascii_table.text == test_data_ascii


# * Megjelenik egy érvényes művelet:
#    * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#    * `op` mező vagy + vagy - karaktert tartlamaz
#    * `num` mező egy egész számot tartalamaz
def test_valid_operation():
    assert text_chr.text in ascii_list
    assert text_op.text is '+' or text_op.text is '-'
    assert text_num.text.isnumeric()


# * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#    * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#    * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#    * A `num` mezőben megjelenő mennyiségű karaktert
#    * az `result` mező helyes karaktert fog mutatni
def test_calculation():
    button_submit.click()
    result = ''
    if text_op.text is '+':
        result = ascii_list[ascii_list.index(text_chr.text) + int(text_num.text)]

    if text_op.text is '-':
        result = ascii_list[ascii_list.index(text_chr.text) - int(text_num.text)]

    assert result == text_result.text
