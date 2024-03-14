from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ Listar os clientes """
    return render_template('lista_clientes.html', clientes = CLIENTES)

@cliente_route.route('/', methods = ['POST'])
def inserir_clientes():
    """ Inserir os dados do cliente """
    
    data=request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    } 

    CLIENTES.append(novo_usuario)

    return render_template('item_clientes.html', cliente=novo_usuario  )


@cliente_route.route('/new')
def form_clientes():
    """ Formulario para cadastrar um cliente"""
    return render_template('form_clientes.html')

@cliente_route.route('/<int>:cliente_id>')
def detalhe_clientes(cliente_id):
    """ Exibir detalhes do cliente """
    return render_template('detalhe_clientes.html')

@cliente_route.route('/<int>:cliente_id>/edit')
def form_edit_clientes(cliente_id):
    """ Formulario para editar um cliente """
    cliente = None
    for c in CLIENTES:
        if c ['id'] == cliente_id:
            cliente = c
    return render_template('form_clientes.html', cliente=cliente)

@cliente_route.route('/<int>:cliente_id>/update', methods = ['PUT'])
def atualizar_clientes(cliente_id):
    """ Atualizar informacoes do cliente """
    pass

@cliente_route.route('/deletar_clientes/<int:cliente_id>', methods = ['DELETE'])
def deletar_clientes(cliente_id):
    """ Deletar informacoes do cliente """
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c ['id'] != cliente_id ]
    return{'delete':'ok'}