import csv
import time
import tkinter

from bibliotecas import *
from varGlobal import *

def funcionarios():
    nomeFuncionario = []
    idadeFuncionario = []
    enderecoFucionario = []
    salarioFuncionario = []
    funcaoFuncionario = []

    nome = input('informe o nome do funcionario')
    nomeFuncionario.append(nome)
    idade = int(input('qual a idade?'))
    idadeFuncionario.append(idade)
    endereco = input('infomer o endereço')
    enderecoFucionario.append(endereco)
    salario = float(input('qual o salario?'))
    salarioFuncionario.append(salario)
    funcao = input('infome a função')
    funcaoFuncionario.append(funcao)

    return nomeFuncionario, idadeFuncionario, enderecoFucionario, salarioFuncionario, funcaoFuncionario

def listaFuncionarios(dados):
    nomes, idades, enderecos, salasirios, funcoes = dados
    # eu quero que o sistema abra um arquivo para mim

    with open('dados_funcionarios.csv', 'a', newline='') as arquivo:
        popular = csv.writer(arquivo)
        popular.writerow(['nome, idade, endereço, salario', 'funcao'])
        for linha in range(len(nomes)):
            popular.writerow([nomes[linha],idades[linha],salasirios[linha],funcoes[linha]])



# função gera PIN
def gerarPin():
    #gerar um numero
    n1 = str(random.randint(0, 9))
    #escolher letras aleatórias
    l1 = random.choices(string.ascii_uppercase, k=4)
    n2 = str(random.randint(0, 9))
    l2 = random.choices(string.ascii_lowercase, k=2)

    # vou combinar as infomações
    return n1 + ''.join(l1) + n2 + ''.join(l2)
def salvarPin():
    pins = []
    dadosPin = gerarPin()
    pins.append(gerarPin())
    print(pins)

    cadaPin = dadosPin
    with open('pin.csv', 'a', newline='') as arquivo:
        popular = csv.writer(arquivo)
        for linha in range(len(pins)):
            popular.writerow([pins[linha]])

def janela():
    #gera uma tela incial
    root = tk.Tk()
    root.title('sistema lista de materias para construção')
    # o comando geometry
    root.geometry('400x200')
    # para gera um botão uso a instrução Button
    # na instrução Button devo falar onde ele vai aparecer
    # o que vai estar escrito nele
    # e a função a ser executada
    btn1 = tk.Button(root, text='cadastrar', command=janelaCadastro)
    btn1.pack(pady=10)
    btn2 = tk.Button(root, text='gerar pin', command=salvarPin)
    btn2.pack(pady=10)
    # para executar a janela, usar comando mainloop
    root.mainloop()

def janelaCadastro():
    rootCadastro = tk.Tk()
    rootCadastro.title('janela teste')
    rootCadastro.geometry('400x200')
    btnFuncionario = tk.Button(rootCadastro, text='cadastro de funcionario', command=gerarPin())
    btnFuncionario.pack(pady=10)
    btnFornecedor = tk.Button(rootCadastro, text='cadastro de fornecedor', command=gerarPin())
    btnFornecedor.pack(pady=10)
    btnProduto = tk.Button(rootCadastro, text='cadastro do produto', command=gerarPin())
    btnProduto.pack(pady=10)
    rootCadastro.mainloop()

def limparPins():
    time.sleep(10)
    with open('pin.csv','w', newline='') as arquivo:
        popular = csv.writer(arquivo)
        popular.writerow('')

def fornecedores():
    idFornecedor = []
    nomeFornecedor = []
    cnpjtFornecedor = []
    enderecoFornecedor = []
    tipoProdutoFornecedor = []
    contatoFornecedor = []
    emailFornecedor = []

    id= len(idFornecedor)
    idFornecedor.append(id)
    nome = input('informe o nome do fornecedor ')
    nomeFornecedor.append(nome)
    cnpj =  int(input('informe o cnpjt '))
    cnpjtFornecedor.append(cnpj)
    endereco = input('informe o endereço ')
    enderecoFornecedor.append(endereco)
    tipoProduto = input('informe o tipo do produto ')
    tipoProdutoFornecedor.append(tipoProduto)
    contato = input('informe o contato ')
    contatoFornecedor.append(contato)
    email = input('informe o email@ ')
    emailFornecedor.append(email)

    return (idFornecedor, nomeFornecedor,cnpjtFornecedor, enderecoFornecedor,
            tipoProdutoFornecedor, contatoFornecedor, emailFornecedor)

def listaFornecedores(dadosFornecedores):
    id, nome, cnpj, endereco, tipo, contato, email = dadosFornecedores

    with open('dados_funcionarios.csv', 'a', newline='') as arquivo:
        popular = csv.writerow(arquivo)
        for linha in range(len(id)):
            popular.writerow([id[linha],nome[linha], cnpj[linha], endereco[linha],
                              tipo[linha], contato[linha], email[linha]])


def produtos():
    idProduto = []
    nomeProduto = []
    valorProduto = []
    fabricanteProduto = []
    quantidadeProduto = []

    id = len(idProduto) + 1
    idProduto.append(id)
    nome = input('informe o nome do produto')
    nomeProduto.append(nome)
    valor = float(input('informe o valor do produto'))
    valorProduto.append(valor)
    fabricante = input('infome o fabricante')
    fabricanteProduto.append(fabricante)
    quantidade = float(input('informe a quantidade'))
    quantidadeProduto.append(quantidade)

    return idProduto, nomeProduto, valorProduto, fabricanteProduto, quantidadeProduto

def listaProdutos(dadoProdutos):
    id, nome, valor, fabricante, quantidade = dadoProdutos

    with open('dados_funcionarios.csv', 'a', newline='') as arquivo:
        popular = csv.writerow(arquivo)
        for linha in range(len(id)):
            popular.writerow([id[linha], nome[linha], valor[linha], fabricante[linha], quantidade[linha]])
