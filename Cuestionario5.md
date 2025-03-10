# CUESTIONARIO CHECKPOINT 5

###

**1.- Que es un condicional?**

Si estas incursionando en el mundo de la programación, es muy probable que te toparas muchas veces con el termino **«condicional»**. ¿qué significa este termino?

Los condicionales son estructuras fácil de entender. De hecho, los usamos constantemente en nuestra vida cotidiana

**Por ejemplo:**

_Si llueve, entonces cojo un paraguas_

Este es un caso de un condicional sencillo. Si se cumple la condición (llover) cogemos el paraguas si no, no hacemos nada.
Esto en programación lo podemos representar usando un condicional **if** (lo veremos más adelante);

_If llueve: // coger un paraguas_

Otro ejemplo de **condicional** podría ser necesitar una acción alternativa. Esta acción se ejecutará sólo si la condición no es cierta. Por ejemplo,

_Si llueve, cojo un paraguas_

_Si no, cojo una gorra_.

Este caso ademas de tener una acción si se cumple la condición, tenemos la acción de realizar si no se cumple la condición. En programación lo vamos a representar usando la condicional **if** y **else** (lo veremos más adelante);

_if llueve: // coger paraguas_

_else : // coger gorra_

En términos simples, los condicionales se utilizan para evaluar una expresión y, en función de si esa expresión es verdadera o falsa, tomar una acción u otra.

Los condicionales son fundamentales en la programación, ya que permiten que un programa tome decisiones dinámicamente en función de diferentes situaciones que puedan presentarse durante su ejecución. Podemos decir que es una herramienta poderosa que permite controlar el flujo de ejecución de un programa en función de condiciones específicas, lo que lo hace esencial para el desarrollo de aplicaciones.

**Sintaxis básicas de los condicionales:**

En la mayoría de los lenguajes de programación, la sintaxis básica de una declaración condicional sigue la estructura «si-entonces».

Un ejemplo común es la declaración **«if»** (si) en muchos lenguajes. La sintaxis de los condicionales varía un poco según el lenguaje de programación que estés utilizando, pero en general, los condicionales se escriben de la siguiente manera:

```python
if (condicion) {
    # Bloque de código si la condición es verdadera
} Else {
    # Bloque de código si la condición es falsa
}
```

Aquí, el programa evalúa la condición y ejecuta el bloque de código dentro del **«if»** si la condición es verdadera; de lo contrario, ejecuta el bloque dentro del **«else»**.

Supongamos que queremos escribir un programa que determine si una persona es mayor de edad o no. En este caso, la expresión que evaluamos es si la edad de la persona es mayor o igual a 18. La acción que realizamos si la expresión es verdadera es imprimir en pantalla un mensaje que diga "Eres mayor de edad". La acción que realizamos si la expresión es falsa es imprimir en pantalla un mensaje que diga "Eres menor de edad".

```python
var edad = 20;
if (edad >= 18) {
console.log("Eres mayor de edad");
} else {
console.log("Eres menor de edad");
}
```

En este ejemplo, la expresión que evaluamos es edad >= 18. Si la edad es mayor o igual a 18, la expresión es verdadera y se ejecuta la primera acción (imprimir en pantalla "Eres mayor de edad"). Si la edad es menor que 18, la expresión es falsa y se ejecuta la segunda acción (imprimir en pantalla "Eres menor de edad").

**Como funcionan los condicionales**

Los condicionales se componen de una expresión que se evalúa y dos acciones (una que se ejecuta si la expresión es verdadera y otra que se ejecuta si la expresión es falsa). Los condicionales son una herramienta fundamental en la programación. En términos generales, los condicionales se componen de tres partes:

- La expresión que se evalúa.
- La acción que se realiza si la expresión es verdadera.
- La acción que se realiza si la expresión es falsa.

**Tipos de condicionales:**

Existen varios tipos de condicionales que se utilizan en la programación. Algunos de los más comunes son:
El **if** es como el guardián que vigila la puerta, decidiendo si permitir o no el paso a una sección del código según una condición dada. Si esa condición no se cumple, entra en escena su compañero else, quien indica qué hacer en caso de que el **if** haya cerrado la puerta.

**if**, **elif** y **else** son los actores principales que dan vida a las ramificaciones lógicas en el mundo del desarrollo web. Con su ayuda, podemos crear programas capaces de adaptarse y tomar decisiones dinámicas según las circunstancias.

**Condicional «if»**

Es el más sencillo de los condicionales, es el más utilizado en la programacion. Es una estructura de control que ejecuta un bloque de código si dicha condición es verdadera.
Un condicional **if** en programación es como tener una llave mágica que abre puertas condicionales en el mundo del código.
Todos los lenguajes de programación cuentan con un condicional **if**

_Si pasa esto -----> haz esto_

Consideremos un escenario simple: imagina que estás creando un programa para verificar si un número es positivo o negativo. Usando un **if**, podrías decirle al programa: «Si el número es mayor que cero, imprime **‘Es positivo’**; de lo contrario, imprime **‘Es negativo’**». De esta manera, el **if** actúa como el juez digital que determina el rumbo del programa según las condiciones establecidas.

En resumen, un **if** en programación es como tener el poder de tomar decisiones en tiempo real dentro del código, es la herramienta clave para añadir inteligencia y lógica a nuestras creaciones digitales. Al dominar este concepto fundamental, los desarrolladores pueden escribir programas más funcionales, evitando errores y optimizando el rendimiento del código.

Es crucial para cualquier programador entender a fondo qué es un **«IF»** y cómo implementarlo en distintos escenarios. Al conocer su definición y ver ejemplos prácticos, se adquiere una habilidad clave para resolver problemas de manera efectiva en el desarrollo de software.

Es importante comprender que el bloque **‘IF’** puede ir acompañado por otros bloques como **‘ELSE’** y **‘ELSE IF’**, los cuales permiten manejar múltiples casos o condiciones alternativas.

En un código de programación se representa de la siguiente manera:

```python
if(condicion) {

}
```

La condición es una expresión que debe poder ser evaluada como verdadera o falsa. Si la condición es verdadera, el bloque de código dentro del condicional if se ejecuta. En caso contrario, el bloque se omite y el programa continúa con la siguiente instrucción.

**Condicional elif**

Cuando hay más de una posibilidad y la primera condición no es suficiente, elif permite plantear otra condición alternativa.
**elif:** La sentencia **elif** (abreviatura de **«else if»**) se utiliza para comprobar múltiples condiciones después de que la condición inicial en el **if** no se cumpla.

Por ejemplo:

```python
m = 6
if m > 9:
print("m es mayor que 9")
elif m == 6:
print("m es igua a 6")
```

Si la condición del **if** no se cumple, se evaluará la condición en **elif**. En este caso, al ser verdadera la condición A == 3, se ejecutará el bloque de código correspondiente.

**else:** La sentencia else se utiliza para ejecutar un bloque de código cuando ninguna de las condiciones anteriores es verdadera. Por ejemplo:

```python
	z = -4
	if z > 0
    print(«z es positivo»)

	elif z == 0:
	print(«z es cero»)

	else:
	print(«z es negativo»)
```

En este caso, al no cumplirse ninguna de las condiciones anteriores (z > 0 o z == 0), se ejecutará el bloque de código dentro del **else**.

En resumen, el uso adecuado de las sentencias **if**, **elif** y else es fundamental para controlar el flujo de un programa y ejecutar acciones basadas en condiciones específicas. Dominar estos conceptos resulta crucial para cualquier programador que busque desarrollar aplicaciones funcionales y eficientes.

**Condicional if else**

El condicional **"if else"** se utiliza para evaluar múltiples condiciones encadenadas. Si la condición del **"if"** es falsa, se evalúa la siguiente condición. Este proceso continúa hasta que se encuentra una condición verdadera o se alcanza el bloque **"else"**. El condicional **if-else** es una evolución del **if** sencillo, **if-else** permite al programador definir dos caminos posibles según una condición dada.

```Python
El condicional if-else significa,
```

Si pasa esto → haz esto
Si no → haz esto otro

```python
if(condicion)
{
 // acciones a ejecutar si condicion es true
}
else
{
 // acciones a ejecutar si condicion es false
}
```

Ejemplo, supongamos que tenemos que evaluar la nota de examen.

Si es mayor que 5, el alumno ha aprobado

Si es menor que 5, el alumno ha suspendido

Puesto en formato código, sería algo así:

```python
if (nota_examen >= 5)
{
 // mostrar mensaje '¡Enhorabuena! Has aprobado'
}
else
{
 // mostrar mensaje 'Lo siento, has suspendido'
}
```

Este otro condicional tambien es importante, no podemos dejar de mencionarlo porque seguramente lo encontraras a lo largo de tu carrera en programacion.

**Condicional switch**

El condicional **"switch"** es utilizado para realizar múltiples comparaciones sobre el valor de una expresión. Dependiendo del valor de la expresión, se ejecuta un bloque de código correspondiente.

Es una estructura de control que ofrece una alternativa al condicional **if-else** para tomar decisiones basadas en múltiples casos. En el caso de un condicional **switch** en lugar de una condición se emplea una expresión que proporciona un valor (por ejemplo, puede ser un número, o un texto). Durante la ejecución la expresión evalúa, y su valor se compara con cada uno de los posibles casos definidos. Si hay una coincidencia, se ejecuta el bloque de código correspondiente a ese caso.

El último caso default es opcional, y se ejecuta cuando la expresión no coincide con ninguno de los casos que hemos definido anteriormente.

**Sintaxis:**

```python
switch(expresion):

    case valor1:
        // código a ejecutar si la expresion es igual a valor1
        break;
    case valor2:
        // código a ejecutar si la expresion es igual a valor2
        break;

    default:
        // código a ejecutar si la expresion no
        coincide con ninguno de los casos anteriores.
```

El uso de la instrucción break después de cada bloque de código sirve para salir del condicional y evitar la ejecución de otros casos.

**Importancia de los condicionales en programación**

Los condicionales son vitales en el desarrollo de software, ya que permiten que los programas tomen decisiones y ejecuten acciones específicas según las circunstancias. Algunas de las razones por las que los condicionales son importantes en programación incluyen:

1. Lógica de control
   Los condicionales proporcionan la capacidad de controlar el flujo de un programa, lo que permite que la lógica se adapte a diferentes situaciones. Esto es fundamental para crear programas dinámicos y eficientes.

2. Respuesta a eventos
   Los condicionales son esenciales para responder a eventos o condiciones específicas dentro de un programa. Por ejemplo, un programa puede utilizar un condicional para manejar diferentes tipos de entrada del usuario.

3. Personalización del comportamiento
   Mediante el uso de condicionales, los desarrolladores pueden personalizar el comportamiento de un programa en función de diversas variables, como el estado del sistema, la entrada del usuario o datos externos.

4. Optimización del rendimiento
   Los condicionales también desempeñan un papel crucial en la optimización del rendimiento de un programa, ya que permiten la ejecución selectiva de bloques de código según las necesidades.

**2.- ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?**

Los bucles (loop en inglés) son una herramienta que nos permite repetir un bloque de código varias veces mientras se cumpla una condicion. Junto con los condicionales, son dos las herramientas más importantes a la hora de programar, ambas modifican el flujo del programa en función de una condición.

Entender un bucle no es mucho más difícil que entender un condicional. De hecho, realizar bucles de acciones (tareas repetitivas) también es algo que hacemos en nuestra vida cotidiana con frecuencia.

**Por ejemplo**, imaginemos que tienes que hacer esto:

- Tengo que poner un sello a cada carta de este montón, esto básicamente significa:
- Coge una carta, ponle un sello mientras queden cartas en el montón, repite la misma secuencia de acciones.

Los bucles en Python sirven para automatizar la ejecución del código, procesar un conjunto de datos o realizar cálculos iterativos, en este lenguaje se realiza de forma secuencial, es decir sigue un orden lineal.

En ocasiones es necesario alterar en flujo del programa con los tipos **while** y **for**. Entraremos en detalles sobre qué son y sus funciones.

En Python, contamos con dos tipos principales de bucles: **for** y **while** se utilizan según las necesidades del programador. Cada uno de los bucles tiene su función dentro de la ejecución del código en Python y una sintaxis para crearlos, que es lo que descubrirás a continuación.

**_BUCLE for_**

El bucle **for** (para) se utiliza para iterar (realizar una acción varias veces) sobre una secuencia (como una lista, tupla, diccionario, etc.) y ejecutar un bloque de código para cada elemento en esa secuencia. Se utiliza la palabra clave **«for»**, seguida de una variable temporal que tomará el valor de cada elemento en cada iteración, la palabra clave **«in»**, y la secuencia de elementos a recorrer de manera ordenada.

Este bucle se utiliza cuando se conoce el número exacto de iteraciones que se deben realizar. La iteración depende de la cantidad de objetos recogidos en las líneas y que finalizará cuando se completen todos los valore de la lista.

_La sintaxis básica del bucle for es la siguiente:_

```python
for  elemento in secuencia:
    // bloque de código a ejecutar para cada elemento
```

Ejemplos bucle **for**:

- Iterar sobre una colección

Por ejemplo, podemos utilizar un **for** para imprimir cada elemento de una lista:

```python
frutas = ["higos", "naranja", "mandarina"]

for fruta in frutas:
   print(fruta)
```

En este caso, el bucle for recorre la lista frutas y en cada iteración, asigna el valor del elemento actual a la variable fruta, la cual es luego impresa. La salida será:

higos, naranja, mandarina

- Iterar un numero de veces

También podemos utilizar el bucle **for** para realizar una serie de iteraciones específicas, por ejemplo, un número de veces fijo. Esto se logra utilizando la función range(), que genera una secuencia de números en un rango dado.

_Ejemplo de bucle for con range(5)_

```
for i in range(5):
    print(i)
```

En este ejemplo, range(5) genera una secuencia de números desde 0 hasta 4 (excluyendo el 5), y el bucle for itera sobre cada uno de estos números, asignándolos a la variable i en cada iteración.

Luego, se imprime el valor de i,

resultando en la salida: 0, 1, 2, 3, 4

Al combinar range() con un bucle **for**, podemos iterar sobre esta secuencia y ejecutar un bloque de código una cantidad predeterminada de veces.

- Iterar sobre una cadena de texto

Además de iterar sobre listas y otras secuencias, el bucle **for** en Python puede utilizarse para iterar sobre otros tipos de datos, como cadenas de texto. Esto es así porque una cadena de texto es una colección de caracteres.

Cuando utilizamos un bucle **for** con una cadena de texto, cada iteración del bucle recorrerá los caracteres individuales de la cadena, permitiéndonos procesar o manipular cada uno de ellos según sea necesario.

_Ejemplo de bucle for con una cadena de texto_

```
for letra in "Python":
    print(letra)
```

En este caso, el bucle **for** itera sobre cada carácter de la cadena de texto "Python". En cada iteración, el valor del carácter actual se asigna a la variable letra, que luego se imprime.  
La salida será:
P
y
t
h
o
n

**_BUCLE while_**

El bucle **while** es uno de los primeros bucles que probablemente encontrarás cuando empieces a aprender a programar. Podría decirse que también es uno de los más intuitivos de entender: si piensas en el nombre de este bucle, comprenderás rápidamente que la palabra **"while"** tiene que ver con un _"intervalo"_ o un _"periodo de tiempo"_. Como ya sabrás a estas alturas, la palabra **"bucle"** se refiere a un trozo de código que se ejecuta repetidamente.

Con todo esto en mente, puedes entender fácilmente la siguiente definición del bucle while:

El bucle **while** es idóneo cuando no se conoce el número exacto de iteraciones que se van a realizar, pero se tiene una condición que determina cuándo se debe detener la repetición. Para escribir la sintaxis del código, es imprescindible verificar la expresión, porque es la clave para verificar la condición verdadera o falsa, es decir una condición _boleana_.

Tres componentes que necesitas para construir el bucle **while** en Python:

- La palabra clave while;
- Una afección que se transmite a True o False;
- Un bloque de código que quieres ejecutar repetidamente.

La sintaxis básica del bucle **while** es la siguiente:

```
while condición:
   bloque de código a ejecutar mientras la condición sea verdadera
```

**Ejemplo:**

```python
numero = 2
Condicion bucle while

while numero<5 :
print("thank you")

Incremento valor de la variable "numero en 1"
numero = numero +1

thank you
thank you
thank you
```

El ejemplo anterior es un poco básico, ahora veremos el uso de bucle **while** con las condicional **if** ya mencionada anteriormente:

```python
numero= 2
#Condicion del bucle while

while numero< 5 :
#Encuentra el modulo de 2

if number%2== 0:
print("el numero"+str(numero)+ "es par")

else:
      print("el numero"+str(numero)+ "es impar")

#Incrementa numero en 1
 numero = numero+1

el numero 2 es par
el numero 3 es impar
el numero 4 es par
```

**_BUCLES anidados_**

En Python también es posible tener bucles dentro de otros bucles, lo que se conoce como bucles anidados.
En Python pueden programarse bucles aislados o estos loops pueden formar parte de sentencias de otros bloques, convirtiéndose en bucles anidados, creando una especie de muñeca rusa. En los bucles anidados encontrarás los bucles externos e internos.

_¿Para qué se usan los bucles anidados?_ Puede darse el caso de desarrollar un programa complejo con numerosas tangentes que deben controlarse a través de este recurso. Estos bloques mantienen un orden que evitan variables indeseadas.

Ejemplo:

```python
Bucle while anidado

numero = 2
#Condicion del bucle while

   while numero < 5 :
#Condicion del bucle while anidado

   while numero % 2 == 0:
        print("el numero "+ str(numero)+"es par")
```

El bucle **while** esta anidado dentro del bucle exterior, este bucle interior pone otra comprobación para ver si el numero % 2 es 0, es decir comprueba si el numero es par e imprime la afirmación _«el numero es par»_.

**_SENTENCIAS break y continue_**

Es importante tener en cuenta que, tanto en el bucle **for** como en el bucle **while**, se pueden utilizar las palabras clave **break** y **continue** para controlar el flujo de ejecución del bucle. La palabra clave **break** se utiliza para salir del bucle por completo, mientras que la palabra clave **continue** se utiliza para saltar a la siguiente iteración sin ejecutar el resto del código dentro del bloque.
Puedes utilizar **break** y **continue** en cualquier bucle que crees.

```python
frutas = ["manzana", "banana", "cereza", "sandía", "uva"]
for fruta in frutas:
     print(fruta)

     if fruta == "sandía":
        break
```

En este caso, el bucle **for** imprimirá cada fruta de la lista hasta que llegue a _“sandía”_, momento en el cual se ejecutará **break** y el bucle se interrumpirá.
Por otro lado, el **continue** nos permite saltar a la siguiente iteración sin ejecutar el resto del bloque de código para esa iteración.

Veamos un ejemplo:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
```

En este ejemplo, el bucle **for** itera sobre los números en la lista numeros. Cuando encuentra un número par (divisible por 2), se ejecuta **continue**, lo que significa que el print(numero) no se ejecuta para ese número y se salta a la siguiente iteración.

En determinadas ocasiones **break** y **continue** pueden ayudar a mejorar la legibilidad del código. Pero, en general, no conviene abusar de ellos porque dificultan seguir el flujo de código.

**_BUCLE con else_**

En Python, los bucles también pueden tener una cláusula **else**, que se ejecuta cuando el bucle termina sin haber sido interrumpido por un **break**.

Ejemplo:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
   if numero = = 0:
   break
else:
   print("El bucle ha terminado sin encontrar el número 0")
```

En este caso, como no hay ningún 0 en la lista numeros, el bucle se ejecutará completamente y al final se imprimirá “El bucle ha terminado sin encontrar el número 0”.

**Recomendaciones en el uso de bucles**

Para evitar que un bucle se ejecute infinitamente en Python, puedes utilizar una condición de salida dentro del bucle. De esta manera, el bucle se seguirá ejecutando siempre y cuando la condición sea verdadera, pero se detendrá cuando la condición sea falsa. Esto asegurará que el bucle tenga un fin y evite la ejecución infinita.

Es importante entender completamente las diferencias entre los distintos tipos de bucles y saber cuál es el más adecuado para cada situación.

Los bucles **for** son ideales cuando se necesita iterar sobre una secuencia o colección de elementos conocida, como listas o cadenas de texto. Por otro lado, los bucles **while** son útiles cuando se desea repetir una acción hasta que se cumpla una condición específica.

Es recomendable utilizar variables de control claras y descriptivas para facilitar la comprensión del código por parte de otros programadores y para reducir posibles errores.

Es una buena práctica usar los bucles con moderación cuando sea posible. A veces, se pueden encontrar soluciones más eficientes y elegantes utilizando otras estructuras de control, como comprensiones de listas, funciones incorporadas de Python.

_En resumen, es muy importante recordar:_

- El bucle **for** se utiliza cuando se conoce de antemano la cantidad de veces que se repetirá una acción. Se específica un rango o una secuencia a recorrer, y el bucle se ejecuta para cada elemento de ese rango o secuencia.

- El bucle **while** se utiliza cuando se repite una acción mientras se cumpla una condición específica. La condición se evalúa al comienzo de cada iteración, y si se cumple, el bucle sigue ejecutándose. Si en algún momento la condición deja de cumplirse, el bucle se detiene.

- Por lo tanto, el bucle **for** es ideal cuando se sabe cuántas veces se debe repetir una acción, mientras que el bucle **while** es más adecuado cuando se necesita repetir una acción hasta que se cumpla una condición determinada.

**3.- ¿Qué es una lista por comprensión en Python?**

En Python, las **listas por comprensión** son una forma concisa de crear listas a partir de otras listas, iterables o rangos. Se pueden utilizar para crear listas de números, cadenas, objetos o cualquier otro tipo de dato.

Las **listas por comprensión** son otra de las herramientas disponibles en Python que permite crear código compacto y elegante. Usar esta técnica puede simplificar nuestro código en el contexto de la Informática.

La sintaxis básica para crear una lista por comprensión es la siguiente:

```python
nueva_lista = [expresion for elemento in lista  if condicion]
```

_En donde:_

- nueva_lista: es la lista generada.

* expresion: es una operación o función que se aplica a cada elemento de la lista original.

- elemento: es cada uno de los elementos de la lista original.

* lista: es la lista original.

- condicion: es una condición opcional que filtra los elementos antes de aplicar la expresión.

En resumen, una **lista por comprensión** nos permite generar rápidamente una nueva lista aplicando operaciones y filtros a una lista original o a cualquier otro tipo de iterable.

Es importante destacar que las **listas por comprensión** no son exclusivas de Python, pero suelen ser muy utilizadas debido a su simplicidad y legibilidad en el código.

**_Por ejemplo_**, si queremos crear una lista con los cuadrados de los números del 1 al 5, podemos hacerlo de la siguiente manera:

```python
cuadrados = [num**2 for num in range(1, 6)]
```

En este caso, la variable "num" toma el valor de cada elemento del rango (del 1 al 5) y se eleva al cuadrado.

El resultado es una nueva lista que contiene [1, 4, 9, 16, 25].

Además de simplificar el código, las **listas por comprensión** también pueden incluir condiciones para filtrar elementos. Por ejemplo, si solo queremos los números pares de una lista, podemos hacer lo siguiente:

```python
numeros_pares = [num for num in lista if num%2 == 0]
```

Aquí, la condición "num%2 == 0" verifica si el número es par antes de agregarlo a la lista resultante.

```python
numeros = [1, 2, 3, 4, 5]
doble = [num * 2 for num in numeros if num % 2 == 0]
```

En este ejemplo, se genera una nueva lista llamada "doble" que contiene el doble de los números pares de la lista original "numeros". La condición `if num % 2 == 0` filtra solo los números pares.

- Creacion de una lista de numeros:

```python
  numeros= [1, 2, 3, 4, 5]
```

- Creación de una nueva lista con los cuadrados de los números de la lista original

```python
cuadrados = [x * x for x in numeros]

print(cuadrados)
Salida:
[1, 4, 9, 16, 25]
```

- Creacion de una lista de cadenas

```Python
cadenas = ["Hola", "mundo", "Python"]
#Creación de una nueva lista con las cadenas de la lista original en mayúsculas

mayusculas = [cadena.upper() for cadena in cadenas]

print(mayusculas)
Salida:
['HOLA', 'MUNDO', 'PYTHON']
```

- Filtrado de elementos

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Creación de una nueva lista con los números pares de la lista original

pares = [x for x in numeros if x % 2 == 0]

print(pares)
Salida:
[2, 4, 6, 8]
```

- Combinacion de listas

```Python
numeros = [1, 2, 3, 4, 5]
cadenas = ["Hola", "mundo", "Python"]
#Creación de una nueva lista con los números y las cadenas de la lista original
combinacion= [x for x in numeros] + [x for x in cadenas]

print(combinacion)
Salida:
[1, 2, 3, 4, 5, 'Hola', 'mundo', 'Python']
```

**Condiciones en las listas por comprensión**

Es posible añadir condiciones a las listas por comprensión en Python. Para lo que se tiene que agregar un **if** al final con la condición. Siguiendo con el ejemplo anterior, se podría sumar uno solamente a los registros que sean menores que tres.

```Python
numbers= [1, 2, 3, 4]
result = [n + 1 for n in numbers if n<3]
results
[2, 3]
```

Al ejecutar el código se puede observar que solamente se tienen dos registros, los que cumple la condición. En el caso de que se desee realizar una operación diferente cuando no se cumple la condición se puede hacer con un **else**. Aunque es necesario cambiar modificar el orden. Si se utiliza un **else** la condición se tiene que situar justamente después de la expresión y antes del **for**.

Por ejemplo, en el siguiente código los números mayores o iguales que 3 se dejan sin modificar.

```Python
numbers = [1, 2, 3, 4]
results = [n + 1 if n < 3 else n for n in numbers]
results
[2, 3, 3, 4]
```

**Identificar los numero comunes en dos listas**

La posibilidad de anidar bucles **for** en las listas por comprensión permiten realizar operaciones realmente completadas. Así se puede iterar sobre varios objetos iterables para aplicar una condición.

Un ejemplo típico de esto es buscar el conjunto de elementos comunes en dos listas. Lo que se puede conseguir con el siguiente código.

```Python
names_1 = ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy']
names_2 = ['Jayson', 'Oralie' ,'Michele', 'Stevy', 'Alwyn']

common = [a for a in names_1 for b in names_2 if a == b]
common

['Oralie', 'Michele', 'Stevy']
```

En donde se selecciona el valor de la primera lista si al iterar sobre la segunda también se encuentra en esta. Si no aparece el registro de ignorará. Para hacer esto mismo con un bucle **for** tradicional es necesario escribir mucho más código.

```Python
list_a = ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy']
list_b = ['Jayson', 'Oralie' ,'Michele', 'Stevy', 'Alwyn']
common = [ ]

for a in names_1:
 	for b in names_2:
       	       if a = = b:
           	common.append(a)
```

**Ventajas**

Las listas por comprensión ofrecen una serie de ventajas sobre las formas tradicionales de crear listas:

- Son más concisas y fáciles de leer.

* Permiten crear listas de forma más eficiente.

- Son más flexibles y permiten crear listas con condiciones y operaciones complejas.

**Desventajas**

- Las listas por comprensión pueden ser difíciles de entender para los principiantes.

* Además pueden ser menos eficientes que las formas tradicionales de crear listas en algunos casos.

**Conclusión**

Las listas por comprensión son una herramienta poderosa que puede utilizarse para crear listas de forma concisa y eficiente. Son una parte esencial de la sintaxis de Python y son utilizadas por desarrolladores experimentados en todo el mundo.

**4.- ¿Qué es un argumento en Python?**

Un argumento en Python es un valor que se pasa a una función cuando se llama. Estos valores permiten que la función realice cálculos o procesos personalizados según los datos proporcionados.

Ejemplo básico en Python:

```Python
def saludo(nombre):
    print("Hola,", nombre)
saludo(«Sara») # Se pasa «Sara» como argumento

('Hola, Sara')
```

Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como **args** (arguments) y **kwargs** (keyword arguments), respectivamente, lo que equivaldría a «argumentos de palabras clave.

**Paso de argumentos por posición**

En el caso de que una función tenga parámetros, una forma de utilizarlos es considerando su posición

```Python
def suma(a,b):
resultado = a+b
return resultado
print(suma(5,6))
```

En el ejemplo anterior, la función suma requiere dos parámetros (a, b). Cuando es llamada, print (suma(5,6)), los argumentos leídos en el orden en que son pasados. En el ejemplo anterior a tomará el valor de 5, y b el valor de 6.

**Paso de argumentos por nombre**

En Python no es necesario escribir los argumentos en el orden en que la función define sus parámetros. Podemos especificar el nombre del parámetro y de esa manera escribir los argumentos en cualquier orden.

```Python
def restar (actual, nacimiento):
 	   resultado = actual - nacimiento
 	   return resultado

edad_erronea = restar(1990,2020)
edad = restar(nacimiento=1990, actual=2020)
print (edad_erronea)
print (edad)
```

En el ejemplo anterior podemos llamar la función restar pasándole como argumentos 1990 y 2020. Por default copiará el valor 1990 al parámetro actual y el valor 2020 al parámetro nacimiento. Pero podemos pasar los argumentos por nombre:

```Python
edad = restar (nacimiento=1990, actual= 2020)
```

y poner los argumentos en cualquier orden.

**Argumentos por default**

En Python también podemos especificar argumentos por default, de modo que, aunque no se pase el valor correspondiente, la función la asume por default.

Por ejemplo:

```Python
def dividir (dividendo, divisor=2):
   resultado= dividendo/divisor

   return resultado

cuarto= dividir(40,4)
mitad= dividir(40)
print (cuarto,mitad)
```

En la función anterior se define un parámetro por default, divisor=2. Es posible llamar a la función pasándole los dos parámetros:

cuarto = dividir(40,4)

o pasando solamente uno:

mitad = dividir(40)

En éste último caso no hay error, porque fue especificado el parámetro divisor, y lo asume por default.

**Argumentos indeterminados en Python**

Una función puede utilizar parámetros indeterminados. Python utiliza la expresión **\*args** para indicar una serie de argumentos indeterminados.

```Python
def sumarx(*args):
 	resultado = 0
 	for valor in args:
  		    resultado = resultado + valor
 return resultado

total = sumarx(4,3,6,2,6)
print (total)
```

En la función anterior, es posible invocar a sumar **x** con la cantidad de datos que nosotros queramos.

```Python
total = sumarx(4,3,6,2,6)
```

o bien

```Python
total = sumarx(4,3,5)
```

Cualquiera de las dos formas será correcta, pues la función está programada para recorrer utilizando un **for** todos los argumentos (valores) pasados (**for** valor in **\*args**)

Para que una función tome una cantidad indefinida de argumentos, se utiliza la expresión **\*args**.

```Python
def f(*args):
         Return args
F(1, 5, True, False, ‹Hello, world!»)
(1, 5, True, False, ‹Hello, world!»)
```

En este caso, **args** es una tupla que contiene todos los valores que se han pasado a la función. El signo asterisco (\*) es utilizado para indicar dicha funcionalidad; de lo contrario, únicamente el primer argumento sería almacenado en **args**.

Dado que todos los valores serán guardados en el primer parámetro (**args**), todo argumento posterior necesariamente se convierte en un argumento clave-valor:

```Python
def f(*args, b):
   return args, b
#b solo puede especificarse a través del nombre.

f(1, 2, b=3)
((1, 2), 3)
```

**Argumentos en funciones (\*args y \*\*kwargs)**

De forma análoga funcionan los **keyword** arguments, que son representados con dos asteriscos (\*\*) y el nombre **kwargs**. Cabe destacar que los nombres de estos parámetros son indiferentes; **args** y **kwargs** son utilizados simplemente por convención.

```Python
 def f(**kwargs):
     return kwargs

    f(a=1, b=True, h=50, z="Hello, world!")
{'a': 1, 'h': 50, 'b': True, 'z': 'Hello, world!'}
```

En este caso **kwargs** es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. Siendo esto así, el orden de los mismos es indistinto.

Ambos métodos pueden ser implementados en una misma función como excepción al error de sintaxis.

```Python
    def f(*args, **kwargs):
     return args, kwargs

args, kwargs= f(True, False, 3.5, message ="Hello, world!", year=2014)
    args
(True, False, 3.5)
    kwargs
{'message': 'Hello, world!', 'year': 2014}
```

Los signos \* y \*\* pueden también ser utilizados para almacenar argumentos en un objeto para ser pasados luego a una función.

```Python
def f(a, b, c):
    return a*b**c
```

Cuando en una función uno de sus argumentos lleva un valor por defecto, este se convierte automáticamente en un keyword argument o argumento clave-valor, tal como un diccionario. Por lo tanto, pueden ser especificados indicando su nombre al momento de invocarlos.

h(1, c=10)

Y viceversa, por lo que ambos ejemplos a continuación resultan en lo mismo.

h(1, b=5)

h(1, 5)

Los argumentos pueden llevar cualquier valor por defecto, incluyendo None y llamadas a otras funciones.

```Python
def a (c=none) :
return 100
```

**Importancia**

- Reutilización de código: Permiten que las funciones sean flexibles y reutilizables.

* Menos repetición: Evitan escribir múltiples versiones de una función con diferentes valores.

- Mayor claridad: Los argumentos bien definidos hacen que el código sea más legible.

**Conclusión**

Los argumentos son un concepto clave en la programación, ya que permiten que las funciones sean más dinámicas y adaptables. Comprender sus tipos y usos facilita la escritura de código eficiente y reutilizable.

**5.- ¿Qué es una función Lambda en Python?**

Las funciones **lambda**, también conocidas como funciones anónimas,también como arrow functions, son una forma alternativa, concisa y expresiva de definir funciones.
Son herramientas potentes y concisas para crear pequeñas funciones anónimas sobre la marcha.

Las funciones **lambda** difieren de las funciones estándar de Python en varios aspectos clave. Son expresiones anónimas, lo que significa que no tienen nombre ya que estas son anónimas por definición a menos que se asignen explícitamente a una variable. También son más concisos y se definen en una sola línea sin necesidad de una declaración return. Esto las hace ideales para operaciones sencillas de una sola vez y para utilizarlas como argumentos de una función de orden superior como lo son **map**, **filter** y **sorted**.

En general, son funciones pequeñas y se emplean en contextos donde se necesita una función de forma temporal y pequeña sin necesidad de definirla usando la palabra clave **def** , las funciones **lambda** se crean usando la palabra clave **lambda**.

_Una función anónima es aquella que definimos sin un nombre específico. Es decir, a diferencia de las funciones regulares, no se definen con una declaración completa y no requieren un identificador_.

La principal ventaja de las funciones lambda es su capacidad para ser creadas y utilizadas de forma inmediata.

**Sintaxis de una función lambda**

La sintaxis básica de una función **lambda** se ve así:

_ambda argumentos: expresion_

Aquí, **lambda** es la palabra clave, **arguments** son los parámetros de entrada de la función, y **expression** es la operación que realiza la función.

Por ejemplo, podemos definir una función **lambda** que calcule el cuadrado de un número de la siguiente forma:

```Python
suma = lambda x: x * x
```

Esta función lambda:

- Toma un argumento x
- Retorna el resultado de x \* x.

**Funciones lamba con múltiples argumentos**

En este ejemplo, suma es una función lambda que toma dos argumentos **x** e **y** y devuelve la suma de ambos.

**Sintaxis: **

```Python
lambda argumentos: expresión

suma = lambda x, y: x + y
print(suma(3, 5))  # Output: 8
```

Despues de la palabra clave lambda se enumeran los argumentos de entrada **x** e **y**, despues de los dos puntos, se especifica la expresión cuyo resultado se devolverá, **x** + **y**

_Ejemplo del cuadrado de una función lambda_:

```Python
def cuadrado(x):
     return x ** 2

cuadrado = lambda x: x ** 2

 print(cuadrado(3))
9

print(cuadrado(5))
25
```

Por ejemplo, supongamos que quieres comprobar si un número entero distinto de cero es par. Podrías escribir una función estándar de Python, pero se puede conseguir la misma funcionalidad con una función **lambda** concisa de una sola línea asignada a una variable:

```python
 is_even = lambda x: x % 2 == 0.
```

Aquí, la función **lambda** de la parte derecha de la asignación toma una entrada **x** y devuelve **True** si **x** es par (es decir, si el resto al dividirlo por 2 es 0).
A esta función **lambda** se asigna a la variable **is_even**, lo que permite llamarla como a una función normal.

Por ejemplo:

```python
is_even(5) (devuelve False) y is_even(678432)
(devuelve True).
```

**Usos comunes de funciones lambda: map(), filter() y reduce()**

Las funciones **lambda** se utilizan a menudo en programación funcional sobre todo con funciones como **filter()**, **map()** y **reduce()** que toman otras funciones como argumentos para procesar elementos de una colección.

**_Función lambda con filter()_**

- Filtrar los numeros pares de la lista.

```python
#Uso de filter con la función lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(list(pares))

[2, 4, 6, 8]
```

En este código, empezamos definiendo un conjunto de numeros. A continuación, creamos una función **lambda** para comprobar si un número es par. La función **filter** aplica esta función **lambda** al conjunto numeros. A continuación, imprimimos la lista de números pares identificados por la función **filter**.

**_Función lambda con map()_**

Podemos utilizar la función **map** para aplicar una **lambda** a una colección de elementos.

**Ejemplos:**

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados)) # Salida: [1, 4, 9, 16, 25]
```

En este ejemplo, hemos definido una lista de números y luego usamos la función **map()** junto con una función **lambda** para calcular los cuadrados de los números en la lista. La función **map()** aplica la función **lambda** a cada elemento de la lista numeros, y convertimos el resultado en una lista con _list()_.  
Como resultado, obtenemos una lista de los cuadrados de los números en [1, 4, 9, 16, 25] .

La cosa se vuelve todavía más interesante cuando, en lugar de una lista de valores, pasamos como segundo parámetro una lista de funciones:

```python
enteros = [1, 2, 4, 7]
def cuadrado(x):
 return x ** 2

def cubo(x):
 return x ** 3

funciones = [cuadrado, cubo]
for e in enteros:
 valores = list(map(lambda x : x(e), funciones))
 print(valores)

[1, 1]
[4, 8]
[16, 64]
[49, 343]
```

**_Función lambda con reduce()_**

Esta función se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.

En este caso, la función que se pasa como primer parámetro recibe dos argumentos, imaginemos que queremos obtener el resultado de sumar todos los elementos de una lista, como en las veces anteriores, la suma la podemos calcular de la siguiente manera:

```python
valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el

print(suma)
21

Usando la función reduce() en combinación con una función lambda:
from functools import reduce
suma = reduce(lambda x, y: x + y, valores)

print(suma)
21
```

**En resumen:**

Las funciones **lambda** son útiles cuando necesitamos una función rápida para realizar una operación simple. Se suelen utilizar en combinación con funciones de orden superior, como **map()**, **filter()**, y **reduce()**.

- _Limitaciones de la Sintaxis:_ Las funciones lambda están limitadas a una sola expresión y no pueden contener múltiples declaraciones o líneas de código.

* _Legibilidad:_ Las funciones lambda pueden afectar la legibilidad del código si se utilizan en exceso o en situaciones complicadas.

- _Debugging:_ Puede ser más difícil depurar funciones lambda en comparación con funciones con nombres explícitos.

**6.- Que es un paquete pip ? **

Python es uno de los lenguajes de programación más populares en el mundo, en gran parte gracias a su amplia biblioteca estándar y a su ecosistema de paquetes. Para gestionar estos paquetes, Python cuenta con una herramienta poderosa llamada **pip**.

**pip** es un administrador de paquetes que facilita la instalación, actualización, gestión de bibliotecas y módulos de Python de manera sencilla. Es una herramienta esencial para cualquier desarrollador que trabaje con Python, ya que simplifica en gran medida el proceso de incorporar bibliotecas externas a tus proyectos.
Su nombre proviene de _“Pip Installs Packages”_ o _“Pip Instala Paquetes”_ en español.

![](https://ilinuxgeek.com/storage/img/images/how-to-install-python-pip-for-python-packages_6.png)

Una ventaja importante de **pip** es la facilidad de su interfaz de línea de comandos, el cual permite instalar paquetes de software de Python fácilmente desde solo una orden, El sistema de gestión se asegura de que todas las dependencias se instalan correctamente y siempre mantiene todo actualizado. Además, **pip** tiene una gran cantidad de paquetes disponibles, por lo que siempre puede encontrar lo que necesita.

![](https://helpdeskgeek.com/wp-content/pictures/2020/02/macOS-brew-Python.png)

**pip** es fácil de instalar. Para aquellos que ya tienen Python instalado en sus máquinas, **pip** ya debería estar allí. Para asegurarse de que está instalado, simplemente abra una ventana de terminal y escriba _“pip help”_. Si aparece información en la pantalla, ¡ya está listo para comenzar! Si no, puede instalar Pip escribiendo _“sudo easy_install pip”_ en su terminal.

![](https://www.aplicativosandroid.com/wp-content/uploads/2022/09/1663002928_518_Como-instalar-o-PIP-Python-em-um-PC-com-Windows.png)

_Como instalar pip en windows:_

Descargamos el **get-pip.py** y lo ejecutamos con Python:
python **get-pip.py**

![](https://bobbyhadz.com/images/blog/python-no-module-named-pip/python-get-pip-py-install.webp)

_Como instalar pip en Linux o MacOs:_

![](https://wowgold-seller.com/f/5b434f57cb38dd34376efb7743898928.png)

Una vez que **pip** está instalado, podemos utilizarlo para buscar y descargar paquetes de software verificados por la comunidad de Python. Por ejemplo, si queremos instalar una biblioteca popular como NumPy, todo lo que tenemos que hacer es escribir **“pip install numpy”** en nuestra terminal y **pip** se encargará del resto. **pip** descargará e instalará NumPy, con todas sus dependencias en cuestión de minutos.

![](https://miro.medium.com/max/1400/1*XDCIGOERuuHwPeZw7rIgpg.png)

Al igual que con todo en Python, **pip** tiene su documentación disponible. Algunos paquetes pueden tener requisitos específicos. En los casos en los que se encuentran requisitos específicos,**pip** también los maneja.

La sintaxis para instalar un paquete y sus requisitos específicos es la siguiente:

**pip install package_name[package_reqs]**

Los paquetes que ya están instalados también se pueden actualizar fácilmente con **pip**. Asegúrate de tener la última versión del **pip** instalada antes de ejecutar este comando.

![](https://www.programmingfunda.com/wp-content/uploads/2024/04/python-PIP-package-installation.png)

Actualizar todos los paquetes que tengas instalados es tan simple como escribir:

**pip freeze –local | grep –v ‘^\-e’ | cut –d = -f 1 | xargs pip install -U**

```
Los paquetes son colecciones de módulos y funciones que pueden ser distribuidos y utilizados por otros programadores.
```

Una característica particular de **pip** es que permite gestionar listas de paquetes y sus números de versión correspondientes a través de un archivo de requisitos. Esto nos permite una recreación eficaz de un conjunto de paquetes en un entorno separado (p. ej. otro ordenador) o entorno virtual. Esto se puede conseguir con un archivo correctamente formateado requisitos.txt y la siguiente orden:

_pip install -r requisito.txt_

Con **pip** es posible instalar un paquete para una versión concreta de Python, sólo es necesario reemplazar **${versión}** por la versión de Python que queramos: 2, 3, 3.4, etc:

_pip ${version} install nombre-paquete_

**pip** instalará la versión exacta del paquete que especificamos. Si en algún momento necesitas actualizar este paquete a una versión más reciente, simplemente ejecutas:

_pip install requests --upgrade_

![](https://i.ytimg.com/vi/EfGy389Xct8/maxresdefault.jpg)

Además de actualizar un paquete específico, podemos actualizar todos los paquetes instalados a sus últimas versiones usando la opción --upgrade:

_pip install --upgrade pip _

![](https://media.geeksforgeeks.org/wp-content/uploads/20220124142928/pipupgradelinux.png)

Pero **pip** hace más que simplemente instalar paquetes, también nos permite administrar nuestras dependencias. Por ejemplo, si estamos trabajando en un proyecto que depende de NumPy y SciPy, podemos agregar ambos paquetes a un archivo _requirements.txt_. Luego, si alguien más clona nuestro proyecto, puede simplemente instalar todas las dependencias del mismo tiempo escribiendo:

_pip install -r requirements.txt._

Este comando nos permite instalar todas las dependencias listadas en el archivo _requirements.txt_ de una sola vez, asegurando que todos los desarrolladores están utilizando las mismas versiones de las librerías. Esto instalará los paquetes Flask, requests y numpy con las versiones especificadas en el archivo.

![](https://media.geeksforgeeks.org/wp-content/uploads/20221016155103/1-1024x452.JPG)

En resumen, el uso de **pip** y la creación de un archivo _requirements.txt_ nos permite gestionar de manera eficiente las dependencias de nuestro proyecto en Python. Es una práctica muy útil para cualquier proyecto de software en Python y es recomendable incluirla en el flujo de trabajo del equipo de desarrollo.

**pip** no siempre es perfecto. Puede haber ocasiones en las que dos paquetes de software diferentes necesiten versiones diferentes de la misma dependencia, lo que puede causar conflictos,**pip** nos ofrece opciones avanzadas como la creación de ambientes virtuales y el manejo de paquetes privados, el cual podemos especificar las versiones de los paquetes que necesitamos para cada proyecto.

Una de las principales ventajas de trabajar con ambientes virtuales es que nos permite crear entornos de desarrollo independientes para cada proyecto. De esta manera, no habrá conflictos entre las versiones de las distintas librerías que usemos en diferentes proyectos.

Para crear un ambiente virtual con Pip, utilizamos el siguiente comando:

_python -m venv micarpeta_

Este comando creará una nueva carpeta llamada _“micarpeta”_ en el directorio actual, donde se almacenarán todas las dependencias del proyecto. Para activar el ambiente virtual, debemos utilizar el siguiente comando:

_source micarpeta/bin/activate_

Este comando nos permitirá trabajar en el ambiente virtual aislado, donde podremos instalar las librerías necesarias para nuestro proyecto sin afectar a otras aplicaciones o proyectos. Para desactivar el ambiente virtual, basta con utilizar el comando _“deactivate”._
