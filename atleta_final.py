# Trabalho Final - Avaliação Atleta
# Versão Final - 08/07/2019 Noite
# Leonardo Soares Duarte
# ARQUIVO DE CORPO DO CÓDIGO

from atleta_final_msgs import mensagens
from atleta_final_class import atleta, clube
from atleta_final_arqvs import arquivos

atl = atleta()
clb = clube()
arq = arquivos()

# CADASTRO DO ATLETA
def cadastrar_atleta():
    mensagens().getOpt1()
    mensagens().getAviso1()
    while True:
        ent = atl.entradAtleta()
        if ent == '001':
            return
        elif ent == False:
            atl.addAtleta(arq.getAtletasDict())
        else:
            mensagens().getMsg1()

# CADASTRA OS SALTOS MANUAIS OU AUTOMATICOS / MENU DE OPÇÕES
def cadastrar_saltos():
    mensagens().getOpt2()
    ent = atl.entradAtleta()
    if ent == '001':
        pass
    elif not ent:
        return mensagens().getMsg2()
    else:
        nsalt = atl.verficaSaltos(atl.getNome())
        atl.addSaltos( arq.getAtletasDict(), nsalt )
        return

# CADASTRA O SALTO DE TODOS ATLETAS AUTOMATICAMENTE
# PARA QUE SEJA MAIS FACIL AVALIADO.
def cadastrar_saltos_automaticos():
    aux = arq.getAtletasDict()
    for k, v in aux.items():
        aux2 = 5-len(aux[k])
        for x in range(aux2):
            aux[k].append(atl.saltoGen())
            arq.w_atl_clu()
    return

# RELATORIO DE SALTOS DOS ATLETAS
def relat_atletas_saltos():
    if not arquivos().getAtletasDict().items():
        mensagens().getMsg8()
    else:
        mensagens().getOpt3()
        atl.relatSaltos(arq.getAtletasDict())

# CADASTRA NOME DO CLUBE
def cadasrar_clubes():
    mensagens().getOpt4()
    mensagens().getAviso1()
    while True:
        ent = clb.entradClube()
        if ent == '002':
            return
        elif ent == False:
            clb.addClube(arq.getClubesDict())
        else:
            mensagens().getMsg11()

# ADICIONA ATLETAS A UM CLUBE
def add_atleta_clube():
    while True:
        mensagens().getOpt5()
        aux = [list(arquivos().getClubesDict()), clb.confirmaListasAtl()]
        if not aux[1]:
            mensagens().getMsg12()
            return
        else:
            try:
                mensagens().getOpt51()
                clb.listaAtlClb(aux[0])
                selectClb = clb.escolhaClube('\nNº Clube: ', aux[0])
                if selectClb == '002':
                    return
                else:
                    mensagens().getOpt52()
                    clb.listaAtlClb(aux[1])
                    selectAtl = clb.escolhaAtleta('\nNº Atleta: ', aux[1])
                    if selectAtl == '002':
                        return
                    else:
                        arq.getClubesDict()[selectClb].append(aux[1][selectAtl])
                        arq.w_atl_clu()
            except IndexError:
                mensagens().getMsg14()

# RELATORIO COM TODOS CLUBES E ATLETAS CADASTRADOS
def relat_atletas_em_clubes():
    mensagens().getOpt6()
    clb.relatClubes(arq.getClubesDict())

# RELATORIA DAS MEDIAS DOS ATLETAS
def relat_media_atletas():
    if not list(arq.getAtletasDict()):
        mensagens().getMsg8()
        return
    else:
        mensagens().getOpt7()
        atl.relatMedias()

def clear():
    if not list(arq.getAtletasDict()):
        mensagens().getMsg8()
        return
    elif not list(arq.getClubesDict()):
        mensagens().getMsg6()
        return
    else:
        mensagens().getOpt8()
        mensagens().getAviso1()
        mensagens().getAviso2()
        if input('------: ').upper() == 'LIMPAR':
            arq.clear_atl_clu()
            mensagens().getMsg13()
        else:
            mensagens().getMsg4()
            return

def menu_opt():
    while True:
        arq.r_atl_clu()
        arq.w_atl_clu()
        mensagens().getMenu0()
        opt = input( str( "OPÇÃO DESEJADA: " ) )
        if opt == "0": # FINALIZAR PROGRAMA
            arq.w_atl_clu()
            break
        elif opt == "1": # CADASTRAR ATLETA
            cadastrar_atleta()
        elif opt == "2": # CADASTRAR SALTOS DO ATLETA
            cadastrar_saltos()
        elif opt == "3": # RELATÓRIO DO ATLETA
            relat_atletas_saltos()
        elif opt == "4": # CADASTRA CLUBE
            cadasrar_clubes()
        elif opt == "5": # ADICIONA ATLETA NO CLUBE
            add_atleta_clube()
        elif opt == "6": # RELATÓRIO CLUBE ATLETAS
            relat_atletas_em_clubes()
        elif opt == "7": # RELATÓRIO MEDIA ATLETAS
            relat_media_atletas()
        elif opt == '8': # PRINTAR E LIMPAR DICIONARIOS
            clear()
        elif opt == '9':  # LIMPAR DICIONARIOS
            cadastrar_saltos_automaticos()
        elif opt == '10':  # LIMPAR DICIONARIOS
            print(arq.getAtletasDict())
            print(arq.getClubesDict())
        else:
            mensagens().getMsg10()

mensagens().getAviso3()
if input('----: ').upper() == 'SIM' and 'S':
    arquivos().notepad(r'atleta_final.py')
    arquivos().notepad(r'atleta_final_class.py')
    arquivos().notepad(r'atleta_final_arqvs.py')
    arquivos().notepad(r'atleta_final_msgs.py')
    arquivos().notepad(r'arquivos/obs/LSD.txt')
else:
    pass
menu_opt()

