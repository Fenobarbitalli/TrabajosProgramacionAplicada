# TrabajosProgramacionAplicada
Hola mundo y hola profe

## Proyecto Reloj Inteligente

El proyecto **Reloj Inteligente**, consiste en un *reloj digital* que marca la hora y fecha, lo más impresionante del **Reloj Inteligente**, es que con un *Raspberry Pi zero w* alimentado por una batería puede durar semanas o incluso meses dando la hora, fecha y temperatura. Pero lo que más hace util este proyecto, es el hecho de poder programar la placa, para que deje de funcionar dependiendo del horario, es decir, a partir del tiempo de funcionamiento definido la placa hará el muestreo o medición necesaria en el horario programado0, haciendole totalmente util para complementar demás proyectos que requieran llevar un registro de cualquier evento por periodos de tiempo limitados, ahorrando así energía.

La idea del proyecto fue complementada con la siguiente pagina web (https://www.raspberrypi.com/news/build-low-power-clock-controlled-devices//) 
> La manera en que se haga visible la fecha, hora y temperatura, estará pendiente, pero en sus posibilidades están una pantalla LCD, OLED, o un display digital USB.

### Desarrollo del proyecto

El proyecto presentado al profesor se hará con una Raspberry Pi programada y un display que haga visible el muestreo

 Mostrar la temperatura, humedad y presión | Funcionar por un tiempo límitado 
 -|-
 BME280 es un modulo que hace posible obtener estas medidas| Para esto será necesario tener una alimentación a la placa, sea por batería o usb
 Para visualizarlo será necesario un display que registre los datos|La programación  de la placa definirá el horario en que funciones y haga su muestreo
 
 1. Materiales
    1. Sensores para hacer muestreo, por ejemplo el modulo BME280 (medidor de presión, temperatura y humedad)
    1. ds3231 (Reloj en tiempo real)
    2. Mosfet canal-P (IRF9540N)
    3. Resistencias (2.2 kΩ, 4.7 kΩ, and 220 Ω)
    4. Raspberry Pi zero W o Arduino.
    5. Protoboard, baquelita o circuito impreso para unir los componentes.
 ![Proyecto](https://www.raspberrypi.com/app/uploads/2020/04/Figure-01-Zero-MilliAmps-500x633.png)
 
 Puede utilizarse con distintos tipos de placas, microcontroladores o sistemas embebidos, pero para este proyecto se utilizara el modelo Raspberry Pi Zero w:
 
 ![Raspberry Pi 0w](https://ae01.alicdn.com/kf/H290ccd4d57ef41b6bc922f459af32bbdx/Original-Raspberry-Pi-Zero-W-Board-1GHz-CPU-512MB-RAM-with-Built-in-WI-FI-Bluetooth.jpg_Q90.jpg_.webp)

El primero modelo o Beta del proyecto es con el modulo BME280, pero la idea del proyecto es poder implementarse en el registro de cualquier medida, muestreo o registro de alguna medición física.

### Limitaciones del proyecto

* Disponibilidad de materiales
  * Conseguir un mosfet (IRF9540N), por lo cual en dado caso se podría reemplazado por un transistor BJT, pero sería reestructurando el circuito.
* Grupo de trabajo
  * Que los compañeros esten de acuerdo con el proyecto.
  * Que el profesor acepte el proyecto.
  * Que todos los integrantes participen y comprendan el proposito del proyecto.
