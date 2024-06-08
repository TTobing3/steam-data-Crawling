from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

#순위 & 이름
rank_list = []
title_list = []
#가격
price_list = []
#리뷰
review_list = []
#기간
date_list = []
#출시일
release_date_list = []
#랭킹 대상 국가
country_list = []
#장르
genre_list = []
#개발사
developer_list = []
#퍼블리셔
publisher_list = []

start_time = time.time()

''' 시작세팅으로 반드시 성인 필터 해제 '''
''' 크롬 드라이버도 깔아야 함 '''

country = "KR" #대상 국가
date = "2024-5-28" #대상 날짜, 웹 사이트 들어가서 측정 시작일
page = 1
start_number = 1 #시작할 순위

driver = webdriver.Chrome()
driver.get('https://store.steampowered.com/charts/topsellers/'+country+'/'+date)
driver.implicitly_wait(3)

input('시작 세팅 끝 : ') #성인 해제 하고 콘솔창에 아무거나 입력해서 크롤링 시작


for i in range(1,page+1):
    print(str(i)+"번째 페이지")
    for j in range(start_number,100+1):
        print(str(j)+'시작')
        #driver.find_element(By.XPATH, '').text
        #처음 100위까지 보이기

        driver.refresh()

        #//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr[84]/td[3]/a/div
        #//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr[85]/td[3]/a/div
        #//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr[85]/td[3]/a/div/span

        #없으면 눌러
        #순위
        print('순위')
        rank_list.append(j)

        #이름
        print('이름')
        if driver.find_elements(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[3]/a/div') :
            title_list.append(driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[3]/a/div').text)
        else :
            driver.find_elements(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/div/button')[0].click()
            title_list.append(driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[3]/a/div').text)
        #기간
        print('기간')
        date_list.append(driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[3]/div[3]').text)
        #국가
        print('국가')
        country_list.append(driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[1]/div/div/div/div[1]').text)
        #가격
        print('가격')
        price_element = driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[4]/div')
        if(price_element.text==''): #가격 없는
            price_list.append(0)
        elif(len(price_element.find_elements(By.XPATH,'./div/div')) == 1): #일반
            price_list.append(price_element.find_element(By.XPATH,'./div/div').text)
        elif(len(price_element.find_elements(By.XPATH,'./div/div')) > 1):
            price_element_1 = driver.find_element(By.XPATH,'//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[4]/div/div/div[2]')
            if (price_element_1.text == '') : #할인
                price_list.append(price_element.find_element(By.XPATH,'./div/div[2]/div[1]').text)
            else : #예구
                price_list.append(price_element.find_element(By.XPATH,'./div/div[2]').text)
     
        #세부 페이지로 이동
        print('이동')
        driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[4]/table/tbody/tr['+str(j)+']/td[3]/a').click()

        try :

            #장르 <array>
            print('장르')
            try :
                genre_element = driver.find_elements(By.XPATH, '//*[@id="genresAndManufacturer"]/span/*')
                genre = ''
                for i in range(0, len(genre_element)):
                    genre += ','+genre_element[i].text
                genre = genre[1:]
                genre_list.append(genre)
            except :
                genre_list.append(None)
                review_list.append(None)

            #리뷰
            print('리뷰')
            try :
                review_element = driver.find_element(By.XPATH, '//*[@id="userReviews"]')
                if len(review_element.find_elements(By.XPATH, './*')) == 1 :
                    review_list.append (review_element.find_elements(By.XPATH, './*')[0].find_elements(By.XPATH, './*')[1].text)
                else :
                    review_list.append (review_element.find_elements(By.XPATH, './*')[1].find_elements(By.XPATH, './*')[1].text)
            except :
                review_list.append(None)

            #출시일
            print('출시일')
            try :
                panel = driver.find_element(By.XPATH, '//*[@id="game_highlights"]')
                if len(panel.find_elements(By.XPATH,'./*')) > 3 :
                    release_date = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[2]/div/div[3]/div[2]')
                    release_date_list.append(release_date.find_elements(By.XPATH,'./*')[1].text)
                else: 
                    release_date = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[3]/div[2]')
                    release_date_list.append(release_date.find_elements(By.XPATH,'./*')[1].text)
            except :
                release_date_list.append(None)
                
            #개발사 및 퍼블리셔
            print('퍼블리셔 개발사')
            try :
                if len(panel.find_elements(By.XPATH,'./*')) > 3 :
                    made = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[2]/div/div[3]')
                else :
                    made = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[3]')
                try : developer_list.append(made.find_elements(By.XPATH,'./*')[2].find_elements(By.XPATH,'./*')[1].text)
                except : developer_list.append(None)
                try : publisher_list.append(made.find_elements(By.XPATH,'./*')[3].find_elements(By.XPATH,'./*')[1].text)
                except : publisher_list.append(None)
            except :
                developer_list.append(None)
                publisher_list.append(None)
        except :
            genre_list.append(None)
            review_list.append(None)
            release_date_list.append(None)
            developer_list.append(None)
            publisher_list.append(None)
        
        print(str(j)+'끝')
        df = pd.DataFrame({'순위':rank_list,
                        '이름':title_list,
                        '가격':price_list,
                        '기간':date_list,
                        '랭킹 국가':country_list,
                        '장르':genre_list,
                        '리뷰':review_list,
                        '출시일':release_date_list,
                        '개발사':developer_list,
                        '퍼블리셔':publisher_list})
        df.to_excel('steam_'+country+'.xlsx')
        print(str(i)+'페이지'+str(j)+'까지 임시 저장')
        driver.back()
    
    df.to_excel('steam_'+country+'_backup_0.xlsx')
        

    print("순위"+str(len(rank_list))+
          "이름"+str(len(title_list))+
          "가격"+str(len(price_list))+
          "기간"+str(len(date_list))+
          "랭킹 국가"+str(len(country_list))+
          "장르"+str(len(genre_list))+
          "리뷰"+str(len(review_list))+
          "출시일"+str(len(release_date_list))+
          "개발사"+str(len(developer_list))+
          "퍼블리셔"+str(len(publisher_list))+" ")
    df = pd.DataFrame({'순위':rank_list,
                    '이름':title_list,
                    '가격':price_list,
                    '기간':date_list,
                    '랭킹 국가':country_list,
                    '장르':genre_list,
                    '리뷰':review_list,
                    '출시일':release_date_list,
                    '개발사':developer_list,
                    '퍼블리셔':publisher_list})
    df.to_excel('steam_'+country+'_backup_1.xlsx')
    driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[3]/div[2]/a').click()
    start_number = 1

for i in rank_list : print(i)
for i in title_list : print(i)
for i in title_list : print(i)

df.to_excel('steam_'+country+'_backup_2.xlsx')

end_time = time.time()
print("경과 시간 : "+str(end_time-start_time))

print("종료")