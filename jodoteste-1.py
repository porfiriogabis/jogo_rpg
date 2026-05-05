def inicio():
    print("Escolha o gênero do seu personagem!")
    print("Você chega à cena do crime. O que deseja fazer?")
    print("1 - Examinar o corpo")
    print("2 - Interrogar testemunhas")

    escolha = input("Escolha: ")

    if escolha == "1":
        examinar_corpo()
    elif escolha == "2":
        interrogar()            
    else:
        print("Escolha inválida.")
        inicio()


def examinar_corpo():
    print("\nVocê encontra uma pista: um bilhete suspeito.")
    print("1 - Ler o bilhete")
    print("2 - Ignorar e sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        final_bom()
    else:
        final_ruim()


def interrogar():
    print("\nA testemunha parece nervosa.")
    print("1 - Pressionar")
    print("2 - Acalmar")

    escolha = input("Escolha: ")

    if escolha == "1":
        final_ruim()
    else:
        final_bom()


def final_bom():
    print("\nVocê resolveu o caso! Parabéns, detetive!")


def final_ruim():
    print("\nO culpado escapou... Caso encerrado sem solução.")

inicio()
