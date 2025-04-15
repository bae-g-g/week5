from gpiozero import LED, Button,LEDBoard #gpiozero라이브러리에서 led,button,LEDBoard클래스 임포트
from signal import pause#signal 모듈에서 pause함수 임포트

leds = LEDBoard(20,21,23,24) #20,21,23,24번 각각을 LED로 사용하는 LEDBoard 객체생성
button = Button(25, pull_up=True, bounce_time=0.1) #25번핀을 pull_up(내부 풀업저항)으로 기본상태를 high로, 버튼의 디바운스를 처리하기 위해 0.1초 바운스타임설정

def domino(): # 버튼이 눌리면 호출되는 함수입니다.
    for led in leds:  # ledboard객체의 각 요소들을 순서대로 반복합니다.
        led.blink(on_time=1, off_time=0,n=1,background=False) #각 요소가 1초간 켜지고(on_time=1) 바로 종료(off_time=0) 각 실행이 순차적으로 일어나게 블로킹(background=False)
            #1회만 blink되도록(n=1) 설정

button.when_pressed = domino #버튼이 눌리면 domino함수가 실행됩니다.

pause()   #코드실행후 종료하지않고 led를 작동시키고 버튼의 입력을 받아드릴 수 있도록 합니다.
