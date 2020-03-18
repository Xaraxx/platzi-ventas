
import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]
    

def list_clients():
    global clients
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
        _print_not_name_in_client_list(client_name)

def delete_client(client_name):
    global clients

    for idx, client in enumerate(clients):

        if idx == client_id:
            del clients['idx']
        else:
            _print_not_name_in_client_list(client_name)

def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
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

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What\'s the client name? ')

        if client_name == 'exit':
            print('this conditional')
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()
    
    if command == 'C':
        client = _get_client_from_user()
        create_clients(client)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
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
