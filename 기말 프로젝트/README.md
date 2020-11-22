
## 1. 게임의 소개
* **제목** : 저스다이스 (JUSDICE)
* **목적** : 몰려오는 적들을 막는 TD(TOWER DEFENCE)게임
* **방법** : 주사위를 배치하고 합성, 강화를 통해 적들을 저지한다.

![예시 이미지](https://github.com/meenki/20202DGP/blob/master/%EA%B8%B0%EB%A7%90%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/README/sample_image.png?raw=true)
**인게임 이미지**

## 2. GameState
* **Logo Scene
* **Menu Scene
* **Game Scene

**총 3개의 GameState**

## 3. GameState 설명
#### * LogoScene
- 게임 제목, 로고가 뜨는 화면 별다른 상호작용은 불가능하다.
- State이동
+ 일정 시간 경과 시 자동으로 MenuScene로 이동.
- Logo, GameTitle 배치

#### * MenuScene
- 게임의 타이틀 화면, 게임 시작 종료와 같은 분기점을 담당.
- 마우스 이벤트를 통한 state전환 가능
- state이동
+ 시작 버튼 -> GameScene
+ 종료 버튼 -> Exit
- GameTitle, Start, Exit 배치

#### * GameScene
- 게임의 메인 화면, 게임의 진행을 담당
- 마우스 이벤트를 통한 오브젝트와의 상호작용
- state이동
+ GameOver -> MenuScene
- Tower, Monster, Upgrade/Buy Button 배치

## 4. 필요한 기술

#### * 배운 기술
- 게임의 시작부터 종료까지의 진행할 때의 기본적인 로직
- 사용자 입력과 오브젝트, 오브젝트와 오브젝트간 상호작용시 이벤트 처리

#### * 2DGP에서 배울 것으로 기대되는 기술
- Python 언어 활용 능력

## 5. 게임 개요

![게임 개요](https://github.com/meenki/20202DGP/blob/master/%EA%B8%B0%EB%A7%90%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/README/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C2.PNG?raw=true)

## 6. 게임 플로우

![게임 플로우](https://github.com/meenki/20202DGP/blob/master/%EA%B8%B0%EB%A7%90%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/README/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C3.PNG?raw=true)

## 7. 개발 정보

![개발 정보](https://github.com/meenki/20202DGP/blob/master/%EA%B8%B0%EB%A7%90%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/README/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C4.PNG?raw=true)
