#include "led_controller.h"
#include <stdio.h>

int main(void) {
    LED led;
    LED_Init(&led);

    LED_TurnOn(&led);
    LED_SetBrightness(&led, 128);

    LED_TurnOff(&led);
    LED_SetBrightness(&led, 200);

    return 0;
}
