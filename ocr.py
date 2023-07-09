import cv2
import pytesseract
import serial

# Inicialização da webcam
webcam = cv2.VideoCapture(0)

# Configuração do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Caminho para o executável do Tesseract
custom_config = r'--oem 3 --psm 6'  # Configuração personalizada do Tesseract

# Configuração da porta serial da Raspberry Pi Pico
serial_port = '/dev/ttyACM0'  # Porta serial da Pico
baud_rate = 9600  # Taxa de transmissão

# Inicialização da conexão serial
ser = serial.Serial(serial_port, baud_rate)

while True:
    # Captura do quadro da webcam
    ret, frame = webcam.read()

    # Redimensionamento do quadro para melhorar o desempenho
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Detecção de texto usando OCR
    text = pytesseract.image_to_string(frame, config=custom_config)

    # Verificações do texto
    if "LHR786" in text or "lhr786" in text or "Lhr786" in text:
        print("Placa: LHR786")
        print("Registrado")
        print("Nome: Jhon")
        print("CPF: 13106-5256283-7")
        print("Veículo: Corolla 2006")
        print("Chassi: 3322bv54676")
        ser.write(b'1\n')  # Envia o comando para a Raspberry Pi Pico
    elif "ABC1" in text or "abc1" in text or "Abc1" in text:
        print("Placa: ABC1")
        print("Registrado")
        print("Nome: Afaq")
        print("CPF: 13401-6756284-2")
        print("Veículo: HONDA 2004")
        print("Chassi: 552Cbv76676")
        ser.write(b'1\n')  # Envia o comando para a Raspberry Pi Pico
    elif "RWP4" in text or "RWP 4" in text or "rwp 4" in text:
        print("Placa: RWP4")
        print("Não registrado")
        print("Sem informações disponíveis")

    # Exibição do quadro
    cv2.imshow("OCR", frame)

    # Verificação de tecla de saída
    if cv2.waitKey(1) == 27:  # Tecla Esc
        break

# Liberação da webcam, fechamento da janela e encerramento da conexão serial
webcam.release()
cv2.destroyAllWindows()
ser.close()
