int x;
int LED=13;
int red_led = 2;
int green_led = 3;
void setup() {
 pinMode(red_led, OUTPUT);
 pinMode(green_led, OUTPUT);                     
 digitalWrite (red_led, LOW);
 digitalWrite (green_led, LOW);
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 if (x == 0){
  digitalWrite (red_led, HIGH);
  digitalWrite (green_led, LOW);
 }
 else if(x == 1){
  digitalWrite (green_led, HIGH);
  digitalWrite (red_led, LOW);
 }
}
