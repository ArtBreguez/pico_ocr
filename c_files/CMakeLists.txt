cmake_minimum_required(VERSION 3.12)

include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)

project(blink_led C CXX ASM)

pico_sdk_init()

add_executable(blink_led
	blink_led.c
	)

target_link_libraries(blink_led pico_stdlib)

pico_enable_stdio_usb(blink_led 1)
pico_enable_stdio_uart(blink_led 1)

pico_add_extra_outputs(blink_led)