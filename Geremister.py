### criar plataforma de controle de clientes para empresa TELECOM
### plataforma utilizando flask
### paginas de verificação como informadas no trello
### Estilização com Bootstrap
from flask import Flask, render_template, request, redirect, session, flash, url_for
## Importando as bibliotecas


class  Cliente:
    def __init__(self, nome, cpf, endereco, plano):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.plano = plano
        self.faturas = None

        if self.plano == 'BASIC':
            self.faturas = 'R$ 89,90'
        else:
            self.faturas = 'R$ 120,00'

clienteslista = [
    Cliente("Gabriel Castanho", "123.456.789-09","Casa 123, Rua das Flores, Cidade Alegre", "BASIC"),
    Cliente("Jose da silva", "987.654.321-98","Casa 456, Avenida Principal, Cidade do Sol",  "PREMIUM"),
    Cliente("Vagner oliveira", "456.789.123-45","Casa 789, Rua da Esperança, Cidade Feliz",  "BASIC"),
    Cliente("Maria Santos", "876.543.210-87","Casa 321, Rua da Amizade, Cidade Tranquila", "PREMIUM"),
    Cliente("Pedro Oliveira", "321.654.987-32","Casa 654, Avenida da Paz, Cidade Serena", "BASIC"),
    Cliente("Ana Rodrigues", "654.987.321-65","Casa 987, Rua da Harmonia, Cidade Harmoniosa", "PREMIUM"),
    Cliente("Sofia Costa", "234.567.890-23","Casa 234, Avenida da Alegria, Cidade Encantada", "BASIC")
]





### rotas do site
app = Flask(__name__)

app.secret_key = 'gabriel'

@app.route('/login')
def login():
    # Implemente a lógica para a página de login aqui
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Implemente a lógica para a página de dashboard aqui
    return render_template('dashboard.html', titulo="GEREMISTER")


@app.route('/clientes')
def clientes():
    # Implemente a lógica para a página de dashboard aqui
    return render_template('clientes.html', clientes=clienteslista)

@app.route('/planos')
def planos():
    # Implemente a lógica para a página de dashboard aqui
    return render_template('planos.html')


@app.route('/atualizar')
def atualizar():

    return render_template('atualizar.html')



@app.route('/atualiza', methods=['POST'])
def atualiza():
    cpf = request.form['CPF']  # Obtém a senha do pedido do formulário
    novo_plano = request.form['PLANO']

    for cliente in clienteslista:
        if cliente.cpf == cpf:
            cliente.plano = novo_plano
            flash('PLANO DO CLIENTE ALTERADO', 'sucess')
            flash('FATURA DO CLIENTE ALTERADO', 'sucess')

            return render_template('clientes.html', clientes=clienteslista)

        else:
            flash('CLIENTE NAO ENCONTRADO VERIFIQUE O CPF INFORMADO')
            return render_template('atualizar.html')
    return render_template('atualizar.html')

@app.route('/faturas')
def faturas3():
    # Implemente a lógica para a página de dashboard aqui
    return render_template('atualizarfaturas.html')


@app.route('/fatura', methods=['POST'])
def verificarfatura():
    cpf = request.form['CPF']
    cliente_encontrado = None

    for cliente in clienteslista:
        if cpf == cliente.cpf:
            cliente_encontrado = cliente
            break  # O cliente foi encontrado, podemos sair do loop

    if cliente_encontrado:
        return render_template('valorfatura.html', clientes=cliente_encontrado)
    else:
        flash('CLIENTE NAO ENCONTRADO VERIFIQUE O CPF INFORMADO')
        return render_template('atualizarfaturas.html')





if __name__ == "__main__":
    app.run(debug=True)
