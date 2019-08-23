# Trabalho Final - Avaliação Atleta
# Versão Final - 08/07/2019 Noite
# Leonardo Soares Duarte
# ARQUIVO DE CLASSES DO ATLETA / CLUBE

from atleta_final_arqvs import arquivos
from atleta_final_msgs import mensagens

# CLASSE PARA NOMES DE ATLETAS
class atleta:
    def __init__(self):
        self.nome = self.setNome('nome')
        self.salto_0 = 0.0

    # RETORNA VALORES
    def getNome(self):
        return self.nome

    def getSalto(self):
        return self.salto

    # ALTERA VALORES
    def setNome(self, nome):
        self.nome = nome

    def setSalto(self, salto):
        self.salto = salto

    # GERADOR DE SALTOS PARA EVITAR DIGITAR VARIOS SALTOS
    def saltoGen(self):
        import random
        salto_rand = random.uniform(4.50, 8.99)
        return round(salto_rand, 2)

    # ADICIONA ATLETA NO DICIONARIO "VARLISTA"
    def addAtleta(self, dicio):
        dicio[self.getNome()] = []

    # VERIFICAÇÃO PARA CANCELAMENTO DE FUNÇÃO
    def confirmaInput(self):
        entrad = input(mensagens().getEntrada1()).capitalize()
        if entrad == '' or entrad == ' ' or entrad == '  ':
            mensagens().getMsg4()
            return '001'
        else:
            return entrad

    # ENTRADA NOME ATLETA
    def entradAtleta(self):
        entrad = self.confirmaInput()
        if entrad != '001':
            proc = self.procAtleta(entrad, arquivos().getAtletasDict())
            return proc
        else:
            return entrad

    # PROCURA ATLETA NO DICIONARIO DE ATLETAS COM SALTOS
    def procAtleta(self, entrada, dicio):
        self.setNome(entrada)
        dicio_it = dicio.items()
        for k, v in dicio_it:
            if entrada == k:
                self.setNome(k)
                return True
            else:
                pass
        return False

    # VERIFICA A QUANTIDADE DE SALTOS
    def verficaSaltos(self, nome):
        qtds = len(arquivos().getAtletasDict()[nome])
        if qtds == 5:
            mensagens().getMsg3()
        elif qtds >= 0 and qtds <= 4:
            return qtds
        else:
            pass

    # ENTRADA COM VERIFICAÇÃO DE FLOAT
    def input_salto(self, stre):
        while True:
            try:
                print('Salto', stre)
                x = float(input('------: '))
                return round(x, 2)
            except:
                print("Valor incorreto. Ex: 0.0")

    # ADICIONA SALTOS A LISTA DENTRO DO DICINARIO DOS ATLETAS
    def addSaltos(self, dicio, nsaltos):
        try:
            dicio[self.getNome()].append(self.input_salto(nsaltos+1))
            nsaltos+=1
        except TypeError:
            pass

    # RELATORIO DE ATLETAS COM SALTOS
    def relatSaltos(self, dicio):
        for k, v in dicio.items():
            print(k+':')
            if len( v ) == 0:
                mensagens().getMsg5()
            else:
                print('-'*len(k)+': ',end='')
                for x in range(len(v)):
                    if x <= len(v)-2:
                        print(dicio[k][x], end=' ')
                    elif x <= len(v)-1:
                        print(dicio[k][x])
                    else:
                        print(dicio[k][x])

    # RELATORIA DAS MEDIAS DOS ATLETAS
    def relatMedias(self):
        for k, v in arquivos().getAtletasDict().items():
            print( k)
            if len(arquivos().getAtletasDict()[k]) < 5:
                print('Atleta com', len(arquivos().getAtletasDict()[k]), 'Saltos\n')
            else:
                aux = sorted(v)
                media = aux[1] + aux[2] + aux[3] / 3
                print('-'*len(k), '>', round(media / 3, 2 ))


# CLASSE PARA NOMES DE ATLETAS
class clube:
    def __init__(self):
        self.nome = self.setNome('nome')

    def addClube(self, dicio):
        dicio[self.getNome()] = []

    # RETORNA VALORES
    def getNome(self):
        return self.nome

    # ALTERA VALORES
    def setNome(self, nome):
        self.nome = nome

    # VERIFICAÇÃO PARA CANCELAMENTO DE FUNÇÃO
    def confirmaInput(self, msg):
        entrad = input(msg).capitalize()
        if entrad == '' or entrad == ' ' or entrad == '  ':
            mensagens().getMsg4()
            return '002'
        else:
            return entrad

    # ENTRADA NOME DO CLUBE
    def entradClube(self):
        entrad = self.confirmaInput(mensagens().getEntrada2())
        if entrad != '002':
            proc = self.procClube(entrad, arquivos().getClubesDict())
            return proc
        else:
            return entrad

    # PROCURA NOME DO CLUBE NOS DICIONARIOS
    def procClube(self, entrada, dicio):
        self.setNome(entrada)
        dicio_it = dicio.items()
        for k, v in dicio_it:
            if entrada == k:
                self.setNome(k)
                return True
            else:
                pass
        return False

    # LISTA COM NOMERAÇÃO DOS CLUBES OU ATLETAS PARA ADICIONAR
    def listaAtlClb(self, list):
        for x in range(len(list)):
            print(x+1, list[x])

    # VARREDURA E COMPARAÇÃO NAS LISTAS DE ATLETAS CADASTRADOS EM CLUBES E ATLETAS LIVRES
    def confirmaListasAtl(self):
        listAtlEmClb = []
        listaAtlDict = list(arquivos().getAtletasDict())
        for k, v in arquivos().getClubesDict().items():
            for x in range(len(arquivos().getClubesDict()[k])):
                    listAtlEmClb.append(arquivos().getClubesDict()[k][x])
        for z in range(len(listAtlEmClb)):
            if listAtlEmClb[z] in listaAtlDict:
                listaAtlDict.remove(listAtlEmClb[z])
            else:
                pass
        return listaAtlDict

    # ESCOLHER CLUBE COM NUMEROS DA LISTA
    def escolhaClube(self, msg, list):
        entrada = self.confirmaInput(msg)
        if entrada != '002':
            mensagens().getMsg15((list[int(entrada)-1]).upper())
            return list[int(entrada)-1]
        else:
            return entrada

    # ESCOLHER ATLETAS PARA CADASTRO COM NUMEROS NA LISTA
    def escolhaAtleta(self, msg, list):
        entrada = self.confirmaInput(msg)
        if entrada != '002':
            return int(entrada)-1
        else:
            return entrada

    # RELATORIO DE CLUBES COM ATLETAS CADASTRADOS
    def relatClubes(self, dicio):
        if len(list(dicio)) == 0:
            mensagens().getMsg6()
        else:
            for k, v in dicio.items():
                print( k + ':' )
                if len(v) == 0:
                    mensagens().getMsg7()
                else:
                    for x in range(len(v)):
                        print( '-' * len( k ) + ': ', end='' )
                        if x <= len(v) - 2:
                            print(dicio[k][x])
                        elif x <= len( v ) - 1:
                            print(dicio[k][x])
                        else:
                            print(dicio[k][x])