# Variable para llevar a cabo un limite de diferencia mayor entre sensores de luz
# Permite determinar la sensibilidad de diferencia entre ambos sensores
diff = 100
# Variable para leer el sonar
distance=0
#Mostrar una imagen de cara dormida
basic.show_icon(IconNames.ASLEEP)
#input.button_is_pressed(Button.A)
#input.button_is_pressed(Button.B)
#Parar el bot si estaba en movimiento
gigglebot.stop()
#Definir velocidad de movimiento de los motores
gigglebot.set_speed(gigglebotWhichMotor.BOTH, 50)
#Loop principal
while True:
    #Definir accion si boton A se presiona
    if input.button_is_pressed(Button.A):
        #Mostrar imagen de corazon
        basic.show_icon(IconNames.HEART)
        #Entrar en nuevo Loop
        while True:
            # Mostrar cara feliz
            basic.show_icon(IconNames.HAPPY)
            #Leer sensores de luz 
            right=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.RIGHT)
            left=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.LEFT)
            #Leer el valor en sentimetros del sonar deifniendo los pines en que esta conectado el sonar.ping(DigitalPin.P0, DigitalPin.P0, PingUnit.MICRO_SECONDS)
            #Leer el valor en centímetros del sonar definiendo los pines en que esta conectado el sonar
            distance= sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)

            #gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
            # Si la distancia es mayor a 15 cm el robot debe de evitar caerse 
            # Se puede cambiar el comparador para que funcione en funcion de si tiene obstaculos adelante
            while distance<15:
                #Lee ocnstantemente la distancia y gira hasta que la distancia sea menor significando que no esta al borde de la mesa
                distance= sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)
            # Se puede cambiar el comparador para que funcione en función de si tiene obstáculos delante
            while distance>15:
                #Lee constantemente la distancia y gira hasta que la distancia sea menor significando que no esta al borde de la mesa
                gigglebot.gigglebot_spin(gigglebotWhichTurnDirection.RIGHT)
                distance= sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)

            # Ver si un sensor capta mayor luz que el otro 
            #Si derecha capta mas que izquiera girar a la derecha
            if right > left+diff:

                gigglebot.turn(gigglebotWhichTurnDirection.RIGHT)
            #Si capta mas izquierda girar a la izquierda
            elif left > right+diff:
                gigglebot.turn(gigglebotWhichTurnDirection.LEFT)
            #Si captan similar ir recto
            else:
                gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
            #Si el boton B es presionado salir del loop y detener el robot y mostrar cara dormida
            if input.button_is_pressed(Button.B):
                gigglebot.stop()
                basic.show_icon(IconNames.ASLEEP)
                break
