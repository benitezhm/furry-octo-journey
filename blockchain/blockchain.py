from functools import reduce
import pickle

from block import Block
from transaction import Transaction

from hash_util import hash_block, hash_string_256

# Initializing our blockchain list
MINING_REWARD = 10

blockchain = []
open_transactions = []
OWNER = 'Miguel'
participants = set(['Miguel'])


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction.sender)
    return sender_balance >= transaction.amount


def add_transaction(recipient, sender=OWNER, amount=1.0):
    """ Add a new value as well as the las value of the blockchin to the block 

    Arguments:
        :sender: The sender of the coins
        :recipeint: the recipient of the coins
        :amount: The amount of coins sent with the transacion (default = 1.0)
    """
    transaction = Transaction(sender, recipient, amount)
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        save_data()
        participants.add(sender)
        participants.add(recipient)
        return True

    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = Transaction('MINNING', OWNER, MINING_REWARD)
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transactions, proof)
    blockchain.append(block)
    return True


def save_data():
    try:
        with open('blockchain.p', mode='wb') as file:
            data = {
                'chain': blockchain,
                'ot': open_transactions
            }
            file.write(pickle.dumps(data))
    except IOError:
        print('Save failed! File not found!')


def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.p', mode='rb') as file:
            file_content = pickle.loads(file.read())

            blockchain = file_content['chain']
            open_transactions = file_content['ot']
    except (IOError, IndexError):
        genesis_block = Block(0, '', [], 100, 0)
        blockchain = [genesis_block]
        open_transactions = []


load_data()


def valid_proof(transactions, last_hash, proof_number):
    guess = (str([tx.to_ordered_dict() for tx in transactions]) +
             str(last_hash) + str(proof_number)).encode()
    guess_hash = hash_string_256(guess)
    return guess_hash[0:2] == "00"


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions
                  if tx.sender == participant] for block in blockchain]
    open_tx_sender = [tx.amount
                      for tx in open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amount: tx_sum +
                         sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_sender, 0)

    tx_recipient = [[tx.amount for tx in block.transactions
                     if tx.recipient == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amount: tx_sum +
                             sum(tx_amount) if len(tx_amount) > 0 else tx_sum, tx_recipient, 0)

    return amount_received - amount_sent


def get_transaction_value():
    """ Return the input of the user (a new transaction amount) as a float. """
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
    """ Verify the current blockchain and return True if valid, False otherwise """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue

        if block.previous_hash != hash_block(blockchain[index - 1]):
            return False

        if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print("Proof of work is invalid")
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
            print('Transaction failed!')
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was inavalid, please pick a value form the list')

    if not verify_chain():
        print_blockain_elements()
        print('Invalid blockchain')
        waiting_for_input = False

    print('Balance of {}: {:6.2f}'.format(OWNER, get_balance(OWNER)))

print('Done!')
