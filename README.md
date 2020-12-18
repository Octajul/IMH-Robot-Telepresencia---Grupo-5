


# Proyecto de Robot de Telepresencia IMH

<a href="https://www.imh.eus/eu" rel="some text">![Foo](https://media-exp1.licdn.com/dms/image/C4D0BAQFpuzjCUj95cg/company-logo_200_200/0/1579542289894?e=2159024400&v=beta&t=MqzIGMRqGZ4diQz7Y4T1qaaIh0YsdYIQdwPKU6zvWMQ)</a>


>Se llevaron a cabo 5 tareas distintas que se pueden ver en el repositorio en cada carpeta


#Integrantes: Aitor, Iñaki & Julio Gonzalez

## Tarea 1 :
[Carpeta Tarea 1](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%201)

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
[Carpeta Tarea 2](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%202)

Archivos CAD con modificaciones para uso del sonar y sensor

<a href="https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/raw/master/Tarea%202/Back%20V2.0.stl">![Foo](https://i.imgur.com/CWoaKO0.jpg)</a>


<a href="https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/raw/master/Tarea%202/UM2_nose_v1%20v4.stl">![Foo](https://i.imgur.com/UnobRzq.jpg)</a>


## Tarea 3 : 
[Carpeta Tarea 3](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%203)

Código de Particle para la obtención de datos por parte del sensor y su transmisión para el uso en Red Node

Archivo .JSON con flows necesarios para la visualización del Dashboard

En este folder está el código de Particle y los archivos JSON de RED Node con los que se han creado las pestañas Flow 1 y Flow 3
Flow 1 Es para colocar un mapa en la pestaña IMH Robot Telepresencia
Flow 3 se encarga de mostrar los datos desplegados de los sensores del robot de Telepresencia

```cpp
/ Compute heat index
// Must send in temp in Fahrenheit!
	float hi = dht.getHeatIndex();
	float dp = dht.getDewPoint();
	float k = dht.getTempKelvin();

	Serial.print("Humid: "); 
	Serial.print(h);
	Serial.print("% - ");
	Serial.print("Temp: "); 
	Serial.print(t);
	Serial.print("*C - ");
//	Serial.print(k);
//	Serial.print("*K - ");
	Serial.print("DewP: ");
	Serial.print(dp);
	Serial.print("*C - ");
//	Serial.print("HeatI: ");
//	Serial.print(hi);
//	Serial.println("*C - ");
// Lectura del pin analogico A2 donde esta conectado el microfono
    db=analogRead(A2);
// Se convierte el valor analogico en dB
    n= 20.0  * log10 (db  + 1.0);
	Serial.println(Time.timeStr());
	Particle.publish("Humedad", String(h));
	Particle.publish("Noise", String(n));
	Particle.publish("Temperatura", String(t));
	Particle.publish("TVOC", String(ccs.getTVOC()));
	delay(1000);
	Particle.publish("eCO2", String(ccs.geteCO2()));
```


## Tarea 4 : 
[Carpeta Tarea 4](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%204)

Codigo en control IO y video de funcionamiento 

<a href="https://www.loom.com/share/601ccd1b21f14bd4999cd6b41fa7456d
" rel="some text">![Foo](https://i.imgur.com/sVijgPE.jpg)</a>

## Tarea 5 :
[Carpeta Tarea 5](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%205)

Links para visualización de Dashboards Online en Tableau Public de datos obtenidos por los sensores 


<a href="https://public.tableau.com/profile/i.aki.rubio#!/vizhome/Tarea662/Dashboard1?publish=yes" rel="some text">![Foo](https://i.imgur.com/K68wlI8.jpg)</a>


