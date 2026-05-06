print("Você foi capturado por um goblin do mal...")
print("Saia da cela e ache um jeito de escapar!")

def nome_classe():
    print("Escolha sua classe:")
    print("1 - Mago")
    print("2 - Elfa")
    print("3 - Samurai")
          
    while True:
        classe = input("digite o número da classe")

        if classe == "1":
            return "Mago"
        elif classe == "2":
            return "Elfa"
        elif classe == "3":
            return "Samurai"
        else:
            print("ops, opção invalida, escolha uma das opçoes acima")

classe_selecionada = nome_classe()

def caminho_mago():
 print(f"\nVocê escolheu a classe {classe_selecionada}")
 print("\nO que voce faz?")
 print("1 - olhar em volta e analisar o ambiente")
 print("2 - gritar como se estivesse agonizando de dor")
 print("3 - lançar um feitiço de fogo no goblin que está dormindo")

escolha_mago = input("digite o número da opção")

if escolha_mago == "1":
    print("\nVocê viu uma chave pendurada no pescoço do goblin que está dormindo.")
