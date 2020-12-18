


# Proyecto de Robot de Telepresencia IMH

<a href="https://www.imh.eus/eu" rel="some text">![Foo](https://media-exp1.licdn.com/dms/image/C4D0BAQFpuzjCUj95cg/company-logo_200_200/0/1579542289894?e=2159024400&v=beta&t=MqzIGMRqGZ4diQz7Y4T1qaaIh0YsdYIQdwPKU6zvWMQ)</a>


>Se llevaron a cabo 5 tareas distintas que pueden apreciarse individualmente en cada carpeta del repositorio o accediendo a ellas mediante enlaces que se facilitan a continuación. En el siguiente archivo "Readme", se resume el contenido de cada tarea y se aportan imágenes o códigos que facilitan su comprensión.

#Integrantes: Aitor, Iñaki & Julio Gonzalez.

## Tarea 1 :
[Carpeta Tarea 1](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%201)

La primera tarea está orientada a crear un código que permita el movimiento controlado del GiggleBot y le indique detenerse en el extremo de una superficie, así como evitar su caída.
En este caso, se ha optado por dirigir el robot a través de sensores de luminosidad que captan la luz emitida por un dispositivo, como podría ser el flash del teléfono móvil. Estableciendo un diferencial de 100 entre los valores recogidos por cada sensor (derecho o izquierdo), el robot distingue si debe girar a la derecha o la izquierda, o sin embargo, seguir recto si la diferencia entre valores es menor a 100.
Adicionalmente, para evitar la caída del bot, un sensor de ultrasonidos conectado al microcontrolador mide constantemente la distancia que lo separada del suelo sobre el que se mueve y cuando esta distancia supero los 15cm, el robot gira hasta que esta distancia se convierte en menor a 15cm. 
Tras esquivar la caida, el bot continúa siendo guiado a través de los sensores lumínicos.
A continuación se muestra el fragmento del código más representativo del funcionamiento del GiggleBot, que demuestra los explicado previamente:
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

Para permitir alojar el sensor AmbiMate que recoge datos de CO2 del ambiente, el archivo CAD ha sido modificado de forma que el sensor sería incorporado en su interior y conectado al microcontrolador del bot. Cabe destacar, que debido a las exigencias de funcionamiento del robot, se ha optado por recortar dos ventanas longitudinales laterales en la parte trasera, que permiten a los sensores lumínicos del bot percibir intensidad de luz.

<a href="https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/raw/master/Tarea%202/Back%20V2.0.stl">![Foo](https://i.imgur.com/CWoaKO0.jpg)</a>


En cuanto a la parte delantera (nose), se ha escogido realizar dos orificios al material que facilitan alojan el sensore de ultrasonidos de manera estética, ya que simulan los faros de un automóvil maximizando su funcionalidad.

<a href="https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/raw/master/Tarea%202/UM2_nose_v1%20v4.stl">![Foo](https://i.imgur.com/UnobRzq.jpg)</a>


## Tarea 3 : 
[Carpeta Tarea 3](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%203)

La tercera tarea alberga el código de Particle escrito en lenguaje C++ para la obtención de datos por parte del sensor y su transmisión a la placa DHT. Como se muestra en el fragmento de código a continuación, el programa recoge el dato de ruido en valor analógico y una fórmula convierte el valor recogido por el sensor alojado en el PIN2 adecibelios (dB). 

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
Además de ruido, sensores también recogen datos sobre las siguientes magnitudes que son críticas en la fabricación de componentes plásticos mediante fabricación aditiva (FDM):
-Temperatura (ºC)
-Humedad (%)
-Presencia de CO2 (PPM)
-Calidad de aire (PPM)

Para la visualización de estos valores recogidos por los sensores, el código de Particle deben ser parseado y transferido a Node-RED. Este programa permite creas pestañas que alberguen cajas preprogramadas a disposición de los usuarios. En este caso, se han creado las pestañas Flow 1 y Flow 3:
-Flow 1: Es para colocar un mapa en el dashboard "IMH Robot Telepresencia"
-Flow 3:Se encarga de mostrar los datos desplegados de los sensores del robot de Telepresencia en el dashboard mencionado. 
Todo el código de Node-RED se ha recogido en un fichero .JSON y puede apreciarse clicando en el enlace habilitado para acceder a la carpeta referente a la Tarea 3 del repositorio. 

## Tarea 4 : 
[Carpeta Tarea 4](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%204)

Para simular el proceso de distribución de los paquetes que contendrían los productos GiggleBot fabricados, se ha empelado la herramienta Factory IO. En esta, se ha escogido un escenario que clasificaría los pedidos dependiendo la altura del paquete, enviando los paquetes grandes a los contenedores de los rodillos derechos y los pequeños, sin embargo, a los contenedores del camino izquierdo. 

Es resenable, que para la programación del escenario, no se ha utilizado la plantilla estándar básica disponible, si no que se ha optado por empezar desde 0 de manera autónoma y sin hacer uso de los recursos proporcionados, otorgando mayor singularidad al funcionamiento de la aplicación. Por ejemplo, se ha creadp una memoria FiFo (First In First Out) que va registrando el tamaño de cada uno de las cajas que se desplaza hacia la plataforma giratoria y al momento de que se retira la caja de la plataforma se borra y se registra una nueva caja.

Además del código de Control IO para ejecutar el escenario en la aplicación de Factory IO, también se proporciona un enlace a LOOM que muestra no solo el esquema de automatización del escenario, si no también la ejecución de la simulación. 

<a href="https://www.loom.com/share/601ccd1b21f14bd4999cd6b41fa7456d
" rel="some text">![Foo](https://i.imgur.com/sVijgPE.jpg)</a>

## Tarea 5 :
[Carpeta Tarea 5](https://github.com/Octajul/IMH-Robot-Telepresencia---Grupo-5/tree/master/Tarea%205)

Por último, los datos del clima en Elgoibar durante el periodo de 2016-2017 también pueden graficarse y hacerse públicos para todos los usuarios registrados en Tableau Public. Esto se debe, a que este software costituye un herramienta muy eficiente tanto para la realización de hojas que serán incorporadas al dashboard, como para su transmisión a servidores Tableau en la nube. 
A continuación se muestra el dashboard creado para mostrar los datos recogidos por los sensores, que consiste a su vez en un enlace directo al dashboard público. Como se aprecia en la imagen, mediante la representación de la evolución de cada magnitud a lo largo del tiempo o la correlación entre magnitudes, se distingue la información más relevante y posibilita tomar decisiones más certeras y objetivas. 


<a href="https://public.tableau.com/views/Tarea662/Dashboard1?:showVizHome=no" rel="some text">![Foo](https://i.imgur.com/exxwFGR.jpg)</a>


