1차발표: https://youtu.be/NDh2bC0vJQs

게임 이름: 가디언 오브 테라

2017180039정극훈

1. 게임 컨셉: 외계 생물의 침입을 방어시설을 건설하거나 전투기를 출력해 막는 게임
   
   -1. 적이 위에서부터 내려오며 일부 적은 투사체를 발사해 원거리 공격
   
   -2. 자원을 소모해 방어시설을 건설하여 적을 막거나 공격
   
   -3. 전투기를 출격시켜 직접 적을 공격
   
   -4. 전투기가 출격하면 지속적으로 연료 소모, 기지 복귀 시 연료 회복
   
   -5. 전투기에 적이나 적 투사체가 닿으면 체력 소모, 체력이 0이 되면 해당 라운드에서 출격 불가
   
   -5. 기지에 적이나 적 투사체가 닿으면 체력 소모, 체력이 0이 되면 게임 오버
   
   -6. 라운드가 끝나면 대기화면으로 이동->자원을 소모해 업그레이드 가능
   
   -7. 대기화면에서 라운드 시작버튼을 누르면 새로운 라운드 시작
   
   ![1](https://github.com/user-attachments/assets/7b071a87-4be8-4c40-a69e-8b147fda04b9)
   ![2](https://github.com/user-attachments/assets/61fb7f1b-43d0-4f87-b8cf-ee52eeff512a)
   ![3](https://github.com/user-attachments/assets/af07c9ee-6643-427a-a368-cdbbc375130e)

   
3. 개발 내용
   - Scene: 메인화면, 라운드, 대기화면, 게임오버
   - 
   - 메인화면->라운드<->대기화면
  
                    ->게임오버->메인화면
   -            
   - 메인화면: 시작버튼, 종료버튼
     
     - 시작버튼: 라운드씬을 push해 게임 시작
       
     - 종료버튼: 프로그램 종료
       
    - 라운드: 기지, 방어시설, 전투기, 적 오브젝트들
      
      - 기지: 적이나 적 투사체에 닿으면 체력 소모, 체력이 0이 되면 게임 오버
        
      - 방어시설: 자원을 소모해 적을 막거나 자동 공격하는 시설 설치, 적이나 적 투사체에 닿으면 체력 소모, 체력이 0이 되면 시설 사라짐
     
      - ![image](https://github.com/user-attachments/assets/5726fc7f-61f9-401a-895d-42330e8f814e)
     
      - 터렛 설치 공간에 좌클릭하면 공격터렛, 우클릭하면 방어터렛 설치
     
      - 적과 부딪히면 터렛의 체력이 줄어들며 체력이 0이 되면 제거됨

        
      - 전투기: 투사체를 발사해 적을 공격, 출격시 연료가 지속적으로 소모되며 0이 되면 기지복귀, 기지복귀시 연료가 회복됨, 적이나 적 투사체에 닿으면 체력 소모, 체력이 0이 되면 해당 라운드에서 출격 불가
        
      - 적: 화면 위에서 생성되며 아래쪽으로 내려옴, 아군에게 닿으면 피해를 주며 일부 적은 피해를 주는 투사체를 발사
        
    - 대기화면: 업그레이드, 라운드시작버튼
      
      - 업그레이드: 자원을 소모해 각종 요소들을 업그레이드(기지, 방어시설, 전투기)
        
      - 라운드시작버튼: 대기화면을 pop해 라운드씬으로 이동
        
    - 게임오버: 점수판, 종료버튼
      
      - 점수판: 점수를 계산에 화면에 표시
        
      - 종료버튼: 메인을 제외한 씬들을 pop해 메인화면으로 복귀
        

4. 일정
   
![image](https://github.com/user-attachments/assets/43e15d17-057f-41e4-879c-2f97f3f5d454)


5. 진행상황

   2주차: 씬변환 완료, 터렛 객체 생성까지 진행

   3주차: 메인씬 게임시작버튼 추가, 공격/방어터렛 생성 및 제거, 전투기 출동 및 제거
   

7. 커밋
   
   ![image](https://github.com/user-attachments/assets/14a1a5ee-9e06-45ac-a892-9293216866fb)

   ![image](https://github.com/user-attachments/assets/4d73e9bc-3030-450d-9d9c-4844fad3887e)




