#ifndef LED_CONTROLLER_H
#define LED_CONTROLLER_H

#include <stdint.h>

typedef enum {
    OFF,
    ON
} LEDState;

typedef struct {
    LEDState state;
    uint8_t brightness;  // 0 (off) to 255 (maximum brightness)
} LED;

void LED_Init(LED* led);
void LED_TurnOn(LED* led);
void LED_TurnOff(LED* led);
void LED_SetBrightness(LED* led, uint8_t brightness);

#endif // LED_CONTROLLER_H
