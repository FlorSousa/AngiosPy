import os
from Starter import *
from ChaveC import *
from ChaveB import *
from ChaveA import *

# Função que limpa o display do terminal
clear = lambda: os.system('cls')
Pasta = os.path.dirname(os.path.abspath(__file__))
FamiliasCaminho = os.path.join(Pasta, 'familias.txt')
BiomasCaminho = os.path.join(Pasta, 'biomas.txt')

class MenuPrincipal():
    def __init__(self):
        self.estado = False
        self.FirstLoad = True
        self.Buffer = []
        self.conta = 0

    # Funções responsaveis por atuar na classificação,busca,registro de plantas como também de mostra devs e dar a chance de sair

    # Muda a variavel estado para falso e encerra o loop
    def Encerra(self):
        if len(self.Buffer) > 0:
            FamiliasTXT = open(FamiliasCaminho, "r", encoding="UTF-8")
            listaLinhas = FamiliasTXT.readlines()
            for atual in self.Buffer:
                novo = atual[0]
                for linha in listaLinhas:
                    linha = linha.strip().split("#")
                    Familia = linha[1]
                    if atual[1] == Familia:
                        try:
                            lista = "#".join(linha) + " " + novo + "; " + "\n"
                            listaLinhas[self.conta] = lista
                            FamiliasTXT = open(FamiliasCaminho, "w", encoding="UTF-8")
                            FamiliasTXT.writelines(listaLinhas)
                            FamiliasTXT.close()
                            #print(self.conta)
                            self.conta = 0
                            break
                        except:
                            Err = input("\n Ocorreu um erro ao tentar salvar o arquivo, aperte qualquer tecla para fechar\no programa")
                            if Err:
                                break
                    else:
                        self.conta = self.conta + 1
                self.estado = False    
        else:
            # encerra o programa
            self.estado = False


    # Verifica Qual a chave e redireciona para o algoritmo de classificação
    def Classifica(self):
        EntradaChave = input("A.Flores aclamídeas ou monoclamídeas (CHAVE A)\nB.Flores diclamídeas dialipétalas(CHAVE B)\nC.Flores diclamídeas gamopétalas(CHAVE C)\nDigite a chave (A/B/C) ou aperte (S) para sair e (V) para Voltar:\n").upper()

        if EntradaChave == "A":
            callback = "Resultado:\n"+encontra_familia_chave_A()
            print(callback)
            EntradaChaveFinal = input("\nA.Efetuar Registro\nB.Para voltar\nC.Para Fechar Programa\n").upper()
            if EntradaChaveFinal == "B":
                clear()
                self.Inicio()
            elif EntradaChaveFinal == "A":
                self.registra(callback)
            else:
                self.Encerra()

        elif EntradaChave == "B":
            callback = "Resultado:\n"+encontra_familia_chave_B()
            print(" ")
            print(callback)
            EntradaChaveFinal = input("\nA.Efetuar Registro\nB.Para voltar\nC.Para Fechar Programa\n").upper()
            if EntradaChaveFinal == "B":
                clear()
                self.Inicio()
            elif EntradaChaveFinal == "A":
                self.registra(callback)
            else:
                self.Encerra()

        elif EntradaChave == "C":
            callback = "Resultado:\n"+encontra_familia_chave_C()
            print(" ")
            print(callback)
            if callback[11] == "F":
                EntradaChaveFinal = input("\nA.Efetuar Registro\nB.Para voltar\nC.Para Fechar Programa\n").upper()
                if EntradaChaveFinal == "B":
                    clear()
                    self.Inicio()
                elif EntradaChaveFinal == "A":
                    self.registra(callback)
                else:
                    self.Encerra()
            else:
                pass
        elif EntradaChave == "V":
            self.Inicio()
        else:
            self.Encerra()
        
    # Verifica o tipo de busca e redereciona para o algoritmo de busca
    def Busca(self):
        clear()
        EntradaBusca = input("A.Busca por Bioma\nB.Busca por Família\nC.Exibe todas as Famílias do Sistema\nV.Voltar\n").upper()
        if EntradaBusca == "A":
            self.buscaBioma()
        elif EntradaBusca == "B":
            self.buscaFamilia()
        elif EntradaBusca == "C":
            self.Familias_chave()
        else:
            self.Inicio()
    
     #Verifica todas famílias presentes na chave
    def Familias_chave(self):
        lista_familias = []
        arquivoFamilias = open(FamiliasCaminho, "r", encoding="UTF-8")
        Familias = arquivoFamilias.readlines()
        arquivoFamilias.close()
        for k in Familias:
            k = k.split("#")
            nomeFamilia = k[1]
            lista_familias.append(nomeFamilia)
        for k in lista_familias:
            print(k)

    # Mostra o nome dos desenvolvedores
    def Desenvolvedores(self):
        clear()
        print("\n" + "#" * 50)
        print("\nMaria Bárbara - Biotecnologia")
        print("Gustavo Oliveira - Biotecnologia")
        print("Jhonatas Flor - Ciencia da Computação\n")
        print("\n" + "#" * 50 + "\n")
        EntradaDevs = input("A.Voltar Menu Principal\nB.Sair do programa\n").upper()
        if EntradaDevs == "A":
            clear()
            self.Inicio()
        else:
            self.Encerra()

    def registra(self, nomeFamilia):
        nomePlanta = input("Digite o nome da Planta: ")
        nomeFamilia = nomeFamilia.split(" ")
        nomeFamilia = nomeFamilia[1]
        self.Buffer.append([nomePlanta, nomeFamilia])
    

        EntradaFinal = input("A.Voltar\nB.Sair\n")
        if EntradaFinal == "A":
            self.Inicio()
        else:
            self.Encerra()

    def buscaBioma(self):
        BiomaArquivo = open(BiomasCaminho, "r", encoding="UTF-8")
        BiomaEntrada = input("Digite o bioma brasileiro:\nExemplos de entrada:Amazônia,Mata Atlântica\n>>>> ").capitalize()
        Biomas = BiomaArquivo.readlines()
        BiomaArquivo.close()
        contador = 0
        for k in Biomas:
            k = k.split("#")
            Bioma = k[0]
            Familias = k[1].split(",")
            if contador < len(Biomas)-1:
                if Bioma == BiomaEntrada:
                    print("Estas são algumas Familias da %s" % BiomaEntrada + ":")
                    for nome in Familias:
                        print(nome)
                else:
                    contador = contador + 1
            else:
                if Bioma == BiomaEntrada:
                    print("Estas são algumas Familias da %s" % BiomaEntrada + ":")
                    for nome in Familias:
                        print(nome)
                else:
                    print("#"*24)
                    print("# Bioma não encontrado #")
                    print("#    tente novamente   #")
                    print("#"*24)
        EntradaFinal = input("A.Voltar\nB.Sair").upper()
        if EntradaFinal == "A":
            self.Inicio()
        else:
            self.Encerra()
        BiomaArquivo.close()

    def buscaFamilia(self):
        FamiliaArquivo = open(FamiliasCaminho, "r", encoding="UTF-8")
        FamiliaEntrada = input("Digite o nome da familia: \nExemplos de entrada:Fabaceae(Leguminosae), Malvaceae\n>>>>")
        familias = FamiliaArquivo.readlines()

        FamiliaArquivo.close()
        contador = 0
        for familia in familias:
            dados_familia = familia.split("#")
            nome_familia = dados_familia[1]
            caracteristicas_familia = dados_familia[2]
            exemplos_familia = dados_familia[3]
            if contador < len(familias)-1:
                if FamiliaEntrada.strip().lower() == nome_familia.strip().lower():
                    clear()
                    print("\nResultados:")
                    print("\n" + caracteristicas_familia)
                    print("\n" + exemplos_familia)
                else:
                    contador = contador +1
            else:
                if FamiliaEntrada.strip().lower() == nome_familia.strip().lower():
                    clear()
                    print("\nResultados:")
                    print("\n" + caracteristicas_familia)
                    print("\n" + exemplos_familia)
                else:
                    print("#"*21)
                    print("# Não há informações #")
                    print("#  tente novamente  #")
                    print("#"*21)
        EntradaFinal = input("A.Voltar\nB.Sair").upper()
        if EntradaFinal == "A":
            self.Inicio()
        else:
            self.Encerra()
    
    '''
    Responsavel por renderizar a arte da folha junto com o nome, também muda a variavel de estado FirstLoad e impede que a arte
    apareça novamente, é responsavel por iniciar o loop while
    '''

    def Begin(self):
        clear()
        self.estado = True
        # chama função de renderizar folha
        DesenhaLogo()
        self.FirstLoad = False

    '''
    Encaminha para onde deve seguir pelas decisões tomada no metodo self.inicio()
    '''

    def EscolhaMenuPrincipal(self, Selecionado):
        if Selecionado == "A":
            self.Classifica()
        elif Selecionado == "B":
            self.Busca()
        elif Selecionado == "C":
            self.Desenvolvedores()
        else:
            self.Encerra()

    '''        
    Metodo da classe que é chamado ao iniciar o loop, é responsavel por gerenciar as escolhas iniciais e direcionar para um metodo
    encaminhador
    '''

    def Inicio(self):
        print("\n" + " " * 30 + "#" * 20 + " ANGIOSPY " + "#" * 20)
        entradaInicio = input(
            " " * 30 + "#" + " " * 6 + "Aperte Qualquer Tecla Para Continuar" + " " * 6 + "#" + "\n" + " " * 30 + "#" + " " * 20 + "V0.0.1" + " " * 22 + "#" + "\n" + " " * 30 + "#" * 50 + "\n" + " " * 30)
        if entradaInicio or entradaInicio == "":
            EntradaEscolha = input("A.Classificação\nB.Busca\nC.Desenvolvedores\nD.Sair\n").upper()
            if EntradaEscolha == "A" or EntradaEscolha == "B" or EntradaEscolha == "C" or EntradaEscolha == "D":
                self.EscolhaMenuPrincipal(EntradaEscolha)


Menu = MenuPrincipal()
Menu.Begin()
while (Menu.estado):
    Menu.Inicio()
