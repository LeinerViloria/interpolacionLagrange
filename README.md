# Interpolacion de Lagrange (Lineal, Cuadratica, Cubica)
Integrantes: Leiner Viloria, Robert Paternina, Andres Benitez

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

![file](https://user-images.githubusercontent.com/88936718/170803380-ff743005-6a83-4181-a007-e21b775440d2.png)

Escribes el nombre de la libreria y le das instalar

![file](https://user-images.githubusercontent.com/88936718/170803412-02c23aa3-90ed-4655-842b-50f262a31c86.png)

Estando con todo listo, abres el archivo main.py y encontrarás que, las primeras 24 lineas, contienen lo siguiente:

![file](https://user-images.githubusercontent.com/88936718/170803480-9370db85-461a-45b4-947f-bbd6f48168c7.png)

Te interesan las siguientes lineas:

![file](https://user-images.githubusercontent.com/88936718/170803537-7b73d886-3074-4838-ac92-ef23c4b22a9f.png)

En la linea #9, te encontrarás la variable X, ahí irán los valores de X.
En la linea #13 y #14, están las variables para saber el rango en el que se evaluará el resultado final

Las otras dos lineas a las que debes poner cuidado son la linea #10 y #23, ya que si te dan una ecuacion debes dejar la y vacia, tal como está, y debes meter una ecuación, puede ser cualquiera, donde la variable independiente es la X, ten cuidado con los parentesis, serán importantes; por otro lado, si te dan los valores de Y, debes meterlos en la linea #10, así como está en el ejemplo de la linea #11, y dejar la ecuacion=""

Si bajas a lo ultimo, llegarás a la linea #81...

![file](https://user-images.githubusercontent.com/88936718/170803735-2abda593-d40c-412e-b320-4f40d50a157f.png)

Donde si no deseas que se calcule una interpolacion, simplemente la comentas como está en la linea #83.

EJECUCION
--> Desde Pycharm, click derecho a main.py y le das en Run

![file](https://user-images.githubusercontent.com/88936718/170803816-bea9c20d-2341-4e1a-a74e-dbbc34c8455f.png)

Te encontrarás en consola esto

![file](https://user-images.githubusercontent.com/88936718/170803879-9c61c17d-37c9-4917-b349-692707c938cd.png)

Y te saldran las graficas (La grafica del error saldrá si tiene una ecuacion original dada en la linea #23)

![inter](https://user-images.githubusercontent.com/88936718/170803905-20b645bf-7dac-4d33-b300-cfe3e3a4d25b.png)

![err](https://user-images.githubusercontent.com/88936718/170803909-59ceaec9-603b-49df-baca-5b596e7259d6.png)


-> Visual Studio Code (VSC)
Si tienes esta extencion, funcionará bien.

![py](https://user-images.githubusercontent.com/88936718/170803987-87147f33-86d9-4b55-ba5b-c9758aee7fd4.png)

Click derecho a main.py y le das en correr en terminal

![file](https://user-images.githubusercontent.com/88936718/170804036-0c04e87d-5a88-440d-a4ad-0e43f1771b01.png)

![file](https://user-images.githubusercontent.com/88936718/170804065-49639d99-ad06-4f69-9bfe-72bef8944b6f.png)



