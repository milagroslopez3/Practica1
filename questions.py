import random
categories = {"datos" : ["cadena","entero","lista"] , 
     "lenguaje" : ["python"]  , 
     "conceptos" : ["variable", "funcion", "bucle", "programa" ]}
used_words = []
total_score = 0
while True:
    for clave in categories:
        print(clave)
    cat = (input("Elegir una categoria")).lower().strip()
    available =  [p for p in categories[cat] if p not in used_words]
    if not available:
        print(f"¡Ya usaste todas las palabras de '{cat}'! Elegí otra.")
        continue
    word = random.sample(available,1)[0] #[0] porque la funcion devuelve una lista
    used_words.append(word)
    guessed = []
    attempts = 6
    score = 0
    print("¡Bienvenido al Ahorcado!")
    print()
    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            score += 6
            total_score += score
            print("¡Ganaste!")
            print (f"Tu puntaje es {score}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ").lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            print ('Entrada no valida')
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        score = 0
        print(f"¡Perdiste! La palabra era: {word}")
        print (f"Tu puntaje es {score}")
    if input("\nEscriba 'jugar' para empezar otra partida o 'fin' para terminar:").lower() != 'jugar':
        break
print(f"\nJuego terminado. Puntaje final {total_score}")

