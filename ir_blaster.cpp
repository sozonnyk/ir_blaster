#include "ir_blaster.h"
#include <IRremote.h>
//#define DBG

IRsend irsend;

// TX pin = Atmega328 - 3, Atmega32u4 - 5
// For Atmega32u4 changes required in IRremoteInt.h: Enable IR_USE_TIMER3 and add TIMER_PWM_PIN 5
// Also change USBCore.cpp SendDescriptor(USBSetup& setup), line 531
//			char name[ISERIAL_MAX_LEN] = "ir-blaster";
//			//PluggableUSB().getShortName(name);

int PAUSE = 10;
int NEC_BITS = 32;

void setup() {
	Serial.begin(115200);
	Serial.setTimeout(9999999999999);
#ifdef DBG
	while (!Serial);
	Serial.println("Ready ");
#endif
}

void pana(unsigned long addr, unsigned long data) {
	irsend.sendPanasonic(addr, data);
	delay(PAUSE);
}

void nec(unsigned long data) {
	irsend.sendNEC(data, NEC_BITS);
	delay(PAUSE);
}

void process(String str) {
	str.trim();
#ifdef DBG
	Serial.println("in: -"+str+"-");
#endif
	unsigned long data_1 = 0, data_2 = 0;

	char buffer[str.length() + 1];
	str.toCharArray(buffer, str.length()+1);

	int n = sscanf(buffer, "%lx:%lx", &data_1, &data_2);

	switch (n) {
	case 1:
		//NEC code
#ifdef DBG
		Serial.print("NEC ");
		Serial.println(data_1);
#endif
		nec(data_1);
		break;
	case 2:
		// Panasonic code
#ifdef DBG
		Serial.print("Pana ");
		Serial.print(data_1);
		Serial.print(":");
		Serial.println(data_2);
#endif
		pana(data_1, data_2);
		break;
	}
	Serial.println("OK");
}

void loop() {
	if (Serial && Serial.available() > 0) {
		process(Serial.readStringUntil('\n'));
	}
}

