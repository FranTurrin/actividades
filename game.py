import random
# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos
max_failures = 10

# Contador de fallos
failures = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

letters = []

# Lista de vocales
vocales = ["a","e","i","o","u"]

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

print("Facil:1 ; Medio:2 ; Difícil:3")
dificultad = int(input("Elija un nivel de dificultad: "))

# Dificultad dos(se muestra la última y primera letra)
if dificultad == 2:
    for letter in secret_word:
        letters.append("_")
    letters[0] = secret_word[0]             
    letters[-1] = secret_word[-1]
    word_displayed = "".join(letters)
    print(f"Palabra : {word_displayed}")
    guessed_letters.extend([secret_word[0],secret_word[-1]])
elif dificultad == 1:           # Dificultad uno(se muestran las vocales)
    guessed_letters.extend(vocales)
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra : {word_displayed}")
else:               # Dificultad tres o si se ingreso cualquier otro número(no se muestra nada)
    word_displayed = "_" * len(secret_word)
    print(f"Palabra : {word_displayed}")
        
while failures != max_failures:
     
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     
     # Verifico si se ingreso un caracter vacio
     if letter == "" or letter == " ":
        print("No has ingresado una palabra. Intentalo de nuevo")
        continue
     
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         failures = failures + 1
     
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has agotado tus {max_failures} fallos.")
     print(f"La palabra secreta era: {secret_word}")

# En la dificultad media no puede lograr que por ejemplo en la palabra inteligencia se muestre solo la primer letra "i", se muestran todas en la palabra