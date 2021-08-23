# Initializing our blockcahin list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    """ Add a new value as well as the las value of the blockchin to the block 

    Arguments:
        :transaction_amount: The amount that shoudl be added
        :last_transaction: The last blockcahin transaction (defualt: [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Return the input of the user (a new trnasaction amount) as a float. """
    transaction_value = float(input('Your transaction amount please: '))
    return transaction_value


def get_user_choice():
    print(' ')
    print('Please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_input = input('Your choice: ')
    return user_input


def print_blockain_elements():
    # output all the blocks in the blockchain
    index = 1
    for block in blockchain:
        print('Outputting block ' + str(index))
        print(block)
        index += 1
    else:
        print('-' * 20)


def verify_chain():
    is_valid = True
    for block_index in range(1, len(blockchain)):
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    return is_valid


waiting_for_input = True

while waiting_for_input:
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was inavalid, please pick a value form the list')

    if not verify_chain():
        print_blockain_elements()
        print('Invalid blockchain')
        waiting_for_input = False


print('Done!')
