print("Você foi capturado por um goblin do mal...")
print("Saia da cela e ache um jeito de escapar do castelo!")

def nome_classe():
    print("\nEscolha sua classe:")
    print("1 - Mago")
    print("2 - Elfa")
    print("3 - Samurai")

    while True:
        classe = input("Digite o número da classe: ")

        if classe == "1":
            return "Mago"
        elif classe == "2":
            return "Elfa"
        elif classe == "3":
            return "Samurai"
        else:
            print("Opção inválida, tente novamente.")

def caminho_mago():
    print("\nVocê escolheu a classe Mago")
    print("\nO que você faz?")
    print("1 - Olhar em volta e analisar o ambiente")
    print("2 - Gritar como se estivesse agonizando de dor")
    print("3 - Lançar um feitiço de fogo no goblin que está dormindo")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        print("\nVocê observou que tem uma chave pendurada no pescoço do guarda goblin que está dormindo.")
        
        print("\nO que você faz agora?")
        print("1 - Usar magia de nível 1")
        print("2 - Usar magia de nível 2")
        print("3 - Usar magia de nível 3")
        escolha2 = input("Digite o número da opção: ")

        if escolha2 == "1":
            print("\nVocê usou uma magia semelhante a telecinese e executou na chave que trouxe até você flutuando sem fazer barulho, você abre sua cela e recupera seu livro de magia(buff), o que te permite teleportar pra fora do castelo")
            print("Você conseguiu concluir o objetivo.🎉 VOCÊ ESCAPOU!")
        elif escolha2 == "2":
            print("\nA porta faz barulho...")
            print("O goblin acorda e te mata. Fim de jogo.")
        else:
            print("Opção inválida.")
            
    elif escolha == "2":
        print("\nO goblin acorda e te ataca... Fim de jogo.")
    elif escolha == "3":
        print("\nO goblin acorda assustado e te mata... Fim de jogo.")
    else:
        print("Opção inválida.")

classe_selecionada = nome_classe()

if classe_selecionada == "Mago":
    caminho_mago()
elif classe_selecionada == "Elfa":
    print("\nCaminho da Elfa ainda não foi criado...")
elif classe_selecionada == "Samurai":
    print("\nCaminho do Samurai ainda não foi criado...")