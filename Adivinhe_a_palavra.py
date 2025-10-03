import random
lista_de_palavras = [
    "amigo", "banana", "carro", "feliz", "gato", "livro", "porta", "quadro", "sorriso", "tigre",
    "verde", "abacate", "bolacha", "cachorro", "dedal", "elefante", "foca", "girafa", "hotel", "igreja",
    "janela", "kiwi", "limão", "morango", "navio", "ocelote", "piano", "quente", "rosa", "sapato",
    "tulipa", "uva", "vaca", "xadrez", "yoga", "zebra", "alface", "biscoito", "camelo", "dente", "escada",
    "festa", "garfo", "horta", "ilha", "jornal", "lousa", "mesa", "noite", "olhos", "pente"
]

palavra = random.choice(lista_de_palavras) #escolhemos uma palavra aleatoria da lista para dar valor a variável palavra

palavra_adivinhada = ['_'] * len(palavra) 
tentativas = 10

while tentativas > 0:
    print("\nPalavra atual: " + ' '.join(palavra_adivinhada))
    chute = input("Digite uma letra: ").lower()
    
    acertou = False
    if chute in palavra:
        for i in range(len(palavra)):
            if palavra[i] == chute and palavra_adivinhada[i] == '_':
                palavra_adivinhada[i] = chute
                acertou = True
        if acertou:
            print("Acertou!")
        else:
            print("Você já tentou essa letra.")
    else:
        tentativas -= 1
        print("Chute errado! tentativas restantes: " + str(tentativas))
    
    if '_' not in palavra_adivinhada:
        print(f"Parabens, voce adivinhou a palavra!: {palavra}")
        break
    if tentativas == 0 and '_' in palavra_adivinhada:
        print(f"As tentativas acabaram: a palavra era: {palavra}")
        break