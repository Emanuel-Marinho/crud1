import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'conexao'
)

cursor = conexao.cursor()

comando = '''
create table pessoa_fisica(
id int not null auto_increment primary key,
nome varchar(50) not null,
endereco varchar(100) not null,
horas_trabalho varchar(3) not null,
idade varchar(2) not null,
cpf varchar(50) not null);
'''
cursor.execute(comando)
conexao.commit()

comando1 = '''
create table pessoa_juridica(
id int not null auto_increment primary key,
nome varchar(50) not null,
endereco varchar(100) not null,
horas_trabalho varchar(3) not null,
quant_pessoas varchar(4) not null,
cnpj varchar(50) not null);
'''
cursor.execute(comando1)
conexao.commit()

class Funcionario:
    def __init__(self,nome,endereco,horas_trabalho):
        self.nome = nome
        self.endereco = endereco
        self.horas_trabalho = horas_trabalho


class PessoaFisica(Funcionario):
    def __init__(self, nome, endereco, horas_trabalho, idade,cpf):
        super().__init__(nome, endereco, horas_trabalho)
        self.idade = idade
        self.cpf = cpf

    def cadastroFisico(self):
        dados.append(self.nome)
        dados.append(self.endereco)
        dados.append(self.horas_trabalho)
        dados.append(self.idade)
        pf[self.cpf] = dados.copy()
        dados.clear()
        return f'\033[30;42mCadastro do {self.nome}, cujo cpf é {self.cpf} feito com sucesso!\033[m'

class PessoaJuridica(Funcionario):
    def __init__(self,nome,endereco,horas_trabalho,quant_pessoas,cnpj):
        super().__init__(nome, endereco, horas_trabalho)
        self.quant_pessoas = quant_pessoas
        self.cnpj = cnpj

    def cadastroJuridico(self):
        dados.append(self.nome)
        dados.append(self.endereco)
        dados.append(self.horas_trabalho)
        dados.append(self.quant_pessoas)
        pj[self.cnpj] = dados.copy()
        dados.clear()
        return f'\033[30;42mCadastro da {self.nome}, cujo cnpj é {self.cnpj} feito com sucesso!\033[m'

def atualizar():
    opcao = int(input('Digite 1 para visualizar os cadastros das Pessoas Físicas \nDigite 2 para visualizar os cadastros das Pessoas Jurídicas '
                      '\nQual sua opção? '))
    if opcao == 1:
        for cpf, dados in pf.items():
            print(f'\033[7;30mCPF: {cpf} \nNome: {dados[0]} \nEndereço: {dados[1]} \nHoras de Trabalho: {dados[2]} \nIdade: {dados[3]}\033[m')

    elif opcao == 2:
        for cnpj, dados in pj.items():
            print(f'\033[7;30mCnpj: {cnpj} \nEmpresa: {dados[0]} \nEndereço: {dados[1]} \nHoras de Trabalho: {dados[2]} \nQuantidade de Pessoas: {dados[3]}\033[m')

def apagar():
    opcao = int(input('Digite 1 para apagar algum cadastro nas Pessoas Físicas \nDigite 2 para apagar algum cadastro nas Pessoas Jurídicas'
                      '\nQual sua opção? '))
    if opcao == 1:
        for cpf, dados in pf.items():
            print(f'\033[1;35;43mCPF: {cpf}\033[m e Nome: {dados[0]}')
        apagarpf = input('Digite o cpf que deseja apagar: ')
        comandoA = f'''
        delete from pessoa_fisica
        where CPF = {apagarpf}
        '''
        cursor.execute(comandoA)
        conexao.commit()
        pf.pop(apagarpf)
        return f'\033[0;30;41mCpf {apagarpf} apagado com sucesso!\033[m'


    elif opcao == 2:
        for cnpj, dados in pj.items():
            print(f'\033[1;35;43mCNPJ: {cnpj}\033[m e Empresa: {dados[0]}')
        apagarpj = input('Digite o cnpj que deseja apagar: ')
        comandoA = f'''
        delete from pessoa_juridica
        where CNPJ = {apagarpj}
        '''
        cursor.execute(comandoA)
        conexao.commit()
        pj.pop(apagarpj)
        return f'\033[0;30;41mCnpj {apagarpj} apagado com sucesso!\033[m'


pf = dict()
pj = dict()
dados = list()


print('-=' *20)
print('SISTEMA DE CADASTRO'.center(40))
print('-=' *20)
while True:
    tipo = int(input('Digite 1 para cadastrar Pessoa Física \nDigite 2 para cadastrar Pessoa Jurídica '
                     '\nDigite 3 para ver todos os funcionários cadastrados \nDigite 4 para apagar algum funcionário '
                     '\nDigite 0 para sair do sistema \nQual sua opção? '))
    if tipo == 1:
        nome = input('Digite o nome do funcionário: ')
        endereco = input('Digite o seu endereço: ')
        horas_trabalho = int(input('Digite a carga horária do funcionário: '))
        idade = int(input('Qual a sua idade? '))
        cpf = input('Digite o seu cpf: ')
        funcionario = PessoaFisica(nome,endereco,horas_trabalho,idade,cpf)
        print(funcionario.cadastroFisico())
        comando = f'''
        insert into pessoa_fisica(nome, endereco, horas_trabalho, idade, cpf)
        values('{nome}','{endereco}','{horas_trabalho}','{idade}','{cpf}')
        '''
        cursor.execute(comando)
        conexao.commit()

    elif tipo == 2:
        nome = input('Digite o nome da empresa: ')
        endereco = input('Digite o endereço: ')
        horas_trabalho = int(input('Carga horária: '))
        quant_pessoas = int(input('Digite a quantidade de pessoas nessa empresa: '))
        cnpj = input('Digite o cnpj: ')
        empresa = PessoaJuridica(nome,endereco,horas_trabalho,quant_pessoas,cnpj)
        print(empresa.cadastroJuridico())
        comando = f'''
        insert into pessoa_juridica(nome,endereco,horas_trabalho,quant_pessoas,cnpj)
        values('{nome}','{endereco}','{horas_trabalho}','{quant_pessoas}','{cnpj}')
        '''
        cursor.execute(comando)
        conexao.commit()

    elif tipo == 3:
        atualizar()

    elif tipo == 4:
        print(apagar())

    elif tipo == 0:
        print('Até Mais!')
        comando = '''
        drop table pessoa_fisica;
        '''
        cursor.execute(comando)
        conexao.commit()
        comando1 = '''
        drop table pessoa_juridica;
        '''
        cursor.execute(comando1)
        conexao.commit()
        break

    else:
        print('Opção Inválida! Tente Novamente')

cursor.close()
conexao.close()