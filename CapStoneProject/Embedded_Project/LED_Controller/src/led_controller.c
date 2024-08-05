#include "../include/led_controller.h"
#include <stdio.h>

void LED_Init(LED* led) {
    led->state = OFF;
    led->brightness = 0;
    printf("LED initialized. State: OFF, Brightness: 0\n");
}

void LED_TurnOn(LED* led) {
    led->state = ON;
    printf("LED turned on.\n");
}

void LED_TurnOff(LED* led) {
    led->state = OFF;
    printf("LED turned off.\n");
}

void LED_SetBrightness(LED* led, uint8_t brightness) {
    if (led->state == ON) {
        led->brightness = brightness;
        printf("LED brightness set to %d.\n", brightness);
    } else {
        printf("LED is off. Cannot set brightness.\n");
    }
}
