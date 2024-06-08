필요 세팅

<h2>1. 웹 드라이버 & selenium 설치 🪛🪛</h2>

크롬 웹 드라이버 설치 사이트 : https://developer.chrome.com/docs/chromedriver/downloads?hl=ko

참고 사이트 : https://velog.io/@bansohi/Python-Selenium-Chrome-driver-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0

스팀 로봇텍스트 : https://store.steampowered.com/robots.txt

pandas도 필요함

<h2>2. 권한 허용 ✅✅</h2>

![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/3f6d6c58-d9eb-4f40-a420-c448258d07c1)

<h2>3. 세팅 😎😎</h2>


![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/12414d4e-bccf-4afa-9d59-7dda394d374d)

<hr>

country : 수집할 국가 결정
![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/8f04393b-9e86-4066-b79b-b68cad57892b)


date : 수집 시작 날짜 결정
"https://store.steampowered.com/charts/topsellers/KR/2024-5-28" 
![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/daba3967-e99d-48eb-8474-316413ef3b8f)

page : 시작일부터 몇 주 동안의 데이터를 수집할 것인지 결정

start_number : 몇 위 부터 수집할 것인지 결정<br>
( 종종 중간에 종료되는 경우가 있어서 그럴 경우 백업된 파일을 보고 해당 순위부터 수집 시작 )

<h2>3. 사용 🥵🥵</h2>

-1. 코드를 실행한 뒤 반드시 성인 인증을 해주어야 함<br>

![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/eeb197b4-3997-438c-a64e-c27be95d17a4)

-2. view page를 눌러주어서 성인 인증 후 다시 순위 페이지로 돌아오기<br>
![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/b7e30cf7-ee84-4716-85b9-d27255c6cc9a)

-3. 이후 콘솔창에서 아무값이나 입력해서 실행<br>
![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/00ed1a32-b6c1-4c2e-8051-7ea0475e4752)

<h2>4. 결과 👏👏</h2>

결과물은 엑셀 파일로 "C:\Users:\유저이름" 경로에 생성
![image](https://github.com/TTobing3/steam-data-Crawling/assets/100311186/af340c6f-ffc2-457f-b075-e6eee944d647)

! 할인의 경우 원래 가격과 동시에 입력<br>
! 리뷰의 경우, 최근 리뷰가 아닌 전체 리뷰<br>
! 한국에서 제한된 게임은 이름만 수집한  스킵<br>
