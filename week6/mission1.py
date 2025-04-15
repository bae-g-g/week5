from gpiozero import LED, Button #gpiozero라이브러리에서 led,button클래스 임포트
from signal import pause  #signal 모듈에서 pause함수 임포트

led = LED(20) #20번핀을 LED로 사용하는 객체생성
button = Button(25, pull_up=True) #25번핀을 pull_up(내부 풀업저항)으로 기본상태를 high로 

led.source = button # led의 on/off를 결정하는 source를 버튼으로 설정합니다. 버튼의 value에 따라서 led의 value도 변경됩니다. 

pause() #코드실행후 종료하지않고 버튼의 입력을 받아드릴 수 있도록 합니다.
