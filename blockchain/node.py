from blockchain import Blockchain
from verification import Verification

from uuid import uuid4


class Node:

    def __init__(self):
        self.id = 'Miguel'
        self.blockchain = Blockchain(self.id)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockain_elements()
            elif user_choice == '4':
                print(self.participants)
            elif user_choice == '5':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was inavalid, please pick a value form the list')

            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_blockain_elements()
                print('Invalid blockchain')
                waiting_for_input = False

            print('Balance of {}: {:6.2f}'.format(
                self.id, self.blockchain.get_balance()))

        print('Done!')

    def get_user_choice(self):
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

    def print_blockain_elements(self):
        # output all the blocks in the blockchain
        index = 1
        for block in self.blockchain.get_chain():
            print('Outputting block ' + str(index))
            print(block)
            index += 1
        else:
            print('-' * 20)

    def get_transaction_value(self):
        """ Return the input of the user (a new transaction amount) as a float. """
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return (tx_recipient, tx_amount)


node = Node()
node.listen_for_input()
