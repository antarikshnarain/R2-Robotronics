int pin1 = 8;
int pin2 = 9;
int mtrLf = 5;
int mtrLb = 6;
int mtrRf = 10;
int mtrRb = 11;

int i;
int l;
char ch;
char arr[10];

int device;
int ptr;
int value;

void writeMotors(int a, int b, int c, int d)
{
  analogWrite(5, a);
  analogWrite(6, b);
  analogWrite(10, c);
  analogWrite(11, d);
}
void baseFB() // Base Motors Forward Backward
{
  if (value < 0)
  {
    value = -1 * value;
    writeMotors(value, 0, value, 0);
  }
  else
  {
    writeMotors(0, value, 0, value);
  }
}
void baseLR()
{
  if (value < 0)
  {
    value = -1 * value;
    writeMotors(0, value, value, 0);
  }
  else
  {
    writeMotors(value, 0, 0, value);
  }
}
void setup() {
  // put your setup code here, to run once:
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  Serial.begin(115200);
}


void execute()
{
  device = arr[0] - 'A';  ptr = 1;  value = 0;
  if (arr[1] == '-')
  {
    for (i = 2; i < l; i++)
      value = value * 10 + arr[i] - '0';
    value = value * -1;
  }
  else
  {
    for (i = 1; i < l; i++)
      value = value * 10 + arr[i] - '0';
  }
  Serial.println(device);
  Serial.println(value);
  switch (device)
  {
    case 0:
      baseFB();
      break;
    case 3:
      baseLR();
      break;
    case 1:
      break;
    case 2:
      break;
    case 4:
      digitalWrite(pin1, value);
      digitalWrite(pin2, 0);
      break;
    case 5:
      digitalWrite(pin1, 0);
      digitalWrite(pin2, value);
      break;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    ch = Serial.read();
    if (ch == '<')
      l = 0;
    else if (ch == '>')
      execute();
    else
      arr[l++] = ch;
  }
}
