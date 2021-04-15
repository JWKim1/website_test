from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

def join_mem(mem_infor):
    mem_form = driver.find_element_by_link_text("회원가입")
    mem_form.click()
    mem = ["id", "pass", "pass_confirm", "name", "nick", "hp2", "hp3"]
    num = 0
    for i in mem:
        mem_input = driver.find_element_by_name(i)
        mem_input.send_keys(mem_infor[num])
        time.sleep(1)
        num += 1
    mem_input.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//*[@id=\"button\"]/a[1]/img").click()
    try:
        alert = Alert(driver)
        print(alert.text)
        time.sleep(3)
        alert.accept()
    except:
        print('회원가입 정상작동')

def do_logout():
    try:
        mem_form = driver.find_element_by_link_text("로그아웃")
        mem_form.click()
        print("로그아웃 정상작동")
    except:
        print('로그인 상태가 아닙니다')

def do_login(id_1, ps_1):
    try:
        mem_form = driver.find_element_by_link_text("로그인")
        mem_form.click()
        time.sleep(2)
        log_input = driver.find_element_by_name("id")
        log_input.send_keys(id_1)
        time.sleep(1)
        log_input = driver.find_element_by_name("pass")
        log_input.send_keys(ps_1)
        time.sleep(1)
        log_input.send_keys(Keys.RETURN)
        try:
            alert = Alert(driver)
            print(alert.text)
            time.sleep(3)
            alert.accept()
        except:
            print('로그인 정상작동')
    except:
        print('이미 로그인 되어있습니다.')

def write_greet(title, content):
    driver.find_element_by_xpath("//*[@id=\"menu\"]/div[2]/a/img").click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@id=\"button\"]/a[2]/img").click()
        input_g = driver.find_element_by_name("subject")
        input_g.send_keys(title)
        time.sleep(3)
        input_g = driver.find_element_by_name("content")
        input_g.send_keys(content)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"write_button\"]/input").click()
        try:
            alert = Alert(driver)
            print(alert.text)
            time.sleep(3)
            alert.accept()
        except:
            print('가입인사 작성 정상작동')
            screenshot_name = "my_screenshot_name.png"
            driver.save_screenshot(screenshot_name)
    except:
        print("로그인 필요")


if __name__ == "__main__":
    mem_infor = ["qqqq", "1234", "1234", "홍길동", "nick", "0000", "0000"]
    false_infor_number = ["zzzz", "1234", "1234", "홍길동", "nick", "aaaa", "0000"]
    false_id = ["한글", "1234", "1234", "홍길동", "nick", "0000", "0000"]
    no_pass= ["한글이름", "", "1234", "홍길동", "nick", "0000", "0000"]
    id_1 = "aaaa"
    ps_1 = "1234"

    chromedriver_dir = r'C:\Users\M\PycharmProjects\softtesting\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver_dir)
    driver.get('http://localhost/index.php')
    time.sleep(2)

    #time.sleep(2)
    #join_mem(false_id)


    #do_login(id_1, ps_1)
    #time.sleep(3)
    #do_logout()
    #write_greet("","내용내용")



