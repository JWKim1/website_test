from selenium import webdriver
import bs4
import time

chromedriver_dir = r'C:\Users\M\PycharmProjects\softtesting\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(3)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(3)

loca = driver.find_element_by_class_name('sido_arae_box') 
li = loca.find_elements_by_tag_name('li') 
li[0].click() 
time.sleep(3)

gugun = driver.find_element_by_class_name('gugun_arae_box')
guli = gugun.find_element_by_tag_name('li')
guli.click()
time.sleep(3)

source = driver.page_source
bs = bs4.BeautifulSoup(source, 'lxml')
entire = bs.find('ul', class_='quickSearchResultBoxSidoGugun')
li_list = entire.find_all('li')

for infor in li_list:
    print(infor.find('p').text)

