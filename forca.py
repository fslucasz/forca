import random

def jogar_forca():
    palavras = ["python", "programacao", "computador", "dados", "desenvolvimento"]
    palavra_secreta = random.choice(palavras)
    letras_certas = []
    tentativas_maximas = 6
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")

    while erros < tentativas_maximas:
        # Mostra a palavra com letras acertadas e traços para as ocultas
        palavra_mostrada = ""
        for letra in palavra_secreta:
            if letra in letras_certas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "_ "

        print("\nPalavra:", palavra_mostrada.strip())

        # Verifica se o jogador venceu
        if "_" not in palavra_mostrada:
            print("")
            print("Parabéns, você ganhou!")
            break

        print("")

        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_certas:
            print("")
            print("Você já tentou esta letra.")
            continue

        if palpite in palavra_secreta:
            letras_certas.append(palpite)
            print("")
            print("Boa! Letra correta.")
        else:
            erros += 1
            print("")
            print(f"Letra errada! Tentativas restantes: {tentativas_maximas - erros}")

    if erros == tentativas_maximas:
        print("")
        print(f"\nFim de jogo! Você perdeu. A palavra era: {palavra_secreta}")

jogar_forca()