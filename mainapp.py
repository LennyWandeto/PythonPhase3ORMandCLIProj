from models.carpenter import Carpenter
from models.woodwork import Woodwork
from models.owner import Owner
from models.set import create_tables

def start():
    while True:
        print('\n1. Create a new carpenter')
        print('2. Create a new woodwork')
        print('3. Create a new owner')
        print('4. Assign a woodwork to a carpenter')
        print('5. List all carpenters')
        print('6. List all woodworks')
        print('7. List all owners')
        print('8. List all woodworks under a carpenter')
        print('9. List all woodworks under an owner')
        print('10. Delete a carpenter')
        print('11. Delete a woodwork')
        print('12. Delete an owner')
        print('13. Exit')
        choice = input('What would you like to do? ')