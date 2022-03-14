import csv
from contatos.models import Categoria, Contato


def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        nome = item.get('nome')
        sobrenome = item.get('sobrenome')
        telefone = item.get('telefone')
        email = item.get('email')
        _cat = item.get('categoria')
        cat = Categoria.objects.filter(nome=_cat).first()
        
        obj = Contato(
            nome=nome,
            sobrenome=sobrenome,
            telefone=telefone,
            email=email,
            categoria=cat,    
        )
        
        aux.append(obj)
    
    return aux


data = csv_to_list('poppulated/contacts.csv')
print(data)
list_obj = save_data(data)
print(list_obj)
Contato.objects.bulk_create(list_obj)
