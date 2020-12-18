
> Open this page at [https://octajul.github.io/sonar--ligh-sensors/](https://octajul.github.io/sonar--ligh-sensors/)

# Proyecto de Robot de Telepresencia IMH

<a href="https://www.imh.eus/eu" rel="some text">![Foo](https://media-exp1.licdn.com/dms/image/C4D0BAQFpuzjCUj95cg/company-logo_200_200/0/1579542289894?e=2159024400&v=beta&t=MqzIGMRqGZ4diQz7Y4T1qaaIh0YsdYIQdwPKU6zvWMQ)</a>


>Se llevaron a cabo 5 tareas distintas que se pueden ver en el repositorio en cada carpeta
>

#Integrantes: Aitor, Iñaki & Julio Gonzalez

## Tarea 1 :

Codigo de Python para el funcionamiento de Gigglebot


```python
while True:
           
            #Leer sensores de luz 
            right=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.RIGHT)
            left=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.LEFT)
            #Leer el valor en sentimetros del sonar deifniendo los pines en que esta conectado el sonar.ping(DigitalPin.P0, DigitalPin.P0, PingUnit.MICRO_SECONDS)
            #Leer el valor en centímetros del sonar definiendo los pines en que esta conectado el sonar
            distance= sonar.ping(DigitalPin.P1, DigitalPin.P0, PingUnit.CENTIMETERS)

            
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
```
 

## Tarea 2 : 

Archivos CAD con modificaciones para uso del sonar y sensor


[![IMAGEN NOSE](Tarea 2/nose_v1 v2.stl)](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/blob/master/Tarea%202/nose_v1%20v2.stl)


<a href="https://www.imh.eus/eu" rel="some text">![Foo](https://i.imgur.com/CWoaKO0.jpg)</a>


<a href="https://www.imh.eus/eu" rel="some text">![Foo](https://i.imgur.com/cs0sJwt.jpg)</a>


Programación de Python para medir distancia de componentes con vision artificial

## Tarea 3 : 

Código de Particle para la obtención de datos por parte del sensor y su transmisión para el uso en Red Node

Archivo .JSON con flows necesarios para la visualización del Dashboard

## Tarea 4 : 

Codigo en control IO y video de funcionamiento 

<a href="https://www.loom.com/share/601ccd1b21f14bd4999cd6b41fa7456d
" rel="some text">![Foo](https://i.imgur.com/sVijgPE.jpg)</a>

## Tarea 5 :

Links para visualización de Dashboards Online en Tableau Public de datos obtenidos por los sensores 


<a href="https://public.tableau.com/profile/i.aki.rubio#!/vizhome/Tarea662/Dashboard1?publish=yes" rel="some text">![Foo](https://i.imgur.com/K68wlI8.jpg)</a>


