import random

def generate_random_list(words):
    random.shuffle(words)
    return words

def main():
    print("¡Bienvenido al aleatorizador de listas!")
    print("Introduce tu lista (separado por comas)")
    words_input = input().strip()
    words = [word.strip() for word in words_input.split(",")]
    random_list = generate_random_list(words)
    print("Lista aleatorizada:")
    for word in random_list:
        print(word)

if __name__ == "__main__":
    main()
    