from gpiozero import LED, Button,LEDBoard #gpiozero라이브러리에서 led,button,LEDBoard클래스 임포트
from signal import pause #signal 모듈에서 pause함수 임포트

leds = LEDBoard(24,23,21,20) #24,23,21,20번 각각을 LED로 사용하는 LEDBoard 객체생성
button = Button(25, pull_up=True, bounce_time=0.1) #25번핀을 pull_up(내부 풀업저항)으로 기본상태를 high로, 버튼의 디바운스를 처리하기 위해 0.1초 바운스타임설정
count = 0 #현재 나타내는 숫자가 몇인지 저장할 변수선언

def countup(): # 버튼이 누르면 호출될 함수
    global count #count를 전역변수로 사용명시
    count = (count+1)%16 # 버튼이 눌릴때마다 호출되며 0~15를 순환하며 증가
    leds.value = (1&count,  2&count,  4&count,  8&count) #count변수의 각 비트자리가 0인지 1인지 확인하는 &연산을 수행해서 그 값을 각각 led의 value(on/off)로 설정


button.when_pressed = countup #버튼이 눌리면 countup 함수 호출

pause() #코드실행후 종료하지않고 led를 작동시키고 버튼의 입력을 받아드릴 수 있도록 합니다.
