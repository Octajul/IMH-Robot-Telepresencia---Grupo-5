let right: number;
let left: number;
//  Variable para llevar a cabo un limite de diferencia mayor entre sensores de luz
//  Permite determinar la sensibilidad de diferencia entre ambos sensores
let diff = 100
//  Variable para leer el sonar
let distance = 0
// Mostrar una imagen de cara dormida
basic.showIcon(IconNames.Asleep)
// input.button_is_pressed(Button.A)
// input.button_is_pressed(Button.B)
// Parar el bot si estaba en movimiento
gigglebot.stop()
// Definir velocidad de movimiento de los motores
gigglebot.setSpeed(gigglebotWhichMotor.Both, 50)
// Loop principal
while (true) {
    // Definir accion si boton A se presiona
    if (input.buttonIsPressed(Button.A)) {
        // Mostrar imagen de corazon
        basic.showIcon(IconNames.Heart)
        // Entrar en nuevo Loop
        while (true) {
            //  Mostrar cara feliz
            basic.showIcon(IconNames.Happy)
            // Leer sensores de luz 
            right = gigglebot.lightReadSensor(gigglebotWhichTurnDirection.Right)
            left = gigglebot.lightReadSensor(gigglebotWhichTurnDirection.Left)
            // Leer el valor en sentimetros del sonar deifniendo los pines en que esta conectado el sonar.ping(DigitalPin.P0, DigitalPin.P0, PingUnit.MICRO_SECONDS)
            distance = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.Centimeters)
            // gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
            //  Si la distamia es mayor a 15 cm el robot debe de evitar caerse 
            //  Se puede cambiar el comparador para que funcione en funcion de si tiene obstaculos adelante
            while (distance < 15) {
                // Lee ocnstantemente la distancia y gira hasta que la distancia sea menor significando que no esta al borde de la mesa
                distance = sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.Centimeters)
                gigglebot.gigglebotSpin(gigglebotWhichTurnDirection.Right)
            }
            //  Ver si un sensor capta mayor luz que el otro 
            // Si derecha capta mas que izquiera girar a la derecha
            if (right > left + diff) {
                gigglebot.turn(gigglebotWhichTurnDirection.Right)
            } else if (left > right + diff) {
                // Si capta mas izquierda girar a la izquierda
                gigglebot.turn(gigglebotWhichTurnDirection.Left)
            } else {
                // Si captan similar ir recto
                gigglebot.driveStraight(gigglebotWhichDriveDirection.Forward)
            }
            
            // Si el boton B es presionado salir del loop y detener el robot y mostrar cara dormida
            if (input.buttonIsPressed(Button.B)) {
                gigglebot.stop()
                basic.showIcon(IconNames.Asleep)
                break
            }
            
        }
    }
    
}
