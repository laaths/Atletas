# Trabalho Final - Avaliação Atleta
# Versão Final - 08/07/2019 Noite
# Leonardo Soares Duarte
# ARQUIVO DE CLASSES DE ARQUIVOS

import pickle
import subprocess

# CLASSE PARA TRABALHAR COM ARQUIVOS
class arquivos:
    def __init__(self):
        self.atletas = self.r_atletas()
        self.clubes = self.r_clubes()
    # FAZ A LEITURA DOS ARQUIVOS atletas.txt E clubes.txt
    def r_atl_clu(self):
        self.r_atletas()
        self.r_clubes()

    # FAZ A LEITURA DO ARQUIVO atletas.txt
    def r_atletas(self):
        try:
            arq = open( 'arquivos/atletas.txt', 'rb' )
            dict_ = pickle.load( arq )
            arq.close()
            return dict_
        except IOError:
            self.atletas = {}
            self.w_atletas()
            return self.atletas

    # FAZ A LEITURA DO ARQUIVO clubes.txt
    def r_clubes(self):
        try:
            arq = open( 'arquivos/clubes.txt', 'rb' )
            dict_ = pickle.load( arq )
            arq.close()
            return dict_
        except IOError:
            self.clubes = {}
            self.w_clubes()
            return self.clubes

    # FAZ A GRAVAÇÃO DOS ARQUIVOS atletas.txt E clubes.txt
    def w_atl_clu(self):
        self.w_atletas()
        self.w_clubes()

    # FAZ A GRAVAÇÃO DO ARQUIVO atletas.txt
    def w_atletas(self):
        arq = open( 'arquivos/atletas.txt', 'wb' )
        pickle.dump( self.atletas, arq )
        arq.close()

    # FAZ A GRAVAÇÃO DO ARQUIVO clubes.txt
    def w_clubes(self):
        arq = open( 'arquivos/clubes.txt', 'wb' )
        pickle.dump( self.clubes, arq )
        arq.close()

    # LIMPAR DICIONARIO ATLETAS E CLUBES
    def clear_atl_clu(self):
        self.clear_atletas()
        self.clear_clubes()

    # LIMPA DICIONARIO DE ATLETAS
    def clear_atletas(self):
        self.atletas = {}
        self.w_atletas()
        return self.atletas

    # LIMPA DICIONARIO DE CLUBES
    def clear_clubes(self):
        self.clubes = {}
        self.w_clubes()
        return self.clubes

    # ABRE NOTEPAD COM A NOTA NO PATCH
    def notepad(self, path):
        #path = r'teste.txt'
        subprocess.Popen(['notepad.exe', path])

    # RETORNA DICIONARIO PARA TESTE
    def getAtletasDict(self):
        return self.atletas

    # RETORNA DICIONARIO PARA TESTE
    def getClubesDict(self):
        return self.clubes

