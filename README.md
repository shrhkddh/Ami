# 9-WE_T_S-backend

## Demo Video

[![](https://user-images.githubusercontent.com/63710565/89256216-8bdce180-d65e-11ea-9fd5-d99b5cc3183b.png)](https://youtu.be/c9qNDQm6qqM)

## Modeling

![ami2_20200804_13_18](https://user-images.githubusercontent.com/63710565/89264240-8f2b9980-d66d-11ea-9aa9-da32b9aa2a74.png)

## Introduction
- 2011년 시작된 프랑스의 컨템포러리 패션 브랜드
- 프로젝트 기간 : 2020.6.22 ~ 2020.7.3 (12일)
- 개발 인원 : Front-End 3명(김정현,박창수,손혜인), Back-End(노광오,박상영,양희연)

## 1차 프로젝트 소개
미니멀한 프린트 및 색상과 소재만으로 고유의 유니크한 매력을 담아내는 아미 파리스(Ami Paris) 웹사이트 클론 프로젝트

## 목표
- amiparis.com/kr/shopping/man/ 사이트의 interface와 동일하게 화면 구현하기
- 회원가입/로그인, cart, wishlist 기능 구현하기
- Back-End API를 통해 데이터를 GET / POST 하기
- trello를 사용해 협업하며 매일 정해진 시간에 stand up 미팅 진행하기

## 사용한 기술
- Python, Django
- MySQL
- BeautifulSoup, Selenium
- JWT, Bcrypt
- CORS Headers
- Git, GitHub

## 기능
1. account
    - 유저정보 저장
    - 회원가입 / 로그인
    - 패스워드 암호화 및 유효성 검사
    - 로그인 시 JWT Acess Token 발행
    - 로그인 상태인지 확인하는 데코레이터 함수

2. menu
    - 상품들을 카테고리별로 분류해서 데이터 저장

3. product
    - 제품 상세정보 구현

4. order
    - 회원별 wishlist 구현(담기, 지우기)
