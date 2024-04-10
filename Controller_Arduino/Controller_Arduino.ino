#define joyXPin A0
#define joyYPin A1
#define buttonPin 7

int joyXValue = 0;
int joyYValue = 0;
int lastButtonState = 0;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  joyXValue = analogRead(joyXPin);
  joyXValue = map(joyXValue, 0, 1023, 0, 255);
  joyYValue = analogRead(joyYPin);
  joyYValue = map(joyYValue, 0, 1023, 0, 255);
  int currentButtonState = !digitalRead(buttonPin);
  if (currentButtonState != lastButtonState){
    lastButtonState = currentButtonState;
  }


  Serial.print(joyXValue);
  Serial.print(' ');
  Serial.print(joyYValue);
  Serial.print(' ');
  Serial.println(currentButtonState);

  delay(10);
}

