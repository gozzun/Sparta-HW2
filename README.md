실행:
1. git clone https://github.com/gozzun/Sparta-HW2
2. cd Sparta-HW2
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

<스파르타마켓> 
-회원만 서비스 이용 가능, 각 유저는 물건을 등록하고 찜을 누를 수 있음. 구매하기 구현X

<필수 구현>
-회원 기능 
회원가입/로그인/로그아웃 앱: accounts urls.py: signup, login, logout

-유저 기능 유저별 프로필 페이지 구현 username, 가입일, 내가 등록한 물품, 내가 찜한 물품, 팔로잉(팔로잉 수, 팔로워 수) 
앱: accounts, products(찜) 
모델: following(M:N), created_at, author(찜, FK), like_users(찜, M:N)

-게시 기능 물건 목록 페이지, 물건 개별 페이지 CRUD 구현 찜하기 기능 
앱: products, accounts(찜) 
모델: title, content, created_at, updated_at, author(FK), like_users(M:N)

<심화 구현>
-회원 기능 프로필 사진 
앱: accounts 
모델: image

-게시 기능 찜 수, 조회수 최신순/찜순 정렬 
앱: products 
모델: views

-해시태그 기능 해시태그 추가 
앱: products 모델: Hashtag 
모델 추가, hashtags(Product 내, M:N)

-검색 기능 
앱: products 
Q, icontains 이용

<추가로 구현해야할 사항>
해시태그 입력하지 않아도 물건 이미지와 마찬가지로 그냥 넘어가도록/물건 삭제 시 해시태그도 삭제/해시태그 수정/해시태그 누르면 해당 게시글로 이동
