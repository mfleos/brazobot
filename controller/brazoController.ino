// pins for the LEDs:
const int pin0 = 7;
const int pin1 = 8;

void setup()
{
  // Initialize Serial Port
  Serial.begin(9600);

  // Output Pins
  pinMode(pin0, OUTPUT); 
  pinMode(pin1, OUTPUT); 

}

void loop()
{
	int set;

  // Set H-Bridge Direction
  if( (set = Serial.read()) != -1 )
	{
    Serial.write(set);
    switch (set)
		{
      case 0x30:
        digitalWrite(pin0, LOW);
        digitalWrite(pin1, LOW);
        break;
      case 0x31:
        digitalWrite(pin0, LOW);
        digitalWrite(pin1, HIGH);
        break;
      case 0x32:
        digitalWrite(pin0, HIGH);
        digitalWrite(pin1, LOW);
        break;
      default:
        break;
    }
    delay(1000);
  }
}

