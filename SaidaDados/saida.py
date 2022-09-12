def salvaResultado(resultado):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + ' '
    arquivo = open('C:/Users/thais/PycharmProjects/pythonProject/Lista1/SaidaDados/resultado.txt', 'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()