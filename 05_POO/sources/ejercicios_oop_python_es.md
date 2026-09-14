# 30+ Ejercicios de Programación Orientada a Objetos (OOP) en Python

Fuente original: [pynative.com](https://pynative.com/python-object-oriented-programming-oop-exercise/)

> Todo el contenido (consignas, propósito, pistas, explicaciones y los mensajes impresos por el código) está traducido al español. Los nombres de clases, métodos y variables se mantienen en inglés, siguiendo la convención estándar de programación en Python.

---

## Ejercicio 1: Definir una clase Vehicle vacía

**Consigna:** Escribe un programa en Python para crear una clase llamada `Vehicle` que no tenga variables ni métodos definidos dentro.

**Propósito:** Este ejercicio introduce la forma más básica de definición de una clase en Python. Enseña la sintaxis necesaria para declarar una clase y el uso de la palabra clave `pass` como marcador de posición, algo esencial cuando se quiere definir una clase o función vacía sin provocar un error de sintaxis.

**Entrada dada:** No se requiere entrada.

**Salida esperada:** `<class '__main__.Vehicle'>`

**Pista:**
- Usa la palabra clave `class` seguida del nombre de la clase y dos puntos.
- Usa `pass` dentro del cuerpo de la clase para que sea Python válido sin agregar atributos ni métodos.
- Después de definir la clase, puedes confirmar que existe imprimiendo `Vehicle` directamente.

**Solución y explicación:**

```python
class Vehicle:
    pass

print(Vehicle)
```

- **`class Vehicle:`**: Declara una nueva clase llamada `Vehicle`. Los dos puntos marcan el inicio del cuerpo de la clase.
- **`pass`**: Un marcador de posición que no hace nada, pero satisface el requisito de Python de que el cuerpo de una clase no esté vacío. No hace nada en tiempo de ejecución, pero evita un `SyntaxError`.
- **`print(Vehicle)`**: Imprime el objeto clase en sí, confirmando que fue creado correctamente. La salida muestra el nombre de la clase y el módulo al que pertenece (`__main__` cuando se ejecuta como script).

---

## Ejercicio 2: Clase Vehicle con atributos de instancia

**Consigna:** Escribe un programa en Python para crear una clase `Vehicle` con dos atributos de instancia: `max_speed` y `mileage`. Crea un objeto de la clase e imprime ambos atributos.

**Propósito:** Aprende a definir atributos de instancia usando el método constructor `__init__`. Los atributos de instancia son únicos para cada objeto, lo que significa que distintos objetos `Vehicle` pueden tener diferentes valores de velocidad y kilometraje. Este es un concepto fundamental en la programación orientada a objetos.

**Entrada dada:** `vehicle1 = Vehicle("Tesla Model S", 250, 18)`

**Salida esperada:** `Vehicle Name: Tesla Model S, Speed: 250, Mileage: 18`

**Pista:**
- Define un método `__init__` que acepte `self`, `name`, `max_speed` y `mileage` como parámetros.
- Dentro de `__init__`, asigna cada parámetro a `self` para almacenarlos como atributos de instancia.
- Crea una instancia llamando a `Vehicle(...)` con los argumentos requeridos, y luego accede a los atributos usando notación de punto.

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")
```

- **`def __init__(self, name, max_speed, mileage)`**: El método constructor, llamado automáticamente cuando se crea un nuevo objeto. `self` hace referencia a la instancia específica que se está inicializando.
- **`self.name = name`**: Vincula el argumento pasado durante la creación del objeto a la instancia, haciéndolo accesible como atributo en ese objeto.
- **`vehicle1 = Vehicle("Tesla Model S", 250, 18)`**: Crea una nueva instancia de `Vehicle`. Python pasa los argumentos a `__init__` automáticamente.
- **`vehicle1.max_speed`**: Se usa notación de punto para acceder a los atributos de instancia. Cada objeto mantiene su propia copia de estos valores.

---

## Ejercicio 3: Clase Rectangle con área y perímetro

**Consigna:** Escribe un programa en Python para crear una clase `Rectangle` con `length` y `width` como atributos de instancia, y dos métodos: `area()` que retorna el área y `perimeter()` que retorna el perímetro.

**Propósito:** Aprende a agregar métodos de instancia a una clase. Los métodos permiten que los objetos realicen operaciones usando sus propios datos, lo cual es un principio clave del encapsulamiento en OOP. Calcular propiedades geométricas es un contexto claro y práctico para entender cómo `self` conecta los métodos con los datos de la instancia.

**Entrada dada:** `rect = Rectangle(10, 4)`

**Salida esperada:** `Area = 40` y `Perimeter = 28`

**Pista:**
- Almacena `length` y `width` como atributos de instancia dentro de `__init__`.
- Define `area(self)` que retorne `self.length * self.width`.
- Define `perimeter(self)` que retorne `2 * (self.length + self.width)`.

**Solución y explicación:**

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 4)
print("Area =", rect.area())
print("Perimeter =", rect.perimeter())
```

- **`def area(self)`**: Un método de instancia que usa `self.length` y `self.width` para calcular y retornar el área. El parámetro `self` le da al método acceso a los atributos propios del objeto.
- **`def perimeter(self)`**: Aplica la fórmula estándar del perímetro de un rectángulo: `2 * (length + width)`. Al igual que `area()`, lee directamente de los atributos de la instancia.
- **`rect.area()`**: Al llamar a un método sobre una instancia, esa instancia se pasa automáticamente como `self`. No es necesario pasar `self` explícitamente al llamar al método.

---

## Ejercicio 4: Clase Student con promedio de notas

**Consigna:** Escribe un programa en Python para crear una clase `Student` que almacene el nombre (`name`) de un estudiante y una lista de notas (`marks`). Agrega un método `average()` que calcule y retorne el promedio de todas las notas.

**Propósito:** Este ejercicio muestra cómo los atributos de instancia pueden almacenar tipos de datos complejos, como listas, y no solo valores simples. También practica la combinación de OOP con operaciones de listas y aritmética, un patrón común en libros de calificaciones, paneles de control y herramientas de reportes.

**Entrada dada:** `s1 = Student("Alice", [85, 90, 78, 92, 88])`

**Salida esperada:** `Alice's Average Grade: 86.6`

**Pista:**
- Acepta `name` y `marks` (una lista) en el método `__init__` y asígnalos a `self`.
- En el método `average()`, usa `sum(self.marks) / len(self.marks)` para calcular la media.
- Usa `round()` si quieres controlar la cantidad de decimales en la salida.

**Solución y explicación:**

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name}'s Average Grade: {s1.average()}")
```

- **`self.marks = marks`**: Almacena la lista completa como atributo de instancia. Cada objeto `Student` mantiene su propia lista independiente de notas.
- **`sum(self.marks)`**: Usa la función incorporada `sum()` de Python para sumar todos los elementos de la lista de notas sin necesidad de un bucle explícito.
- **`len(self.marks)`**: Retorna la cantidad de elementos de la lista, usada como divisor para calcular la media. Esto funciona correctamente sin importar cuántas notas se almacenen.
- **`s1.average()`**: Llama al método sobre la instancia. El resultado es un flotante, porque el operador `/` de Python 3 siempre retorna un flotante.

---

## Ejercicio 5: Clase Product con calculadora de valor de stock

**Consigna:** Escribe un programa en Python para crear una clase `Product` con tres atributos de instancia: `name`, `price` y `quantity`. Agrega un método `total_value()` que retorne el valor total del stock multiplicando el precio por la cantidad.

**Propósito:** Este ejercicio modela un escenario de negocio real usando OOP. Refuerza cómo los métodos de instancia pueden derivar nueva información a partir de atributos existentes, un patrón muy usado en gestión de inventario, comercio electrónico y aplicaciones financieras.

**Entrada dada:** `p1 = Product("Laptop", 899.99, 5)`

**Salida esperada:** `Total stock value of Laptop: $4499.95`

**Pista:**
- Define `__init__` con `name`, `price` y `quantity` como parámetros y asigna cada uno a `self`.
- En `total_value()`, retorna `self.price * self.quantity`.
- Usa un f-string con formato `:.2f` para mostrar el resultado como un valor monetario con dos decimales.

**Solución y explicación:**

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")
```

- **`self.price` y `self.quantity`**: Se almacenan como atributos de instancia, de modo que cada objeto `Product` lleva el control de su propio precio y nivel de stock de forma independiente.
- **`def total_value(self)`**: Un método calculado que multiplica `self.price` por `self.quantity` para obtener el valor total del stock. No se necesitan datos externos porque todos los valores ya están en la instancia.
- **`:.2f`**: Un especificador de formato dentro de un f-string que redondea el flotante a exactamente dos decimales, que es el formato estándar para mostrar valores monetarios.

---

## Ejercicio 6: BankAccount con depósito y protección contra sobregiro

**Consigna:** Escribe un programa en Python para crear una clase `BankAccount` con un atributo `balance` y dos métodos: `deposit(amount)` que agrega fondos al saldo, y `withdraw(amount)` que descuenta fondos pero evita que el saldo quede por debajo de cero.

**Propósito:** Aprende validación de datos y lógica condicional dentro de métodos de instancia. Evitar el sobregiro es una regla de negocio del mundo real, y al implementarla aquí aprendes cómo las clases pueden imponer restricciones sobre sus propios datos, una idea central detrás del encapsulamiento en OOP.

**Entrada dada:** Saldo inicial de `1000`, depósito de `500`, retiro de `200`, y luego un intento de retirar `2000`.

**Salida esperada:**

```
Balance after deposit: 1500
Balance after withdrawal: 1300
Insufficient funds. Current balance: 1300
```

**Pista:**
- Inicializa `self.balance` en `__init__`.
- En `deposit()`, suma el monto directamente a `self.balance`.
- En `withdraw()`, usa una sentencia `if` para verificar si `amount <= self.balance` antes de descontar. Si no, imprime un mensaje de fondos insuficientes.

**Solución y explicación:**

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
```

- **`self.balance += amount`**: El método `deposit()` modifica directamente el `balance` de la instancia. Como el atributo se almacena en `self`, el cambio persiste en todas las llamadas futuras a métodos sobre ese objeto.
- **`if amount <= self.balance`**: Protege el retiro verificando que existan fondos suficientes antes de modificar el saldo. Esto impone la regla de negocio de que el saldo no puede volverse negativo.
- **`else: print(...)`**: Da retroalimentación cuando un retiro es rechazado. En una aplicación real esto podría lanzar una excepción personalizada, pero un mensaje impreso es apropiado para un ejercicio introductorio.

---

## Ejercicio 7: Clase Light con alternancia de estado encendido/apagado

**Consigna:** Escribe un programa en Python para crear una clase `Light` con tres métodos: `turn_on()` que enciende la luz, `turn_off()` que la apaga, y `status()` que informa si la luz está actualmente encendida o apagada.

**Propósito:** Este ejercicio modela un objeto con estado simple, donde el objeto recuerda y cambia su propia condición a lo largo del tiempo. Introduce el concepto de gestión de estado dentro de una clase, un patrón presente en componentes de interfaz, dispositivos IoT, objetos de videojuegos y motores de flujo de trabajo.

**Entrada dada:** Crea un objeto `Light`, llama a `turn_on()`, verifica `status()`, llama a `turn_off()` y verifica `status()` nuevamente.

**Salida esperada:**

```
Light is ON
Current status: ON
Light is OFF
Current status: OFF
```

**Pista:**
- Usa un atributo booleano como `self.is_on = False` en `__init__` para rastrear el estado actual.
- `turn_on()` debe establecer `self.is_on = True` e imprimir un mensaje de confirmación.
- `turn_off()` debe establecer `self.is_on = False` e imprimir un mensaje de confirmación.
- En `status()`, usa un condicional para imprimir `"ON"` u `"OFF"` según el valor de `self.is_on`.

**Solución y explicación:**

```python
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")

light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()
```

- **`self.is_on = False`**: Establece el estado inicial de la luz como apagada cuando el objeto se crea por primera vez. Usar un booleano es la forma más directa de representar una condición de dos estados como encendido/apagado.
- **`turn_on()` y `turn_off()`**: Cada método simplemente cambia `self.is_on` al valor booleano apropiado e imprime un mensaje. Como el valor se almacena en `self`, el cambio se conserva en todas las llamadas subsecuentes a los métodos.
- **`"ON" if self.is_on else "OFF"`**: Una expresión ternaria de Python que convierte el estado booleano en una cadena legible. Es más conciso que escribir un bloque `if/else` completo para una salida simple de dos ramas.

---

## Ejercicio 8: Clase User con validación de contraseña

**Consigna:** Escribe un programa en Python para crear una clase `User` que almacene un `username` y un `password`. Agrega un método `check_password(input_password)` que retorne `True` si la entrada coincide con la contraseña almacenada, y `False` en caso contrario.

**Propósito:** Este ejercicio introduce la idea de acceso controlado a datos sensibles dentro de una clase. En lugar de exponer la contraseña directamente, la clase ofrece un método dedicado para verificarla. Este patrón refleja un principio central del encapsulamiento en OOP, donde los datos internos están protegidos y solo se accede a ellos mediante interfaces definidas.

**Entrada dada:** `u1 = User("alice", "secure123")`

**Salida esperada:**

```
True  
False
```

**Pista:**
- Almacena `username` y `password` como atributos de instancia en `__init__`.
- En `check_password(self, input_password)`, compara `input_password` con `self.password` usando `==` y retorna el resultado directamente.
- Llama al método con una contraseña correcta y luego con una incorrecta para verificar ambos resultados.

**Solución y explicación:**

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password

u1 = User("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("wrongpass"))
```

- **`self.password = password`**: Almacena la contraseña como atributo de instancia. En aplicaciones reales nunca se almacenaría una contraseña en texto plano; en su lugar se hashearía usando una librería como `bcrypt`. Aquí se usa texto plano para mantener el foco en los fundamentos de OOP.
- **`def check_password(self, input_password)`**: Acepta una contraseña candidata y la compara con la almacenada. Exponer un método en lugar del atributo directamente significa que el código externo nunca necesita tocar `self.password` directamente.
- **`return self.password == input_password`**: La comparación `==` evalúa a un booleano, por lo que el resultado puede retornarse directamente sin envolverlo en un `if/else` explícito.

---

## Ejercicio 9: Clase Temperature con conversores de unidades

**Consigna:** Escribe un programa en Python para crear una clase `Temperature` que almacene una temperatura en grados Celsius. Agrega dos métodos: `to_fahrenheit()` que convierte y retorna el valor en Fahrenheit, y `to_kelvin()` que convierte y retorna el valor en Kelvin.

**Propósito:** Este ejercicio demuestra cómo una clase puede actuar como contenedor de datos con lógica de conversión incorporada. Refuerza la escritura de múltiples métodos que operan sobre el mismo atributo de instancia, y aplica fórmulas matemáticas sencillas en un contexto científico práctico.

**Entrada dada:** `t = Temperature(100)`

**Salida esperada:**

```
Celsius: 100
Fahrenheit: 212.0
Kelvin: 373.15
```

**Pista:**
- Almacena el valor en Celsius como `self.celsius` en `__init__`.
- Para Fahrenheit, usa la fórmula: `(celsius * 9/5) + 32`.
- Para Kelvin, usa la fórmula: `celsius + 273.15`.

**Solución y explicación:**

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

t = Temperature(100)
print("Celsius:", t.celsius)
print("Fahrenheit:", t.to_fahrenheit())
print("Kelvin:", t.to_kelvin())
```

- **`self.celsius = celsius`**: La única fuente de verdad para este objeto. Ambos métodos de conversión derivan sus resultados de este único atributo, por lo que actualizarlo afectaría automáticamente todas las conversiones.
- **`(self.celsius * 9 / 5) + 32`**: La fórmula estándar de Celsius a Fahrenheit. En Python 3, `9 / 5` evalúa a `1.8` como flotante, por lo que el resultado siempre es un número decimal.
- **`self.celsius + 273.15`**: La conversión de Celsius a Kelvin suma el desplazamiento del cero absoluto. Sumar un literal flotante garantiza que el valor retornado siempre sea un flotante, en consonancia con la notación científica.

---

## Ejercicio 10: Clase Notebook con agregado y visualización de notas

**Consigna:** Escribe un programa en Python para crear una clase `Notebook` que mantenga una lista interna de notas. Agrega un método `add_note(note)` que agregue una nueva nota a la lista, y un método `show_notes()` que imprima todas las notas almacenadas.

**Propósito:** Este ejercicio muestra cómo una clase puede gestionar una colección de datos que crece a lo largo de su vida útil. Practica la inicialización de una estructura de datos mutable dentro de `__init__` y la escritura de métodos que tanto modifican como leen esa estructura, un patrón que aparece en listas de tareas, colas de mensajes, registros y muchas otras aplicaciones.

**Entrada dada:** Agregar tres notas: `"Buy groceries"`, `"Read a book"`, `"Call the doctor"`.

**Salida esperada:**

```
1. Buy groceries
2. Read a book
3. Call the doctor
```

**Pista:**
- Inicializa `self.notes = []` dentro de `__init__` para que cada objeto `Notebook` comience con su propia lista vacía.
- En `add_note()`, usa `self.notes.append(note)` para agregar la nueva entrada.
- En `show_notes()`, usa `enumerate(self.notes, start=1)` para imprimir cada nota con un prefijo numerado.

**Solución y explicación:**

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")

nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()
```

- **`self.notes = []`**: Inicializar la lista dentro de `__init__` es fundamental. Si se definiera a nivel de clase en su lugar, todas las instancias compartirían la misma lista, causando que las notas de un cuaderno aparecieran en otro.
- **`self.notes.append(note)`**: Modifica en el lugar la propia lista de la instancia. Cada llamada a `add_note()` hace crecer la lista en una entrada, y el cambio persiste en el objeto hasta que se destruye.
- **`enumerate(self.notes, start=1)`**: Produce pares de `(índice, valor)` comenzando desde 1, permitiendo que el bucle imprima una lista numerada sin llevar manualmente el conteo con una variable.

---

## Ejercicio 11: CoffeeMachine con seguimiento de múltiples recursos

**Consigna:** Escribe un programa en Python para crear una clase `CoffeeMachine` que rastree tres atributos de recursos: `water`, `coffee` y `milk` (en ml/g). Agrega un método `make_latte()` que verifique si hay recursos suficientes disponibles, los descuente si es así, e imprima un mensaje apropiado en cualquiera de los casos.

**Propósito:** Este ejercicio combina gestión de estado, seguimiento de recursos y lógica condicional dentro de una sola clase. Refleja cómo los sistemas con estado del mundo real (máquinas expendedoras, sistemas de inventario, gestores de recursos de videojuegos) verifican condiciones previas antes de ejecutar una acción y actualizan su estado interno solo cuando la acción es válida.

**Entrada dada:** `CoffeeMachine(water=300, coffee=100, milk=200)`. Un latte requiere `200ml` de agua, `20g` de café y `150ml` de leche.

**Salida esperada:**

```
Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
Not enough resources to make a latte.
```

**Pista:**
- Almacena `water`, `coffee` y `milk` como atributos de instancia en `__init__`.
- En `make_latte()`, define las cantidades requeridas como variables locales y usa una sola condición `if` para verificar los tres recursos a la vez.
- Si la verificación se cumple, descuenta las cantidades requeridas de cada atributo e imprime los niveles restantes. En caso contrario, imprime un mensaje de fallo.

**Solución y explicación:**

```python
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        water_needed = 200
        coffee_needed = 20
        milk_needed = 150

        if self.water >= water_needed and self.coffee >= coffee_needed and self.milk >= milk_needed:
            self.water -= water_needed
            self.coffee -= coffee_needed
            self.milk -= milk_needed
            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")

machine = CoffeeMachine(water=300, coffee=100, milk=200)
machine.make_latte()
machine.make_latte()
```

- **`water_needed`, `coffee_needed`, `milk_needed`**: Definidas como variables locales dentro del método para representar la receta. Mantenerlas locales (en lugar de escribirlas fijas dentro de la condición) hace que el método sea más fácil de leer y los valores fáciles de cambiar en un solo lugar.
- **`if self.water >= water_needed and ...`**: Las tres verificaciones de recursos se combinan en una sola condición usando `and`. El descuento solo ocurre cuando se cumplen todas las condiciones, lo que evita un consumo parcial de recursos ante un intento fallido.
- **`self.water -= water_needed`**: Modifica el atributo de instancia en el lugar. Después de un latte exitoso, el estado de la máquina se actualiza permanentemente, por lo que una segunda llamada a `make_latte()` refleja los niveles reducidos.
- **Segunda llamada a `make_latte()`**: Con solo `100ml` de agua restante (menos que los `200ml` requeridos), la condición falla y se imprime el mensaje de recursos insuficientes, demostrando la persistencia del estado entre llamadas.

---

## Ejercicio 12: Atributo de clase compartido entre instancias

**Consigna:** Escribe un programa en Python para crear una clase `Vehicle` con un atributo de clase `color = "White"` que sea compartido por todas las instancias. Crea dos objetos vehicle y demuestra que ambos comparten el mismo color por defecto, luego muestra que cambiar el atributo de clase actualiza todas las instancias que no lo hayan sobrescrito.

**Propósito:** Este ejercicio clarifica la distinción entre atributos de clase y atributos de instancia. Los atributos de clase se definen directamente en la clase y son compartidos por todas las instancias, lo que los hace ideales para valores por defecto o constantes que aplican universalmente. Entender esta diferencia previene errores sutiles cuando se comparten datos mutables accidentalmente entre objetos.

**Entrada dada:** `v1 = Vehicle("Tesla", 250)` y `v2 = Vehicle("BMW", 200)`.

**Salida esperada:**

```
Tesla - Color: White, Speed: 250
BMW - Color: White, Speed: 200
Tesla - Color: Red, Speed: 250
BMW - Color: Red, Speed: 200
```

**Pista:**
- Define `color = "White"` directamente en el cuerpo de la clase, fuera de cualquier método, para convertirlo en un atributo de clase.
- Los atributos de instancia como `name` y `max_speed` se siguen definiendo en `__init__` como de costumbre.
- Para actualizar el atributo compartido en todas las instancias, reasígnalo mediante la clase misma: `Vehicle.color = "Red"`.

**Solución y explicación:**

```python
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.name} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.max_speed}")

Vehicle.color = "Red"

print(f"{v1.name} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.max_speed}")
```

- **`color = "White"`**: Declarado a nivel de clase, fuera de `__init__`. Esto significa que pertenece a la clase misma, no a ninguna instancia individual. Todos los objetos comparten el mismo valor a menos que lo sobrescriban individualmente.
- **`v1.color`**: Cuando Python busca `color` en una instancia y no lo encuentra como atributo de instancia, sube hasta la clase y lo encuentra ahí como atributo de clase. Esta cadena de búsqueda forma parte del orden de resolución de atributos de Python.
- **`Vehicle.color = "Red"`**: Reasignar mediante el nombre de la clase actualiza el atributo a nivel de clase, por lo que todas las instancias que aún dependan del atributo de clase reflejan inmediatamente el nuevo valor. En cambio, hacer `v1.color = "Red"` solo crearía un nuevo atributo de instancia en `v1`, sin afectar a `v2`.

---

## Ejercicio 13: Subclase Bus que hereda de Vehicle

**Consigna:** Escribe un programa en Python para crear una clase padre `Vehicle` con atributos `name` y `max_speed` y un método `display()`. Luego crea una clase hija `Bus` que herede todo de `Vehicle` sin agregar nada nuevo, y confirma que una instancia de `Bus` puede acceder al método del padre.

**Propósito:** Este ejercicio introduce la herencia, uno de los cuatro pilares de la OOP. La herencia permite que una clase hija reciba automáticamente todos los atributos y métodos de su clase padre, promoviendo la reutilización de código y expresando relaciones naturales de "es un". Un `Bus` "es un" `Vehicle`, por lo que tiene sentido que comparta la misma interfaz.

**Entrada dada:** `bus1 = Bus("School Bus", 120)`

**Salida esperada:** `Vehicle: School Bus, Max Speed: 120 km/h`

**Pista:**
- Para crear una clase hija, pasa la clase padre como argumento en la definición de la clase: `class Bus(Vehicle):`.
- Si la clase hija no agrega nada nuevo, usa `pass` en su cuerpo.
- Crea una instancia de `Bus` usando los mismos argumentos que `Vehicle` y llama a `display()` para confirmar que la herencia funciona.

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 120)
bus1.display()
```

- **`class Bus(Vehicle):`**: Los paréntesis indican que `Bus` hereda de `Vehicle`. Python configura la cadena de herencia automáticamente, lo que significa que `Bus` obtiene todos los atributos y métodos de `Vehicle` de forma gratuita.
- **`pass`**: Como `Bus` no agrega ningún comportamiento nuevo en esta etapa, se usa `pass` como marcador de posición. La clase sigue siendo completamente funcional porque todo lo que necesita viene de `Vehicle`.
- **`bus1.display()`**: Python primero busca `display` en la instancia de `Bus`, luego en la clase `Bus`, y finalmente en `Vehicle`, donde encuentra y ejecuta el método. Este proceso de búsqueda se conoce como Orden de Resolución de Métodos (MRO).

---

## Ejercicio 14: Sobrescribir un método del padre usando super()

**Consigna:** Escribe un programa en Python donde una clase padre `Vehicle` tenga un método `seating_capacity()` que acepte un argumento `capacity`. Crea una clase hija `Bus` que sobrescriba este método para proporcionar una capacidad de asientos por defecto de `50`, usando `super()` para llamar internamente a la versión del padre.

**Propósito:** Este ejercicio cubre la sobrescritura de métodos y el uso de `super()`, dos herramientas clave en la herencia de OOP. La sobrescritura permite que una clase hija personalice o extienda el comportamiento de un método del padre sin reescribirlo desde cero. `super()` delega parte del trabajo de vuelta al padre, manteniendo el código DRY y conservando la lógica original como base.

**Entrada dada:** `bus = Bus("School Bus", 120)`

**Salida esperada:** `School Bus seating capacity is: 50`

**Pista:**
- Define `seating_capacity(self, capacity)` en la clase `Vehicle` y haz que imprima un mensaje usando el argumento capacity.
- En la clase `Bus`, define un método con el mismo nombre pero sobrescríbelo para llamar a `super().seating_capacity(50)`, pasando el valor por defecto `50` directamente.
- Llama a `bus.seating_capacity()` sobre una instancia de `Bus` sin argumentos para confirmar que el valor por defecto se aplica.

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)

bus = Bus("School Bus", 120)
bus.seating_capacity()
```

- **`def seating_capacity(self, capacity)` en `Vehicle`**: El padre define el método para aceptar un valor de capacidad flexible, manteniéndolo lo suficientemente general para funcionar con cualquier tipo de vehículo.
- **`def seating_capacity(self)` en `Bus`**: El hijo sobrescribe el método con una versión que no recibe argumento de capacidad. Esta es la sobrescritura: cuando se llama a `seating_capacity()` sobre una instancia de `Bus`, Python ejecuta esta versión en lugar de la del padre.
- **`super().seating_capacity(50)`**: `super()` retorna un proxy hacia la clase padre, permitiendo que el hijo llame directamente al método del padre. El `50` fijo es el valor por defecto específico del bus, pasado hacia arriba a la implementación del padre para que la lógica de impresión permanezca en un solo lugar.
- **`bus.seating_capacity()`**: Se llama sin argumentos sobre la instancia de `Bus`. La sobrescritura intercepta la llamada, provee el valor por defecto de `50`, y delega la salida real al padre, combinando el comportamiento de ambas clases de forma limpia.

---

## Ejercicio 15: Agregar tarifa de mantenimiento en clase hija vía super()

**Consigna:** Escribe un programa en Python que cree una clase padre `Vehicle` con una tarifa base, y luego extienda una clase hija `Taxi` que agregue una tarifa de mantenimiento del 10% sobre la tarifa base usando `super()`.

**Propósito:** Este ejercicio enseña cómo usar `super()` para llamar al constructor de la clase padre, extender el comportamiento de la clase hija construyendo sobre atributos heredados, y modelar lógica de precios del mundo real usando herencia.

**Entrada dada:** `base_fare = 500`

**Salida esperada:** `Total fare with maintenance fee: 550.0`

**Pista:**
- Define una clase `Vehicle` con un `__init__` que acepte `base_fare` y lo almacene como atributo de instancia.
- Crea una clase `Taxi` que herede de `Vehicle`.
- En `Taxi.__init__`, llama a `super().__init__(base_fare)` para inicializar al padre, y luego calcula la tarifa de mantenimiento como `base_fare * 0.10`.
- Agrega un método `total_fare()` que retorne `self.base_fare + self.maintenance_fee`.

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare * 0.10

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

taxi = Taxi(500)
print("Total fare with maintenance fee:", taxi.total_fare())
```

- **`class Vehicle`**: Define la clase padre que acepta y almacena `base_fare` en su constructor.
- **`super().__init__(base_fare)`**: Llama al constructor del padre desde dentro de la clase hija, asegurando que `self.base_fare` quede correctamente establecido antes de que el hijo agregue su propia lógica.
- **`self.maintenance_fee = base_fare * 0.10`**: Calcula la tarifa de mantenimiento del 10% y la almacena como un atributo exclusivo del hijo.
- **`total_fare()`**: Retorna la suma de la tarifa base y la tarifa de mantenimiento, demostrando cómo las clases hijas pueden extender el comportamiento del padre sin modificarlo.

---

## Ejercicio 16: Polimorfismo con speak() en Dog y Cat

**Consigna:** Escribe un programa en Python que defina una clase base `Animal` con un método `speak()`, y luego lo sobrescriba en las subclases `Dog` y `Cat` para que retornen sus respectivos sonidos.

**Propósito:** Este ejercicio introduce la sobrescritura de métodos, uno de los pilares centrales del polimorfismo en OOP. Muestra cómo distintas subclases pueden compartir la misma interfaz pero proporcionar su propio comportamiento específico.

**Entrada dada:** Objetos de las clases `Dog` y `Cat`

**Salida esperada:**

```
Dog says: Woof!  
Cat says: Meow!
```

**Pista:**
- Define una clase `Animal` con un método `speak()` que retorne una cadena genérica como `"Some sound"`.
- Crea las clases `Dog` y `Cat` que hereden de `Animal`.
- Sobrescribe `speak()` en cada subclase para retornar la cadena de sonido apropiada.
- Instancia ambas clases y llama a `speak()` en cada objeto para verificar la salida.

**Solución y explicación:**

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
```

- **`class Animal`**: Actúa como clase base con un método `speak()` por defecto, estableciendo una interfaz común para todas las subclases.
- **`class Dog(Animal)`**: Hereda de `Animal` y sobrescribe `speak()` para retornar `"Woof!"`, reemplazando la implementación genérica del padre.
- **`class Cat(Animal)`**: De forma similar, sobrescribe `speak()` para retornar `"Meow!"`.
- **Sobrescritura de métodos**: Cuando se llama a `speak()` sobre un objeto `Dog` o `Cat`, Python usa la versión de la subclase, no la del padre. Este es el fundamento del polimorfismo.

---

## Ejercicio 17: Lógica de pago para empleados de tiempo completo vs medio tiempo

**Consigna:** Escribe un programa en Python que defina una clase base `Employee`, y luego cree las subclases `FullTimeEmployee` y `PartTimeEmployee`, cada una implementando una lógica distinta para calcular el pago.

**Propósito:** Este ejercicio modela un escenario común de recursos humanos y enseña cómo usar la herencia para compartir atributos comunes mientras se permite que cada subclase defina su propia lógica de negocio para calcular el pago.

**Entrada dada:** `FullTimeEmployee("Alice", 60000)` y `PartTimeEmployee("Bob", 500, 20)`

**Salida esperada:**

```
Alice's monthly pay: 5000.0  
Bob's monthly pay: 10000
```

**Pista:**
- Define una clase base `Employee` con `__init__` que acepte `name` y un método `calculate_pay()` que pueda dejarse como marcador de posición.
- En `FullTimeEmployee`, almacena el `salary` anual y calcula el pago mensual como `salary / 12`.
- En `PartTimeEmployee`, almacena `hourly_rate` y `hours_worked`, y luego calcula el pago como su producto.
- Sobrescribe `calculate_pay()` en cada subclase con la fórmula apropiada.

**Solución y explicación:**

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_pay(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

ft = FullTimeEmployee("Alice", 60000)
pt = PartTimeEmployee("Bob", 500, 20)

print(f"{ft.name}'s monthly pay: {ft.calculate_pay()}")
print(f"{pt.name}'s monthly pay: {pt.calculate_pay()}")
```

- **`class Employee`**: Sirve como clase base que contiene el atributo compartido `name` y un `calculate_pay()` por defecto que retorna `0`.
- **`FullTimeEmployee.calculate_pay()`**: Divide el salario anual entre 12 para obtener el pago mensual, usando el operador `/` de Python 3, que retorna un flotante.
- **`PartTimeEmployee.calculate_pay()`**: Multiplica `hourly_rate` por `hours_worked`, modelando un contrato de pago por hora.
- **`super().__init__(name)`**: Usado en ambas subclases para delegar la asignación de `name` al padre, evitando la duplicación de código.

---

## Ejercicio 18: Subclases Shape con métodos area() personalizados

**Consigna:** Escribe un programa en Python que defina una clase base `Shape` con un método `area()`, y luego lo implemente en las subclases `Circle`, `Square` y `Triangle` usando las fórmulas geométricas correspondientes.

**Propósito:** Este ejercicio es una demostración clásica de polimorfismo. Cada figura comparte la misma interfaz `area()` pero proporciona un cálculo completamente distinto, mostrando cómo la OOP maneja de forma limpia la variación del mundo real.

**Entrada dada:** `Circle(7)`, `Square(4)`, `Triangle(6, 8)`

**Salida esperada:**

```
Circle area: 153.94  
Square area: 16  
Triangle area: 24.0
```

**Pista:**
- Define una clase base `Shape` con un método `area()` que retorne `0` como marcador de posición.
- Para `Circle`, usa la fórmula `3.14159 * radius ** 2`.
- Para `Square`, usa `side ** 2`.
- Para `Triangle`, usa `0.5 * base * height`.

**Solución y explicación:**

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(7), Square(4), Triangle(6, 8)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")
```

- **`class Shape`**: Proporciona una interfaz común con un `area()` por defecto que retorna `0`. Se espera que todas las subclases sobrescriban este método.
- **`Circle.area()`**: Aplica la fórmula `pi * r^2`. El resultado se redondea a 2 decimales usando `round()` para una salida limpia.
- **`Square.area()`**: Retorna `side ** 2`, la fórmula de área más simple.
- **`type(shape).__name__`**: Obtiene dinámicamente el nombre de la clase de cada objeto en tiempo de ejecución, haciendo reutilizable el bucle de impresión sin necesidad de escribir los nombres a mano.

---

## Ejercicio 19: Subclases Media con atributos específicos por tipo

**Consigna:** Escribe un programa en Python que defina una clase base `Media`, y luego cree las subclases `Book`, `Magazine` y `DVD`, cada una con atributos específicos de su tipo y un método `describe()`.

**Propósito:** Este ejercicio muestra cómo la herencia puede modelar una taxonomía de objetos relacionados. Cada tipo de medio comparte una identidad común (título, precio) pero lleva atributos únicos específicos de su formato, reflejando sistemas reales de bibliotecas o inventarios.

**Entrada dada:** `Book("Clean Code", 499, "Robert C. Martin")`, `Magazine("Wired", 150, "Monthly")`, `DVD("Inception", 299, 148)`

**Salida esperada:**

```
Book: Clean Code by Robert C. Martin - Rs.499  
Magazine: Wired (Monthly) - Rs.150  
DVD: Inception, 148 mins - Rs.299
```

**Pista:**
- Define una clase base `Media` con `title` y `price` en `__init__`.
- Cada subclase debe llamar a `super().__init__(title, price)` y luego agregar su propio atributo único: `author` para `Book`, `frequency` para `Magazine`, y `duration` para `DVD`.
- Sobrescribe un método `describe()` en cada subclase para imprimir una cadena formateada usando los atributos compartidos y únicos.

**Solución y explicación:**

```python
class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def describe(self):
        return f"{self.title} - Rs.{self.price}"

class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def describe(self):
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"

class Magazine(Media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self.frequency = frequency

    def describe(self):
        return f"Magazine: {self.title} ({self.frequency}) - Rs.{self.price}"

class DVD(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration

    def describe(self):
        return f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}"

items = [
    Book("Clean Code", 499, "Robert C. Martin"),
    Magazine("Wired", 150, "Monthly"),
    DVD("Inception", 299, 148)
]

for item in items:
    print(item.describe())
```

- **`class Media`**: Almacena los atributos compartidos `title` y `price`, comunes a todos los tipos de medios, y proporciona un `describe()` genérico como respaldo.
- **`super().__init__(title, price)`**: Usado en cada subclase para evitar repetir la asignación de los atributos compartidos, manteniendo el código DRY (No te Repitas).
- **Atributos únicos**: `author`, `frequency` y `duration` son específicos de cada subclase y no pertenecerían a la clase base, ya que no todos los tipos de medios los comparten.
- **Iterar con `describe()`**: Llamar al mismo método en distintos objetos y obtener distintas salidas es polimorfismo en la práctica.

---

## Ejercicio 20: Subclase DiscountedOrder con 10% de descuento

**Consigna:** Escribe un programa en Python que cree una clase `Order` con un monto total, y luego cree una subclase `DiscountedOrder` que aplique un descuento del 10% al total.

**Propósito:** Este ejercicio modela un patrón común de comercio electrónico y muestra cómo una clase hija puede extender el comportamiento de un padre modificando un valor calculado, sin cambiar en absoluto la clase padre.

**Entrada dada:** `DiscountedOrder("ORD001", 1200)`

**Salida esperada:**

```
Order ID: ORD001  
Original Total: 1200  
Discounted Total: 1080.0
```

**Pista:**
- Define una clase `Order` con atributos `order_id` y `total` y un método `get_total()` que retorne `self.total`.
- En `DiscountedOrder`, llama a `super().__init__(order_id, total)` y sobrescribe `get_total()` para retornar `self.total * 0.90`.
- Imprime tanto el `self.total` original como el resultado con descuento de `get_total()` para mostrar la diferencia.

**Solución y explicación:**

```python
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, order_id, total):
        super().__init__(order_id, total)

    def get_total(self):
        return self.total * 0.90

order = DiscountedOrder("ORD001", 1200)
print("Order ID:", order.order_id)
print("Original Total:", order.total)
print("Discounted Total:", order.get_total())
```

- **`class Order`**: La clase padre almacena `order_id` y `total`, y `get_total()` simplemente retorna el monto completo sin ninguna modificación.
- **`DiscountedOrder.get_total()`**: Sobrescribe el método del padre para aplicar una reducción del 10% multiplicando `self.total` por `0.90`. La clase padre nunca se modifica.
- **`order.total` vs `order.get_total()`**: Acceder directamente a `self.total` sigue retornando el valor original, mientras que `get_total()` retorna el valor con descuento. Esta distinción es importante para mantener intactos los datos originales.
- **Principio de abierto/cerrado**: La clase `Order` está cerrada a la modificación pero abierta a la extensión. `DiscountedOrder` la extiende sin tocar el código original.

---

## Ejercicio 21: Jerarquía de clases Vehicle con Bike, Truck y Bus

**Consigna:** Escribe un programa en Python que defina una clase base `Vehicle` y cree las subclases `Bike`, `Truck` y `Bus`, cada una definiendo un atributo `max_speed` único y un método `describe()`.

**Propósito:** Este ejercicio refuerza el concepto de jerarquías de clases y muestra cómo las subclases pueden especializar un modelo compartido con sus propios valores de atributos, reflejando cómo se categorizan los sistemas de transporte del mundo real.

**Entrada dada:** Objetos de las clases `Bike`, `Truck` y `Bus`

**Salida esperada:**

```
Bike max speed: 120 km/h  
Truck max speed: 90 km/h  
Bus max speed: 100 km/h
```

**Pista:**
- Define una clase base `Vehicle` con un atributo `max_speed` establecido en `0` y un método `describe()` que lo imprima.
- Crea las subclases `Bike`, `Truck` y `Bus`, cada una estableciendo su propio `max_speed` en `__init__`.
- Sobrescribe `describe()` en cada subclase, o confía en el método del padre si el formato de salida es el mismo.

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def describe(self):
        print(f"{type(self).__name__} max speed: {self.max_speed} km/h")

class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)

class Bus(Vehicle):
    def __init__(self):
        super().__init__(100)

vehicles = [Bike(), Truck(), Bus()]
for v in vehicles:
    v.describe()
```

- **`class Vehicle`**: Acepta `max_speed` como parámetro y proporciona un método `describe()` compartido usado por todas las subclases.
- **Constructores de las subclases**: Cada subclase fija su propio valor de `max_speed` y lo pasa hacia el padre mediante `super().__init__()`. No se necesitan atributos adicionales en las subclases.
- **`type(self).__name__`**: Dentro del `describe()` de la clase base, esto obtiene el nombre real de la clase en tiempo de ejecución (`Bike`, `Truck` o `Bus`), haciendo el método reutilizable sin necesidad de sobrescribirlo en cada subclase.
- **Recorrer una lista mixta**: Los tres objetos se almacenan en una sola lista y se recorren de manera uniforme, un ejemplo directo de comportamiento polimórfico.

---

## Ejercicio 22: Identificar la clase de un objeto usando type()

**Consigna:** Escribe un programa en Python que cree objetos de múltiples clases y use la función incorporada `type()` para identificar a qué clase pertenece cada objeto.

**Propósito:** Este ejercicio enseña cómo Python rastrea el tipo de cada objeto en tiempo de ejecución. Entender `type()` es esencial para depurar, para el despacho dinámico, y para escribir código flexible que reaccione de forma distinta según el tipo de objeto que recibe.

**Entrada dada:** Objetos de las clases `Dog`, `Cat` y `Vehicle`

**Salida esperada:**

```
d is of type: Dog  
c is of type: Cat  
v is of type: Vehicle
```

**Pista:**
- Define algunas clases simples (pueden tener cuerpos vacíos usando `pass`).
- Crea un objeto de cada clase.
- Usa `type(obj).__name__` para obtener el nombre de la clase como cadena, o compara `type(obj)` directamente con la clase misma (por ejemplo, `type(obj) == Dog`).

**Solución y explicación:**

```python
class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass

d = Dog()
c = Cat()
v = Vehicle()

objects = {"d": d, "c": c, "v": v}

for name, obj in objects.items():
    print(f"{name} is of type: {type(obj).__name__}")
```

- **`class Dog: pass`**: La palabra clave `pass` crea un cuerpo de clase válido pero vacío. Esto es útil cuando la estructura de la clase no es relevante para el objetivo del ejercicio.
- **`type(obj)`**: Retorna la clase (objeto de tipo) a partir de la cual se creó `obj`. Por ejemplo, `type(d)` retorna `<class '__main__.Dog'>`.
- **`type(obj).__name__`**: El atributo `.__name__` sobre el objeto de tipo retornado da solo el nombre simple de la clase como cadena, como `"Dog"`, sin el prefijo del módulo.
- **Alternativa – `isinstance()`**: Mientras que `type()` verifica la clase exacta, `isinstance(d, Dog)` también retorna `True` para subclases. Usa `type()` cuando necesites una coincidencia exacta, e `isinstance()` cuando la herencia deba tenerse en cuenta.

---

## Ejercicio 23: Verificación de tipos con isinstance() e issubclass()

**Consigna:** Escribe un programa en Python que use `isinstance()` para verificar si un objeto es instancia de una clase dada, y `issubclass()` para verificar si una clase es subclase de otra.

**Propósito:** Este ejercicio enseña dos de las herramientas de inspección de tipos más importantes de Python. A diferencia de `type()`, ambas funciones consideran la herencia, haciéndolas esenciales para escribir código flexible y seguro que maneje tipos de objetos mixtos con elegancia.

**Entrada dada:** Una clase `Dog` que hereda de `Animal`, y una instancia `d = Dog()`

**Salida esperada:**

```
Is d an instance of Dog? True  
Is d an instance of Animal? True  
Is Dog a subclass of Animal? True  
Is Animal a subclass of Dog? False
```

**Pista:**
- Define una clase base `Animal` y una subclase `Dog` que herede de ella.
- Usa `isinstance(obj, ClassName)` para verificar si un objeto es instancia de una clase o de cualquiera de sus clases padre.
- Usa `issubclass(ChildClass, ParentClass)` para verificar si una clase hereda de otra.
- Ten en cuenta que `isinstance(d, Animal)` retorna `True` aunque `d` fue creado desde `Dog`, porque `Dog` hereda de `Animal`.

**Solución y explicación:**

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print("Is d an instance of Dog?", isinstance(d, Dog))
print("Is d an instance of Animal?", isinstance(d, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))
```

- **`isinstance(d, Dog)`**: Retorna `True` porque `d` fue creado directamente a partir de la clase `Dog`.
- **`isinstance(d, Animal)`**: También retorna `True` porque `Dog` hereda de `Animal`. Esta conciencia de la herencia es lo que hace que `isinstance()` sea más útil que una comparación directa con `type()` en la mayoría de los escenarios reales.
- **`issubclass(Dog, Animal)`**: Retorna `True` porque `Dog` está definida con `Animal` como su padre. Esto funciona sobre las clases mismas, no sobre las instancias.
- **`issubclass(Animal, Dog)`**: Retorna `False` porque la relación es unidireccional. El padre no hereda del hijo.

---

## Ejercicio 24: Suma de vectores usando sobrecarga de __add__

**Consigna:** Escribe un programa en Python que cree una clase `Vector` que represente un vector 2D, e implemente el método dunder `__add__` para que dos objetos `Vector` puedan sumarse usando el operador `+`.

**Propósito:** Este ejercicio introduce la sobrecarga de operadores, una potente característica de OOP que permite que tus clases personalizadas se comporten como los tipos incorporados. Implementar `__add__` hace que tus objetos se integren de forma natural con la sintaxis de Python.

**Entrada dada:** `v1 = Vector(2, 3)` y `v2 = Vector(4, 1)`

**Salida esperada:** `Vector(6, 4)`

**Pista:**
- Define una clase `Vector` con atributos `x` e `y` en `__init__`.
- Implementa `__add__(self, other)` para retornar un nuevo `Vector` cuyo `x` sea `self.x + other.x` y cuyo `y` sea `self.y + other.y`.
- Implementa `__repr__` o `__str__` para controlar cómo se imprime el objeto.
- Pruébalo escribiendo `v1 + v2` e imprimiendo el resultado.

**Solución y explicación:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

result = v1 + v2
print(result)
```

- **`__add__(self, other)`**: Python llama a este método automáticamente cuando se usa el operador `+` entre dos objetos `Vector`. `self` es el operando izquierdo y `other` el derecho.
- **Retorna un nuevo `Vector`**: En lugar de modificar `self` en el lugar, el método crea y retorna un objeto `Vector` nuevo. Esto mantiene los objetos inmutables bajo la suma, que es el comportamiento esperado para tipos matemáticos.
- **`__repr__`**: Define la representación en cadena del objeto usada por `print()` y por la consola interactiva. Sin él, `print(result)` mostraría algo como `<__main__.Vector object at 0x...>`.
- **Sobrecarga de operadores**: El mismo patrón aplica a otros operadores, como `__sub__` para `-`, `__mul__` para `*` y `__eq__` para `==`, haciendo que las clases personalizadas se sientan como tipos nativos de Python.

---

## Ejercicio 25: Longitud del carrito usando sobrecarga de __len__

**Consigna:** Escribe un programa en Python que cree una clase `Cart` que almacene una lista de artículos, e implemente `__len__` para que al llamar `len(cart)` se retorne la cantidad de artículos actualmente en el carrito.

**Propósito:** Este ejercicio introduce el método dunder `__len__`, que permite que tu clase personalizada se integre con la función incorporada `len()` de Python. Esto forma parte del modelo de datos de Python y hace que tus objetos se comporten como secuencias o contenedores nativos.

**Entrada dada:** Un carrito con los artículos `["apple", "banana", "mango"]`

**Salida esperada:** `Number of items in cart: 3`

**Pista:**
- Define una clase `Cart` con un `__init__` que inicialice una lista vacía `self.items = []`.
- Agrega un método `add_item(item)` que agregue elementos a `self.items`.
- Implementa `__len__(self)` para retornar `len(self.items)`.
- Una vez definido `__len__`, Python lo usará automáticamente cada vez que llames a `len(cart)` sobre tu objeto.

**Solución y explicación:**

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = Cart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("mango")

print("Number of items in cart:", len(cart))
```

- **`self.items = []`**: Inicializa la lista interna que almacena el contenido del carrito. Cada instancia obtiene su propia lista independiente.
- **`__len__(self)`**: Python llama a esto automáticamente cuando se usa `len(cart)`. Delega en el `len()` incorporado sobre la lista interna, que ya sabe cómo contar sus elementos.
- **Diseño basado en protocolo**: Al implementar `__len__`, tu objeto `Cart` ahora participa en el protocolo de secuencias de Python. Esto también habilita verificaciones de veracidad: un objeto cuyo `__len__` retorna `0` se trata como `False` en un contexto booleano.
- **Métodos dunder relacionados**: Puedes extender este patrón con `__getitem__` para soportar indexado (por ejemplo, `cart[0]`) y con `__iter__` para soportar recorrer el carrito directamente.

---

## Ejercicio 26: Saldo privado con getter y setter de propiedad

**Consigna:** Escribe un programa en Python que cree una clase `BankAccount` donde el saldo se almacene como un atributo privado `__balance`, y se exponga de forma segura mediante un getter con `@property` y un setter que valide el valor antes de actualizarlo.

**Propósito:** Este ejercicio demuestra el encapsulamiento, uno de los cuatro pilares de la OOP. Usar atributos privados con "name mangling" junto con `@property` te permite controlar cómo el código externo lee y modifica el estado interno, evitando que se asignen datos inválidos.

**Entrada dada:** `BankAccount(1000)`, luego un depósito de `500`, y luego un intento de fijar el saldo en `-200`

**Salida esperada:**

```
Current balance: 1000  
Current balance: 1500  
Invalid balance. Must be non-negative.
```

**Pista:**
- Almacena el saldo como `self.__balance` en `__init__`. El doble guion bajo activa el "name mangling" de Python, dificultando el acceso directo desde fuera de la clase.
- Define un método `@property` llamado `balance` que retorne `self.__balance`.
- Define un `@balance.setter` que verifique si el nuevo valor es no negativo antes de asignarlo, e imprima un mensaje de error si no lo es.
- Agrega un método `deposit(amount)` que actualice el saldo usando el setter: `self.balance = self.__balance + amount`.

**Solución y explicación:**

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid balance. Must be non-negative.")
        else:
            self.__balance = amount

    def deposit(self, amount):
        self.balance = self.__balance + amount

account = BankAccount(1000)
print("Current balance:", account.balance)

account.deposit(500)
print("Current balance:", account.balance)

account.balance = -200
```

- **`self.__balance`**: El prefijo de doble guion bajo activa el "name mangling". Python internamente renombra esto a `_BankAccount__balance`, haciéndolo inaccesible como `account.__balance` desde fuera de la clase.
- **`@property`**: Convierte al método `balance` en un accesor de solo lectura tipo atributo. Quien lo llama escribe `account.balance` en lugar de `account.balance()`.
- **`@balance.setter`**: Intercepta cualquier asignación a `account.balance = valor` y ejecuta la lógica de validación antes de actualizar `__balance`. Aquí es donde se hacen cumplir las reglas de negocio.
- **`deposit()` usa el setter**: Al escribir `self.balance = ...` dentro del método en lugar de `self.__balance = ...`, la operación de depósito sigue pasando por la lógica de validación, manteniendo las reglas consistentes.

---

## Ejercicio 27: Clase de objeto invocable usando __call__

**Consigna:** Escribe un programa en Python que cree una clase `Multiplier` que almacene un factor, e implemente `__call__` para que una instancia de la clase pueda invocarse directamente como una función, multiplicando un número dado por ese factor.

**Propósito:** Este ejercicio introduce el método dunder `__call__`, que hace que cualquier objeto sea invocable. Este patrón se usa comúnmente en machine learning (objetos de capas), decoradores, y en cualquier lugar donde necesites un objeto con estado similar a una función.

**Entrada dada:** `Multiplier(3)` invocado con `10`, y `Multiplier(5)` invocado con `7`

**Salida esperada:**

```
30  
35
```

**Pista:**
- Define una clase `Multiplier` con un `__init__` que almacene el factor como `self.factor`.
- Implementa `__call__(self, value)` para retornar `self.factor * value`.
- Crea una instancia con `triple = Multiplier(3)`, y luego invócala como una función: `triple(10)`.

**Solución y explicación:**

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

triple = Multiplier(3)
penta = Multiplier(5)

print(triple(10))
print(penta(7))
```

- **`self.factor`**: Almacena el valor multiplicador al momento de la construcción. Este es el estado que distingue a los objetos invocables de las funciones simples: el objeto recuerda su configuración entre invocaciones.
- **`__call__(self, value)`**: Python invoca este método cada vez que el objeto se llama usando paréntesis, como en `triple(10)`. Sin este método, hacerlo lanzaría un `TypeError: 'Multiplier' object is not callable`.
- **Objetos invocables vs. funciones simples**: Una función regular no puede mantener estado persistente entre llamadas sin usar variables globales o clausuras. Una instancia de clase invocable almacena ese estado de forma limpia en sus atributos.
- **Uso en el mundo real**: Este patrón se usa extensamente en frameworks como PyTorch, donde las capas de redes neuronales son objetos invocables que almacenan pesos como atributos de instancia y procesan datos de entrada a través de `__call__`.

---

## Ejercicio 28: Clase Flight con verificación de capacidad de pasajeros

**Consigna:** Escribe un programa en Python que cree una clase `Passenger` y una clase `Flight`. La clase `Flight` debe gestionar una lista de objetos `Passenger` y bloquear nuevas reservas cuando se alcance la capacidad de asientos.

**Propósito:** Este ejercicio modela un escenario real de composición de objetos, donde una clase posee y gestiona una colección de otra clase. También enseña la imposición de límites, donde las reglas de negocio (límites de capacidad) se integran directamente en los métodos de la clase.

**Entrada dada:** Un `Flight` con capacidad `2`, y luego tres intentos de reserva

**Salida esperada:**

```
Alice booked on Flight AI202.  
Bob booked on Flight AI202.  
Sorry, Flight AI202 is fully booked.
```

**Pista:**
- Define una clase `Passenger` con un atributo `name`.
- Define una clase `Flight` con `flight_number`, `capacity`, y una lista vacía `passengers` en `__init__`.
- Agrega un método `book(passenger)` que verifique `len(self.passengers) < self.capacity` antes de agregar.
- Imprime un mensaje de confirmación en caso de éxito, o un mensaje de "vuelo completo" cuando se supere la capacidad.

**Solución y explicación:**

```python
class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def book(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} booked on Flight {self.flight_number}.")
        else:
            print(f"Sorry, Flight {self.flight_number} is fully booked.")

flight = Flight("AI202", 2)
flight.book(Passenger("Alice"))
flight.book(Passenger("Bob"))
flight.book(Passenger("Charlie"))
```

- **`class Passenger`**: Una clase de datos simple que contiene el nombre de un pasajero. En un sistema más grande, también podría almacenar un número de pasaporte, preferencia de asiento o referencia de reserva.
- **`self.passengers = []`**: Cada instancia de `Flight` mantiene su propia lista. Esto es composición de objetos: el `Flight` posee una colección de objetos `Passenger`.
- **Verificación de capacidad en `book()`**: La condición de guardia `len(self.passengers) < self.capacity` impone la regla de negocio en el punto de ingreso de datos, evitando que la lista crezca más allá de su límite.
- **Pasar objetos como argumentos**: `flight.book(Passenger("Alice"))` crea un objeto `Passenger` en línea y lo pasa directamente. El método de `Flight` luego trabaja con los atributos del objeto, demostrando la comunicación entre objetos.

---

## Ejercicio 29: Clase Zoo que alimenta a todos los animales

**Consigna:** Escribe un programa en Python que defina una clase base `Animal` con un método `eat()`, cree algunas subclases con sus propias implementaciones de `eat()`, y construya una clase `Zoo` que mantenga una lista de animales y llame a `eat()` en todos ellos mediante un método `feed_all()`.

**Propósito:** Este ejercicio combina composición con polimorfismo. La clase `Zoo` no necesita saber el tipo específico de cada animal; simplemente llama a la interfaz compartida `eat()` en cada objeto de su colección, y cada animal responde a su manera.

**Entrada dada:** Un zoológico con un `Lion`, un `Elephant` y un `Parrot`

**Salida esperada:**

```
Lion eats meat.  
Elephant eats grass.  
Parrot eats seeds.
```

**Pista:**
- Define una clase base `Animal` con un método `eat()` que retorne una cadena genérica.
- Crea las subclases `Lion`, `Elephant` y `Parrot`, cada una sobrescribiendo `eat()` con un mensaje específico.
- Define una clase `Zoo` con un método `add_animal(animal)` y un método `feed_all()` que recorra todos los animales almacenados y llame a `eat()` en cada uno.

**Solución y explicación:**

```python
class Animal:
    def eat(self):
        return "eating."

class Lion(Animal):
    def eat(self):
        return "Lion eats meat."

class Elephant(Animal):
    def eat(self):
        return "Elephant eats grass."

class Parrot(Animal):
    def eat(self):
        return "Parrot eats seeds."

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        for animal in self.animals:
            print(animal.eat())

zoo = Zoo()
zoo.add_animal(Lion())
zoo.add_animal(Elephant())
zoo.add_animal(Parrot())

zoo.feed_all()
```

- **`class Zoo`**: Actúa como clase contenedora que gestiona una colección heterogénea de objetos `Animal`. No le importa el subtipo específico de cada animal que contiene.
- **`feed_all()`**: Recorre `self.animals` y llama a `eat()` en cada uno. Como cada animal sobrescribe `eat()`, Python despacha automáticamente al método correcto de la subclase. Esto es polimorfismo en tiempo de ejecución.
- **Composición sobre herencia**: `Zoo` no hereda de `Animal`. En cambio, contiene animales. Esto es una relación "tiene un", a diferencia de la relación "es un" de la herencia.
- **Extensibilidad**: Agregar un nuevo tipo de animal (por ejemplo, `Penguin`) solo requiere crear una nueva subclase con su propio `eat()`. El código de `Zoo` y `feed_all()` no necesita cambios.

---

## Ejercicio 30: Clase Character con lógica automática de subida de nivel

**Consigna:** Escribe un programa en Python que cree una clase `Character` con atributos `health`, `exp` y `level`. El personaje debe subir de nivel automáticamente y reiniciar la experiencia (`exp`) cada vez que la experiencia acumulada alcance o supere 100.

**Propósito:** Este ejercicio muestra cómo integrar lógica de videojuego directamente en una clase usando un método que gestiona transiciones de estado. También demuestra cómo manejar el excedente (experiencia sobrante después de subir de nivel) y mantener sincronizados varios atributos relacionados.

**Entrada dada:** `Character("Aria", health=100)`, y luego `gain_exp(60)` dos veces

**Salida esperada:**

```
Aria gained 60 exp. (Total: 60)  
Aria gained 60 exp. Level up! Now Level 2. (Remaining exp: 20)
```

**Pista:**
- Define `Character.__init__` con `name`, `health`, y establece `self.exp = 0` y `self.level = 1` como valores por defecto.
- En `gain_exp(amount)`, suma `amount` a `self.exp`, y luego verifica si `self.exp >= 100`.
- Si ocurre una subida de nivel, incrementa `self.level`, resta 100 de `self.exp` para trasladar el remanente, e imprime el mensaje de subida de nivel.
- Si no ocurre una subida de nivel, imprime un mensaje más simple mostrando el total actual de experiencia.

**Solución y explicación:**

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} gained {amount} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
        else:
            print(f"{self.name} gained {amount} exp. (Total: {self.exp})")

hero = Character("Aria", health=100)
hero.gain_exp(60)
hero.gain_exp(60)
```

- **`self.exp = 0` y `self.level = 1`**: Estos valores por defecto se establecen en `__init__` en lugar de pasarse como parámetros, ya que es razonable que todo personaje nuevo comience en nivel 1 con cero experiencia.
- **`self.exp += amount`**: Acumula experiencia a través de múltiples llamadas. El total acumulado se verifica después de cada ganancia, no solo una vez.
- **`self.exp -= 100`**: Resta exactamente 100 en lugar de reiniciar a cero, de modo que cualquier experiencia ganada por encima del umbral se traslada al siguiente nivel. Por ejemplo, ganar 60 de experiencia sobre otros 60 da un total de 120; después de subir de nivel, quedan 20 de experiencia.
- **Extender la lógica**: Este patrón admite múltiples subidas de nivel en una sola llamada (por ejemplo, ganar 250 de experiencia de una vez) cambiando el `if` por un bucle `while self.exp >= 100`, haciendo el sistema robusto ante grandes recompensas de experiencia.

---

## Ejercicio 31: Clase Playlist con agregar, quitar y mezclar

**Consigna:** Escribe un programa en Python que defina una clase `Song` y una clase `Playlist`. La `Playlist` debe permitir agregar canciones, eliminar canciones por título, y mezclar el orden de la lista de forma aleatoria.

**Propósito:** Este ejercicio refuerza la composición de objetos, la manipulación de listas y el uso de la biblioteca estándar. Gestionar una colección de objetos con operaciones de agregar, quitar y reordenar es un patrón presente en reproductores multimedia, gestores de tareas y muchas aplicaciones del mundo real.

**Entrada dada:** Una playlist con tres canciones, luego una eliminación y un mezclado

**Salida esperada:**

```
Playlist: Blinding Lights, Levitating, Peaches  
Removed: Levitating  
After shuffle: (order will vary)
```

**Pista:**
- Define una clase `Song` con atributos `title` y `artist`.
- Define una clase `Playlist` con una lista interna `self.songs = []` y un método `add_song(song)` que agregue elementos a ella.
- En `remove_song(title)`, usa una comprensión de listas para filtrar la canción cuyo `title` coincida con la cadena dada.
- En `shuffle()`, usa `random.shuffle(self.songs)` del módulo `random` para aleatorizar el orden en el lugar.

**Solución y explicación:**

```python
import random

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, title):
        original_count = len(self.songs)
        self.songs = [s for s in self.songs if s.title != title]
        if len(self.songs) < original_count:
            print(f"Removed: {title}")
        else:
            print(f"Song '{title}' not found in playlist.")

    def shuffle(self):
        random.shuffle(self.songs)

    def display(self):
        titles = [s.title for s in self.songs]
        print(f"Playlist: {', '.join(titles)}")

playlist = Playlist("My Mix")
playlist.add_song(Song("Blinding Lights", "The Weeknd"))
playlist.add_song(Song("Levitating", "Dua Lipa"))
playlist.add_song(Song("Peaches", "Justin Bieber"))

playlist.display()
playlist.remove_song("Levitating")
playlist.shuffle()
print("After shuffle:", end=" ")
playlist.display()
```

- **`class Song`**: Un objeto de datos ligero que contiene el `title` y el `artist` de una canción. La `Playlist` almacena estos objetos en lugar de simples cadenas, facilitando mostrar o filtrar por cualquiera de los dos atributos.
- **`remove_song()` con comprensión de listas**: `[s for s in self.songs if s.title != title]` construye una nueva lista que excluye la canción coincidente y la reasigna a `self.songs`. Comparar el conteo antes y después confirma si realmente ocurrió una eliminación.
- **`random.shuffle(self.songs)`**: Mezcla la lista en el lugar, lo que significa que no se crea ninguna lista nueva. El orden de `self.songs` se aleatoriza directamente, y la salida será distinta en cada ejecución.
- **`display()`**: Usa una comprensión de listas para extraer solo los títulos y los une con `', '.join()`, produciendo un resumen limpio de una sola línea del estado actual de la playlist.
