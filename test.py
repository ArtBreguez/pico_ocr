import serial
import time

# Abrir a conexão serial
s = serial.Serial('COM7', 9600, timeout=0)

while True:
    message = input("Digite uma mensagem: ")
    # Enviar o comando para a Raspberry Pi Pico
    s.write(message.encode() + b'\n')
    time.sleep(1)
