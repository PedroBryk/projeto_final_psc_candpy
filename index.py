import os
import random
import string

class Cadastro:
    def __init__(self, nome, cpf, email, senha):  
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
    
    def sobre(self):
        print(f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Senha: {self.senha}")

    def to_string(self):
        return f"{self.nome},{self.cpf},{self.email},{self.senha}"


class CadastroFuncionario(Cadastro):
    def __init__(self, nome, cpf, email, senha, cargo):
        super().__init__(nome, cpf, email, senha)  
        self.cargo = cargo
    
    def sobre(self):
        print(f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Senha: {self.senha}, Cargo: {self.cargo}")

    def to_string(self):
        return f"{self.nome},{self.cpf},{self.email},{self.senha},{self.cargo}"


class Produto:
    def __init__(self, nome, descricao, valor, cod):  
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.cod = cod
    
    def sobre(self):
        print(f"Nome: {self.nome}, Descrição: {self.descricao}, Valor R$: {self.valor}, Código Produto: {self.cod}")

    def to_string(self):
        return f"{self.nome},{self.descricao},{self.valor},{self.cod}"

class metodo_cartao:
    def __init__(self, numero, validade, cvv, titular):
        self.numero = numero
        self.validade = validade
        self.cvv = cvv
        self.titular = titular
    
    def sobre(self):
        print(f"Numero: {self.numero}, Validade: {self.validade}, Cvv: {self.cvv}, Titular: {self.titular}")

class endereco:
    def __init__(self, cidade, bairro, rua, complemento):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.complemento = complemento
    
    def sobre(self):
        print(f"Cidade: {self.cidade}, Bairro: {self.bairro}, Numero: {self.rua}, Complemento: {self.complemento}")

CLIENTE_FILE = 'clientes.txt'
PRODUTO_FILE = 'produtos.txt'
VENDEDOR_FILE = 'vendedores.txt'

produtos_cadastrados = []
clientes_cadastrados = []
vendedores_cadastrados = []

def carregar_clientes():
    if os.path.exists(CLIENTE_FILE):
        with open(CLIENTE_FILE, 'r') as f:
            for linha in f.readlines():
                dados = linha.strip().split(',')
                cliente = Cadastro(dados[0], dados[1], dados[2], dados[3])
                clientes_cadastrados.append(cliente)

def carregar_produtos():
    if os.path.exists(PRODUTO_FILE):
        with open(PRODUTO_FILE, 'r') as f:
            for linha in f.readlines():
                dados = linha.strip().split(',')
                produto = Produto(dados[0], dados[1], dados[2], dados[3])
                produtos_cadastrados.append(produto)

def carregar_vendedores():
    if os.path.exists(VENDEDOR_FILE):
        with open(VENDEDOR_FILE, 'r') as f:
            for linha in f.readlines():
                dados = linha.strip().split(',')
                vendedor = CadastroFuncionario(dados[0], dados[1], dados[2], dados[3], dados[4])
                vendedores_cadastrados.append(vendedor)


def salvar_cliente(cliente):
    with open(CLIENTE_FILE, 'a') as f:
        f.write(cliente.to_string() + '\n')


def salvar_produto(produto):
    with open(PRODUTO_FILE, 'a') as f:
        f.write(produto.to_string() + '\n')


def salvar_vendedor(vendedor):
    with open(VENDEDOR_FILE, 'a') as f:
        f.write(vendedor.to_string() + '\n')

def limpar_dados():

    with open("clientes.txt", "w") as arquivo_clientes:
        arquivo_clientes.write("")  
    
    with open("vendedores.txt", "w") as arquivo_vendedores:
        arquivo_vendedores.write("")  
    
    with open("produtos.txt", "w") as arquivo_produtos:
        arquivo_produtos.write("")  

    print("Todos os dados de clientes, vendedores e produtos foram limpos.")


# Função para cadastrar um vendedor antes de cadastrar produtos
def cadastro_obrigatorio_vendedor():
    print("Vamos realizar o cadastro do vendedor.")
    nome = input("Digite o nome do vendedor: ")
    cpf = input("Digite o CPF do vendedor: ")
    email = input("Digite o email do vendedor: ")
    senha = input("Digite a senha do vendedor: ")
    cargo = "Vendedor"
    
    vendedor = CadastroFuncionario(nome, cpf, email, senha, cargo)
    vendedores_cadastrados.append(vendedor)
    salvar_vendedor(vendedor)

    print("\nCadastro de vendedor realizado com sucesso!")
    vendedor.sobre()


def cadastra_produto():
    print("\nVamos realizar o cadastro de um produto: ")
    nome_produto = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    valor = input("Digite o valor do produto: ")
    cod = input("Digite o código do produto: ")

    produto = Produto(nome_produto, descricao, valor, cod)
    produtos_cadastrados.append(produto)
    salvar_produto(produto)

    print("\nProduto cadastrado com sucesso!")
    produto.sobre()


def mostrar_produtos():
    print("\n---------- Produtos Disponíveis ----------")
    if produtos_cadastrados:
        for produto in produtos_cadastrados:
            produto.sobre()
    else:
        print("Nenhum produto cadastrado ainda.")


# Função para cadastrar um cliente
def cadastra_cliente():
    print("Vamos realizar seu cadastro: ")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cliente = Cadastro(nome, cpf, email, senha)
    clientes_cadastrados.append(cliente)
    salvar_cliente(cliente)

    print("\nCadastro realizado com sucesso!")
    cliente.sobre()


# Função para verificar login do cliente
def login_cliente():
    print("\n------------- CandPy -------------")
    email = input("Insira seu email: ")
    senha = input("Insira sua senha: ")

    for cliente in clientes_cadastrados:
        if cliente.email == email and cliente.senha == senha:
            print("Login de cliente realizado com sucesso!")
            return True

    print("Email ou senha incorretos. Iniciando o cadastro.")
    cadastra_cliente()
    return login_cliente()


# Função para verificar login do vendedor
def login_vendedor():
    print("\n------------- CandPy -------------")
    email = input("Insira seu email: ")
    senha = input("Insira sua senha: ")

    for vendedor in vendedores_cadastrados:
        if vendedor.email == email and vendedor.senha == senha:
            print("Login de vendedor realizado com sucesso!")
            return True

    print("Email ou senha incorretos.")
    return login_vendedor()


# Função para o cliente
def codigo_cliente():
    print("Olá cliente, que bom tê-lo conosco! ")
    condicao1 = input("Você possui cadastro em nossa loja? S/N: ").upper()

    if condicao1 == "S":
        if login_cliente():
            mostrar_produtos()
            compra_produto()
    elif condicao1 == "N":
        cadastra_cliente()
        if login_cliente():
            mostrar_produtos()
            compra_produto()
    else:
        print("Opção inválida!")


# Função para o vendedor
def codigo_funcionario():
    print("Olá vendedor!")
    if login_vendedor():
        print("Você pode cadastrar produtos.")
        while True:
            cadastra_produto()
            continuar = input("Deseja cadastrar outro produto? (S/N): ").upper()
            if continuar == 'N':
                break
def codigo_admin():
    print("Ola administrador do sistema! ")
    limpadados = input("Gostaria de limpar os dados armazenados no sistema? S/N").upper()

    if limpadados == 'S':
        limpar_dados()
        print("Dados limpos!")
    else:
        return None
    
def gerar_codigo_pix():
    caracteres = string.ascii_letters + string.digits  
    codigo_pix = ''.join(random.choice(caracteres) for _ in range(32))
    
    print("\n Nome do recebedor: CandPy \n Cidade: Guarapuava-PR")
    print("\nCódigo PIX gerado:", codigo_pix)
    return codigo_pix

def compra_produto():
    comprar = input("Gostaria de comprar algum produto? S/N: ").upper()

    if comprar == 'S':
        mostrar_produtos()
        escolha_produto = input("Digite o código do produto que você deseja: ")

        for produto in produtos_cadastrados:
            if produto.cod == escolha_produto:
                print(f"comprar: {produto.nome}")

                print("Preencha seu endereco para entrega: ")

                cidade = input("Qual a cidade? ")
                bairro = input("Qual o bairro? ")
                rua = input("Qual a rua? ")
                complemento = input("Qual o complemento? ")

                endereco_entrega = endereco(cidade, bairro, rua, complemento)

                endereco_entrega.sobre()

                pagamento = input("Qual sera a forma de pagamento, pix ou cartao? ").lower()

                if pagamento == 'pix':
                    gerar_codigo_pix()

                    print("Aguardando pagamento, apos a aprovacao voce recebera um email")
                elif pagamento == 'cartao':
                    print("Vamos realizar o cadastro do cartao: ")
                    numero = input("Digite o numero do cartao: ")
                    validade = input("Digite a data de validade: ")
                    cvv = input("Digite o cvv: ")
                    titular = input("Digite o titular do cartao: ")

                    pagamento_carto = metodo_cartao(numero, validade, cvv, titular)

                    pagamento_carto.sobre()

                    print("Aguardando pagamento, apos a aprovacao voce recebera um email")
                
                else:
                    print("Metodo invalido")
                    mostrar_produtos()

                return
        print("Produto não encontrado.")
    else:
        print("Compra cancelada.")



carregar_clientes()
carregar_produtos()
carregar_vendedores()


if not vendedores_cadastrados:
    
    print("Nenhum vendedor cadastrado. Vamos cadastrar um vendedor antes de iniciar.")
    cadastro_obrigatorio_vendedor()
else:
    
    print("Vendedores encontrados no sistema.")


print("\nAgora que o vendedor e os produtos estão cadastrados, escolha uma opção:")
entrada = input("Você é cliente ou vendedor? ").lower()

opcoes = {
    "cliente": codigo_cliente,
    "vendedor": codigo_funcionario,
    "admin": codigo_admin
}

opcoes.get(entrada, lambda: print("Opção inválida!"))()