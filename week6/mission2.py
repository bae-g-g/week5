from gpiozero import LED, Button #gpiozero라이브러리에서 led,button클래스 임포트
from signal import pause #signal 모듈에서 pause함수 임포트

led = LED(20) #20번핀을 LED로 사용하는 객체생성
button = Button(25, pull_up=True, bounce_time=0.1) #25번핀을 pull_up(내부 풀업저항)으로 기본상태를 high로, 버튼의 디바운스를 처리하기 위해 0.1초 바운스타임설정

button.when_pressed = led.toggle  # 버튼이 눌리면 led의 상태를 반전시키는 led.toggle 호출


pause()  #코드실행후 종료하지않고 led를 작동시키고 버튼의 입력을 받아드릴 수 있도록 합니다.
