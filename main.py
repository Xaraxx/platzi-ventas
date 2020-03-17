
import sys

clients = 'pablo,ricado, '
    

def list_clients():
    global clients
    print(clients)


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('The client already exist in the data base.')


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        _print_not_name_in_client_list(client_name)

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _print_not_name_in_client_list(client_name)

def search_client(client_name):
    global clients
    clients_list = clients.split(',')

    for client in clients_list:
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
    print('[S]earch client')

    print('*' * 48)


def _print_invalid():
    print('The command used is invalid.')

def _print_not_name_in_client_list(client_name):
    print('The Client: {} is not in clients list'.format(client_name))


def _print_name_in_client_list():
    print('The client is in clients list')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What\'s the client name? ')

        if client_name == 'exit':
            break

        if not client_name:
            sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()
    
    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the updated client name?')
        update_client(client_name, updated_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            _print_name_in_client_list()
        else:
            _print_not_name_in_client_list(client_name)
    else:
        _print_invalid()
