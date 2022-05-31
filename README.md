# Interpolacion de Lagrange (Lineal, Cuadratica, Cubica)
Integrantes: Leiner Viloria, Robert Paternina, Andres Benitez

El polinomio de interpolación de Lagrange es una reformulación del polinomio de interpolación de Newton, el método evita el cálculo de las diferencias divididas. El método tolera las diferencias entre las distancias x entre puntos.

El polinomio de Lagrange se construye a partir de las fórmulas:

![fi](https://user-images.githubusercontent.com/88936718/171045499-405487b4-b596-4e23-9d26-83efb0d1f8e3.png)

Donde una vez que se han seleccionado los puntos a usar, se generan la misma cantidad de términos que puntos.

Se empleó la programación orientada a objetos (POO) en el lenguaje Python, ya que es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.

Es muy atractivo en el campo del Desarrollo Rápido de Aplicaciones (RAD) porque ofrece tipificación dinámica y opciones de encuadernación dinámicas.

Python es relativamente simple, por lo que es fácil de aprender, ya que requiere una sintaxis única que se centra en la legibilidad. Los desarrolladores pueden leer y traducir el código Python mucho más fácilmente que otros lenguajes.

Por tanto, esto reduce el costo de mantenimiento y de desarrollo del programa porque permite que los equipos trabajen en colaboración sin barreras significativas de lenguaje y experimentación.

Además, soporta el uso de módulos y paquetes, lo que significa que los programas pueden ser diseñados en un estilo modular y el código puede ser reutilizado en varios proyectos. Una vez se ha desarrollado un módulo o paquete, se puede escalar para su uso en otros proyectos, y es fácil de importar o exportar.

![inter](https://user-images.githubusercontent.com/88936718/171045885-a38ab9c6-6bf5-47f8-b8c3-cca8aca99191.png)

Instalacion de Python

--> Entra a https://www.python.org/downloads/

Entornos donde se puede correr el programa

--> Pycharm - https://www.jetbrains.com/es-es/pycharm/download/#section=windows (Descargas la Version Community)

Si tienes un equipo de pocos recursos, intenta correr el programa en Visual Studio Code

--> VSC - https://code.visualstudio.com/download y descargas una extensión para python

Para descargar las librerias necesarias puedes irte al CMD o en Pycharm las puedes instalar, necesitas:

-> matplot

-> matplotlib

-> sympy

-> asyncio

Desde cmd puedes ir a la ruta del proyecto y escribir: pip install nombreLibreria

O, desde Pycharm:

File/Settings

![file](https://user-images.githubusercontent.com/88936718/170803338-cf056ea3-f28a-46fd-baed-f86ba725433e.png)

Project:Lagrange/Python Interpreter/+

Verificaa tener como interprete de python el ejecutable que está en \AppData\Local\Programs\Python\Python310\python.exe

![file](https://user-images.githubusercontent.com/88936718/170803380-ff743005-6a83-4181-a007-e21b775440d2.png)

Escribes el nombre de la libreria y le das instalar

![file](https://user-images.githubusercontent.com/88936718/170803412-02c23aa3-90ed-4655-842b-50f262a31c86.png)

Estando con todo listo, abres el archivo main.py y encontrarás que, las primeras 27 lineas, contienen lo siguiente:

![file](https://user-images.githubusercontent.com/88936718/171213917-19e84f3b-cb0e-4763-8e2d-1dc13d46ac50.png)

Te interesan las siguientes lineas:

![file](https://user-images.githubusercontent.com/88936718/171214241-396b7f96-c298-47c3-9bf9-dcaaee8de45c.png)

En la linea #10, te encontrarás la variable X, ahí irán los valores de X.

En la linea #17 y #18, están las variables para saber el rango en el que se evaluará el resultado final

Las otras dos lineas a las que debes poner cuidado son la linea #13 y #27, ya que si te dan una ecuacion debes dejar la Y vacia, tal como está, y debes meter una ecuación, puede ser cualquiera, donde la variable independiente es la X, ten cuidado con los parentesis, serán importantes; por otro lado, si te dan los valores de Y, debes meterlos en la linea #13, así como está en el ejemplo de la linea #14, y dejar la ecuacion=""

Debes tener en cuenta las operacione en python

![operador1](https://user-images.githubusercontent.com/88936718/171237136-f7ead323-39ad-4b13-b63e-f9fb6d6d320d.png)

![operador1](https://user-images.githubusercontent.com/88936718/171239441-2e91bf92-056b-495a-a7c6-731ddcd657bc.png)

![operador1](https://user-images.githubusercontent.com/88936718/171240897-fa9dc1f5-1169-4346-8675-97f5018a9c0f.png)

Si quieres ejecutar una interpolacion, dejas el valor de True, sino, lo cambias a False. ¡¡Con la primera letra en mayúscula!! True o False.

![file](https://user-images.githubusercontent.com/88936718/171214615-80249eea-f54a-4d37-bc9c-4e6460d0ffb4.png)

EJECUCION

--> Desde Pycharm, click derecho a main.py y le das en Run

![file](https://user-images.githubusercontent.com/88936718/170803816-bea9c20d-2341-4e1a-a74e-dbbc34c8455f.png)

Te encontrarás esto

![file](https://user-images.githubusercontent.com/88936718/171214796-cf3a34bf-7083-41e4-b01f-cf3dbbedd5ed.png)

Y te saldran las graficas (La grafica del error saldrá si tiene una ecuacion original dada en la linea #27)

![file](https://user-images.githubusercontent.com/88936718/171043664-7a6e4f05-664c-41e1-9824-38a97c09a767.png)

![fi](https://user-images.githubusercontent.com/88936718/171043721-9b75c6c9-8c07-4a47-9591-211273367a38.png)

-> Visual Studio Code (VSC)

Si tienes esta extencion, funcionará bien.

![py](https://user-images.githubusercontent.com/88936718/170803987-87147f33-86d9-4b55-ba5b-c9758aee7fd4.png)

Click derecho a main.py y le das en correr en terminal

![file](https://user-images.githubusercontent.com/88936718/170804036-0c04e87d-5a88-440d-a4ad-0e43f1771b01.png)

![file](https://user-images.githubusercontent.com/88936718/171215097-c1deeb91-926d-4103-ba48-233491b1174b.png)

Para ver las graficas, cierra la ventana que se muestre, para poder pasar a la siguiente
