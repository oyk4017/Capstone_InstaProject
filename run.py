from urllib.request import urlopen, Request  # Internet url open package
from bs4 import BeautifulSoup  # BS
from selenium import webdriver  # webdriver
import time  # Package for waiting time during crawling
import warnings  # Remove Warning message

# Web browser automation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# For Save Data
import pymysql

# For hashtag crawling
import re

# For Search human
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
import os

def ToEng(x): return {'석계역맛집': 'kw','광운대맛집': 'kw', '외대앞맛집': 'hufs', '외대맛집': 'hufs', '회기맛집': 'khu', '시립대맛집':'uos', '서울대입구맛집': 'snu', '홍익대맛집': 'hu', '연대맛집': 'yon', '이대맛집': 'ewha', '한양대맛집':'hy', '건국대맛집':'ku', '덕성여대맛집': 'dswu', '국민대맛집': 'kmu', '성신여대맛집': 'sswu', '한성대맛집':'hsu', '숙대맛집':'sook','고대맛집': 'kor','동덕여대맛집':'ddwu', '서울여대맛집':'swu',  '화랑대맛집':'swu', '서강대맛집':'sgu'}[x]  # File name Korean->English

def imread_hangul_path(path):
    with open(path, "rb") as fp:
        bytes = bytearray(fp.read())
        numpy_array = np.asarray(bytes, dtype=np.uint8)
    return cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)  # Imread if the file name is Korean

warnings.filterwarnings(action='ignore')  # Remove Warning message


# Create instagram url and open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome('/Users/yukyung/chromedriver',chrome_options=chrome_options)
driver.get("https://www.instagram.com")
assert "Instagram" in driver.title  #Exception handling

# Login
time.sleep(0.5)
driver.find_element_by_name('username').send_keys('oyk4017')#food_food_univ #foodincampus
time.sleep(0.5)
driver.find_element_by_name('password').send_keys('yukyung4017!')#!qwert4321! #food1234*
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

time.sleep(3)

# 쓰잘데기없는 화면 넘기기
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/div/div/button').click()#'/html/body/div[4]/div/div/div/div[3]/button[2]'
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

# Data
search_univ = ['화랑대맛집']#'건대맛집추천', '덕성여대맛집', '국민대맛집', '성신여대맛집', '한성대맛집', '숙대맛집', '고대맛집', '동덕여대맛집', '서울여대맛집', '서강대맛집']#'광운대맛집', '외대맛집', '경희대맛집', '시립대맛집', '서울대맛집', '홍대맛집', '연대맛집', '이대맛집', '한양대맛집', 
univ = ['서울여대']#, '덕성여대', '국민대', '성신여대', '한성대', '숙명여대', '고려대', '동덕여대', '서울여대', '서강대' ]#'광운대', '한국외대', '경희대', '서울시립대', '서울대', '홍익대', '연세대', '이화여대', '한양대',  
like = []
content = []
date = []
place = []
tags = []
cur_url = []
check = [[],[]] #중복 확인 

for x in search_univ:
    eng_univ = ToEng(x)

    # Search HashTag
    elem = driver.find_element_by_css_selector(".XTCLo.x3qfX")
    elem.send_keys(x)
    time.sleep(2)
    elem.send_keys(Keys.RETURN)
    elem.send_keys(Keys.RETURN)

    # Set url
    baseUrl = "https://www.instagram.com/explore/tags/"
    plusUrl = x
    url = baseUrl + plusUrl
    driver.get(url)
    time.sleep(3)

    # Scroll Section and Save image to local
    body = driver.find_element_by_tag_name("body")
    num_of_pagedowns = 10
    n = 1
    url_temp = []

    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.7)
        num_of_pagedowns -= 1

        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html)
        insta = soup.select('.v1Nh3.kIKUG._bz0w')

        for i in insta:
            #print('https://www.instagram.com' + i.a['href'])
            imgUrl = i.select_one('.KL4Bh').img['src']
            if imgUrl in url_temp:
                print("Already Exist!") # Ignore duplicate photos
            else:
                with urlopen(imgUrl) as f:
                    with open('./main/static/image/' + eng_univ + str(n) + '.jpg', 'wb') as h:
                        img = f.read()
                        h.write(img)
                n += 1
                url_temp.append(imgUrl)



    # #Delete photos that contain face or body
    face_cascade = cv2.CascadeClassifier('/Users/yukyung/insta_project/posts/main/static/image/data/haarcascades/haarcascade_frontface.xml')
    profile_cascade = cv2.CascadeClassifier('/Users/yukyung/insta_project/posts/main/static/image/data/haarcascades/haarcascade_profileface.xml')

    n_temp = []
    for i in range(1, n):
         # Convert to gray image
         search_img = "/Users/yukyung/insta_project/posts/main/static/image/" + eng_univ + str(i) + '.jpg'
         image = cv2.imread(search_img, cv2.IMREAD_COLOR)
         grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

         faces = face_cascade.detectMultiScale(grayImage, 1.1, 5, 0, (80, 80))
         profilefaces = profile_cascade.detectMultiScale(grayImage, 1.3, 5)

         # If faces detected, print image 
         if len(faces) > 0:
             print("Number of faces detected: " + str(faces.shape[0]))
             print(search_img)
             print(len(faces))

          # If profilefaces detected, print image
         if len(profilefaces) > 0:
             print("Number of profileface detected: " + str(profilefaces.shape[0]))
             print(search_img)
             print(len(profilefaces))
             
          # If eyes deteced, print image 
    #     # Delete the file if you find the person's face
         if(len(faces) > 0 or len(profilefaces) > 0):
             if os.path.isfile(search_img):
                 os.remove(search_img)
                 
         else:
             n_temp.append(i)

    # Extract Hashtag, Like_num, Content, Date, Place, url Information
    first = driver.find_element_by_css_selector('div._9AhH0')
    first.click()
    time.sleep(3)
    search_num = 91

    for i in range(0, search_num):
        html = driver.page_source
        soup2 = BeautifulSoup(html, 'lxml')

        # Like_num
        try:
            like.insert(i, soup2.select('div.Nm9Fw > button')[0].text[4:-1])
            print(like[i]+"a")
        except:
            like.insert(i, 0)

        

        # Content
        try:
            content.insert(i, soup2.select('div.C4VMK > span')[0].text)
        except:
            content.insert(i, '')

        # Date
        try:
            date.insert(i, soup2.select('time._1o9PC.Nzb55')[
                        0]['datetime'][:10])  # 10 characters from the front
        except:
            date.insert(i, '')

        # Place
        try:
            place.insert(i, soup2.select('div.JF9hh')[0].text)
        except:
            place.insert(i, '')

        # Tags
        tags.insert(i, re.findall(r'#[^\s#,\\]+', str(content)))

        # Url
        try:
            cur_url.insert(i, driver.current_url)
        except:
            cur_url.insert(i, '')

        # Next
        if (i != search_num - 1):
            right = driver.find_element_by_css_selector(
                'a._65Bje.coreSpriteRightPaginationArrow')
            right.click()
            time.sleep(3)

    # Save image from local to MySQL
    # Save each information
    conn = pymysql.connect(host="localhost", user="root", password="1234", db='capstone', charset='utf8mb4')
    cur = conn.cursor()

    for i in range(0, search_num):
        if i+1 in n_temp:   # Only information from photos that have not been deleted
            # Pre-work before processing the number of likes
            #subValue = 'span'
            #like[i].replace(" ", "")
            str(like[i]).strip()
            if (like[i] == "[]"):#좋아요 0개일경우
                like[i] = '0'
            if (str(like[i]).find(",")):
                like[i] = str(like[i]).replace(",", "")
            if (like[i] == ''):
                like[i] = '0'
                print("없음")
            #if(str(like[i]).find(" ")):
            #    continue
                
                #str(like[i]).replace(" ", "")
            #elif (like[i].find(subValue)==-1):
            #    print(like[i])
            
            #     like[i] = '0'#like[i].split('좋아요 ')[1].split('개')[0]
            # elif (like[i].find(subValue)!=-1):
            #     like[i] = like[i].split('<span>')[1].split('</span>')[0]
            
            

            print("확인 1 :" + like[i])
            #else:
            #    like[i] = '0'

            if (int(like[i]) > 100):
                print("확인 2 : {}".format(int(like[i])))
                img_path = '/static/image/' + eng_univ + str(i + 1) + '.jpg'
                #img_path = url_temp[i]
                #print(type(url_temp[i]))
                sql = "insert into insert_db(univ, img_path, like_num, content, tags, place, write_date, cur_url) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                print(type(img_path))
                insert_tags = " ".join(tags[i])
                var = [univ[search_univ.index(x)], img_path, like[i], "hello", "hello", place[i], date[i], cur_url[i]]
                cur.execute(sql,var)
                
                conn.commit()

        
                

driver.close()
conn.close()
