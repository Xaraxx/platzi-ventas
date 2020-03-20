
import csv
import os

CLIENTS_TABLE = '.client.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_client_from_storage():
    with open(CLIENTS_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        
        for row in reader:
            clients.append(row)
    

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENTS_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENTS_TABLE)
        os.rename(tmp_table_name, CLIENTS_TABLE)

def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)
    
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
 
    else:
        print('The client already exist in the data base.')


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        client_name = client['name']
        _print_not_name_in_client_list(client_name)

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):

        if idx == client_id:
            del clients['idx']
            break
        else:
            client_name = client['name']
            _print_not_name_in_client_list(client_name)

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('*' * 48)
    print('* W E L C O M E  TO  P L A T Z I - V E N T A S *')
    print('*' * 48)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[L]ist client')
    print('[S]earch client')

    print('*' * 48)


def _print_invalid():
    print('The command used is invalid.')

def _print_not_name_in_client_list(client_name):
    print('The Client: {} is not in clients list'.format(client_name))


def _print_name_in_client_list():
    print('The client is in clients list')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What\'s the client {}?'.format(field_name))

    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }

    return client


# def _get_client_name():
#     client_name = None

#     while not client_name:
#         client_name = input('What\'s the client name? ')

#         if client_name == 'exit':
#             print('this conditional')
#             break

#     if not client_name:
#         sys.exit()

#     return client_name


if __name__ == '__main__':
    _initialize_client_from_storage()
    _print_welcome()

    command = input().upper()
    
    if command == 'C':
        client = _get_client_from_user()
        create_clients(client)
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            _print_name_in_client_list()
        else:
            _print_not_name_in_client_list(client_name)
    else:
        _print_invalid()
    _save_clients_to_storage()
