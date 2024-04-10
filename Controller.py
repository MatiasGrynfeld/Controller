import vgamepad as vg
import serial
gamepad = vg.VDS4Gamepad()

def set_joystick(x: int, y: int, button_state, last_state):
    gamepad.left_joystick(x, y)
    if button_state==True and last_state != button_state:
        gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    elif button_state==False and last_state != button_state:
        gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    gamepad.update()
    last_state = button_state
    return last_state

input_X = 0
input_Y = 0
button_pressed = False
last_state= False

com_port = "COM4"
ser = serial.Serial(com_port, 115200)

while True:
    data = ser.readline().decode().strip()
    values = data.split(" ")
    last_state=set_joystick(int(values[0]), int(values[1]), bool(int(values[2])), last_state)
else:
    gamepad.close()
