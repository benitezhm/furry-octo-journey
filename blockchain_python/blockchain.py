# Initializing our blockcahin list
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Miguel'
participants = set(['Miguel'])


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Add a new value as well as the las value of the blockchin to the block 

    Arguments:
        :sender: The sender of the coins
        :recipeint: the recipient of the coins
        :amount: The amount of coins sent with the transacion (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transacton = {
        'sender': 'MINNING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transacton)
    block = {
        'previous_hash': hashed_block,
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True


def hash_block(block):
    hashed_block = '-'.join([str(block[key]) for key in block])
    return hashed_block


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_transaction_value():
    """ Return the input of the user (a new trnasaction amount) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    print(' ')
    print('Please choose')
    print('1: Add new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
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
    """ Verify the current blockchain and return True if valid, Fals otherwise """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue

        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Trasaction failed!')
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'transactions': [{'sender': 'Luz', 'recipient': 'Miguel', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was inavalid, please pick a value form the list')

    if not verify_chain():
        print_blockain_elements()
        print('Invalid blockchain')
        waiting_for_input = False

    print('Your balance is: ' + str(get_balance('Miguel')))

print('Done!')
