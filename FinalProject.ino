void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}
int x, y, z;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.avaliable()>0){
    if (Serial.read() == 'X'){
      x = Serial.parseInt();
    }
    if (Serial.read() == 'Y'){
      y = Serial.parseInt();
    }
    if (Serial.read() == 'Z'){
      z = Serial.parseInt();
    }
  }
  if (z < 150){
    if x < (LOWER THRESHOLD){
      analogWrite(9, 255);
      analogWrite(3, 255);
      digitalWrite(6, HIGH);
      digitalWrite(5, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
      delay(1000);
    }
    else if x > (UPPER THRESHOLD){
      analogWrite(9, 255);
      analogWrite(3, 255);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, HIGH);
      delay(1000);
    }
    else (
      analogWrite(9, 255);
      analogWrite(3, 255);
      digitalWrite(6, HIGH);
      digitalWrite(5, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, HIGH);
      delay(1000);
  }
  else {
      analogWrite(9, 255);
      analogWrite(3, 255);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
  }
}
