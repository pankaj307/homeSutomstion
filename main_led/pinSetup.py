from machine import Pin

# white led
white_led_brightness_in1 = Pin(16, Pin.OUT, value=0)
white_led_brightness_in2 = Pin(5, Pin.OUT, value=0)
white_led_enbl = Pin(4, Pin.OUT, value=0)
white_led_switch = Pin(0, Pin.OUT, value=0)


# blue led
blue_led_brightness_in1 = Pin(2, Pin.OUT, value=0)
blue_led_brightness_in2 = Pin(14, Pin.OUT, value=0)
blue_led_enbl = Pin(12, Pin.OUT, value=0)
blue_led_switch = Pin(13, Pin.OUT, value=0)

# desk_light
desk_light = Pin(15, Pin.OUT, value=0)

#left_lamp
# left_lamp = Pin(1, Pin.OUT, value=0)
