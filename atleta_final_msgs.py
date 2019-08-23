# Trabalho Final - Avaliação Atleta
# Versão Final - 08/07/2019 Noite
# Leonardo Soares Duarte
# ARQUIVO DE CLASSES DE MENSAGENS

# CLASSE PARA TRABLHAR COM AS MENSAGENS E MENUS
class mensagens:
    def __init__(self):
        self.menu0 = '''
////////////////////////////////////
//     MENU DE OPÇÕES             //
////////////////////////////////////
// 1 - CADASTRAR ATLETA           //
// 2 - CADASTRAR SALTOS DO ATLETA //
// 3 - RELATÓRIO DOS ATLETAS      //
// 4 - CADASTRA CLUBE             //
// 5 - ADICIONA ATLETA NO CLUBE   //
// 6 - RELATÓRIO CLUBE ATLETAS    //
// 7 - RELATÓRIO MEDIA ATLETAS    //
// 8 - LIMPAR CLUBES E ATLETAS    //
// 9 - CADASTRA TODOS SALTOS AUTO //
// 0 - FINALIZAR PROGRAMA         //
////////////////////////////////////'''

        self.menu1 = '''
////////////////////////////////////
// 1 - CADASTRAR TODOS SALTOS     //
// 2 - CADASTRAR SALTO POR SALTO  //
// 3 - NÃO CADASTRAR              //
////////////////////////////////////'''
        self.opt1 = '''
////////////////////////////////////
//       CADASTRAR ATLETA         //
////////////////////////////////////'''

        self.opt2 = '''
////////////////////////////////////
//   CADASTRAR SALTOS DO ATLETA   //
////////////////////////////////////'''

        self.opt3 = '''
////////////////////////////////////
//     ENTER RETORNA AO MENU      //
//                                //
//     RELATORIO DOS ATLETAS      //
//     Atleta:                    //
//     ------: Saltos             //
////////////////////////////////////'''

        self.opt4 = '''
////////////////////////////////////
//       CADASTRAR CLUBES         //
////////////////////////////////////'''

        self.opt5 = '''
////////////////////////////////////
//    ADICIONAR ATLETAS A CLUBES  //
////////////////////////////////////'''

        self.opt51 = '''
SELECIONE O CLUBE:'''
        self.opt52 = '''
SELECIONE O ATLETA:'''

        self.opt6 = '''
////////////////////////////////////
//       RELATORIO DE CLUBES      //
////////////////////////////////////
'''

        self.opt7 = '''
////////////////////////////////////
//      RELATORIO DE MEDIAS       //
////////////////////////////////////
'''
        self.opt8 = '''
////////////////////////////////////
//     LIMPAR ATLETAS E CLUBES    //
////////////////////////////////////'''

        self.opt9 = ''

        self.msg1 = '''            
       ATLETA JÁ CADASTRADO!
       '''

        self.msg2 = '''               
       ATLETA NÃO CADASTRADO!
       '''

        self.msg3 = '''
     TODOS SALTOS CADASTRADOS!
     '''

        self.msg4 = '''               
  OPERAÇÃO CANCELADA PELO USUARIO!
  '''

        self.msg5 = 'Atleta não saltou!'

        self.msg6 = '''
        NEM UM CLUBE CADASTRADO!'''

        self.msg7 = 'Nem um atleta cadastrado!'

        self.msg8 = '''
    NENHUM ATLETA CADASTRADO!'''

        self.msg10 = '''
        OPÇÃO INCORRETA!'''

        self.msg11 = '''
    CLUBE JÁ CADASTRADO!
    '''
        self.msg12 = '''
  TODOS ATLETAS ASSOCIADOS OU
  NEM UM ATLETA CADASTRADO OU
    NEM UM CLUBE CADASTRADO.'''

        self.msg13 = '''
    LIMPEZA CONCLUIDA COM SUCESSO!'''

        self.msg14 = '''
  NUMERO DE LISTA INCORRETO! 
      TENTE NOVAMENTE.'''

        self.msg15 = '''
        CLUBE SELECIONADO
        ------>'''

        self.msg16 = '''
 ATLECA COM 5 SALTOS CONCLUIDOS!
    '''

        self.entrada1 = 'Nome do Atleta: '

        self.entrada2 = 'Nome do Clube: '

        self.aviso1 = '''//     ENTER RETORNA AO MENU      //
////////////////////////////////////'''

        self.aviso2 = '''//     PARA CONFIRMAR LIMPEZA     //
//     DIGITE  "LIMPAR"           //
//     PARA CANCELAR LIMPEZA      //
//     TECLE   "ENTER"            //
////////////////////////////////////
'''
        self.aviso3 = '''
////////////////////////////////////////////////////////////
///////  ABRIR ARQUIVOS DE CONFIGURAÇÃO NO NOTEPAD?  ///////
///////  atleta_final.py                             ///////
///////  atleta_final_class.py                       ///////
///////  atleta_final_arqvs.py                       ///////
///////  atleta_final_msgs.py                        ///////
////////////////////////////////////////////////////////////
///////                                              ///////
///////  DIGITE SIM/S ou PRESSIONE QUALQUER TECLA!   ///////
////////////////////////////////////////////////////////////'''

    def getMenu0(self):
        return print(self.menu0)

    def getMenu1(self):
        return print(self.menu1)

    def getOpt1(self):
        return print(self.opt1)

    def getOpt2(self):
        return print(self.opt3)

    def getOpt3(self):
        return print(self.opt3)

    def getOpt4(self):
        return print(self.opt4)

    def getOpt5(self):
        return print(self.opt5)

    def getOpt51(self):
        return print(self.opt51)

    def getOpt52(self):
        return print(self.opt52)

    def getOpt6(self):
        return print(self.opt6)

    def getOpt7(self):
        return print(self.opt7)

    def getOpt8(self):
        return print(self.opt8)

    def getMsg1(self):
        return print(self.msg1)

    def getMsg2(self):
        return print(self.msg2)

    def getMsg3(self):
        return print(self.msg3)

    def getMsg4(self):
        return print(self.msg4)

    def getMsg5(self):
        return print(self.msg5)

    def getMsg6(self):
        return print(self.msg6)

    def getMsg7(self):
        return print(self.msg7)

    def getMsg8(self):
        return print(self.msg8)

    def getMsg10(self):
        return print(self.msg10)

    def getMsg11(self):
        return print(self.msg11)

    def getMsg12(self):
        return print(self.msg12)

    def getMsg13(self):
        return print(self.msg13)

    def getMsg14(self):
        return print(self.msg14)

    def getMsg15(self, clbindex):
        return print(self.msg15, clbindex)

    def getMsg16(self):
        return print(self.msg16)

    def getEntrada1(self):
        return self.entrada1

    def getEntrada2(self):
        return self.entrada2

    def getAviso1(self):
        return print(self.aviso1)

    def getAviso2(self):
        return print(self.aviso2)

    def getAviso3(self):
        return print(self.aviso3)
