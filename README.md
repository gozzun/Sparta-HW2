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

<피드백 사항>
- 서버를 구동하면 존재하지 않는 페이지를 표시합니다. 반드시 존재하는 페이지를 기본으로 표시하도록 해주셔야해요.
- 회원가입할 때 유효하지 않은 패스워드를 입력하면 OperationalError at /accounts/signup/ 오류 페이지가 발생합니다.
  예외처리를 해주셔서 반드시 사용자가 옳바른 값을 입력하도록 해주셔야해요.
- 회원가입이 되지 않습니다 ㅜㅠ 다른 기능을 확인할 수가 없어요.
-유효하지 않는 로그인을 시도하면 OperationalError at /accounts/login/ 오류 페이지가 발생합니다.
  마찬가지로 예외처리를 해주셔서 반드시 사용자가 옳바른 값을 입력하도록 해주셔야해요.
- readme를 잘 작성해주셨어요. 그치만 어떤 프로젝트인지 소개하는 내용도 반드시 필요합니다. 
- 반드시 배포하실 때 업로드한 프로젝트를 다운받아서 구동해보시는 배포test를 진행하시기를 적극적으로 권유드립니다.
- 전체적으로 코드를 봤을 때 기능을 제대로 확인하지는 못했지만 최대한 열심히하신 부분들을 확인할 수있었어요.
  굉장히 고생 많으셨고 심화 때도 힘내주세요! 파이팅입니다.! 정말로 고생 많으셨어요!
