from models.carpenter import Carpenter
from models.woodwork import Woodwork
from models.owner import Owner
from models.set import create_tables

def start():
    create_tables()
    while True:
        print('\n1. Create a new carpenter')
        print('2. Create a new woodwork')
        print('3. Create a new owner')
        print('4. Assign a woodwork to a carpenter')
        print('5. Assign a woodwork to a owner')
        print('6. List all carpenters')
        print('7. List all woodworks')
        print('8. List all owners')
        print('9. List all woodworks under a carpenter')
        print('10. List all woodworks under an owner')
        print('11. Delete a carpenter')
        print('12. Delete a woodwork')
        print('13. Delete an owner')
        print('14. Exit')
        choice = input('What would you like to do? ')
    
        if choice == '1':
            name = input('What is the carpenter\'s name? ')
            number = input('What is the carpenter\'s number?(This choice is optional): ')
            if number == None:
                Carpenter(name) 
            else:
                Carpenter(name, number)
        
        elif choice == '2':
            name = input('What is the woodwork\'s name? ')
            type = input('What is the woodwork\'s type? ')
            price = input('What is the woodwork\'s price? ')
            Woodwork(name, type, price)
        
        elif choice == '3':
            name = input('What is the owner\'s name? ')
            description = input('Write the owner\'s description: ')
            Owner(name, description)
        
        elif choice == '4':
            woodwork_name = input('What is the woodwork\'s name? ')
            woodwork = Woodwork.get_by_name(woodwork_name)
            if woodwork == []:
                print('The woodwork does not exist')
            carpenter_name = input('What is the carpenter\'s name? ')
            carpenter = Carpenter.get_by_name(carpenter_name)
            if carpenter == []:
                print('The carpenter does not exist')
            Woodwork.assign_woodwork_to_carpenter(woodwork[0], carpenter[0])
        
        elif choice == '5':
            woodwork_name = input('What is the woodwork\'s name? ')
            woodwork = Woodwork.get_by_name(woodwork_name)
            if woodwork == []:
                print('The woodwork does not exist')
            owner_name = input('What is the owner\'s name? ')
            owner = Owner.get_by_name(owner_name)
            if owner == []:
                print('The owner does not exist')
            Woodwork.assign_woodwork_to_owner(woodwork[0], owner[0])

        
        elif choice == '6':
            carpenters = Carpenter.get_all()
            if carpenters == []:
                print('There are no carpenters')
            for carpenter in carpenters:
                print(carpenter)
        
        elif choice == '7':
            woodworks = Woodwork.get_all()
            if woodworks == []:
                print('There are no woodworks')
            for woodwork in woodworks:
                print(woodwork)
        
        elif choice == '8':
            owners = Owner.get_all()
            if owners == []:
                print('There are no owners')
            for owner in owners:
                print(owner)
        
        elif choice == '9':
            carpenter_name = input('What is the carpenter\'s name? ')
            carpenter = Carpenter.get_by_name(carpenter_name)
            if carpenter == []:
                print('The carpenter does not exist')
            woodworks = Woodwork.get_by_carpenter(carpenter_name)
            if woodworks == []:
                print('The carpenter does not have any woodworks')
            for woodwork in woodworks:
                print(woodwork)
        
        elif choice == '10':
            owner_name = input('What is the owner\'s name? ')
            owner = Owner.get_by_name(owner_name)
            if owner == []:
                print('The owner does not exist')
            woodworks = Woodwork.get_by_owner(owner_name)
            if woodworks == []:
                print('The owner does not have any woodworks')
            for woodwork in woodworks:
                print(woodwork)
        
        elif choice == '11':
            carpenter_name = input('What is the carpenter\'s name? ')
            carpenter = Carpenter.get_by_name(carpenter_name)
            if carpenter == None:
                print('The carpenter does not exist')
            Carpenter.delete_carpenter(carpenter_name)
        
        elif choice == '12':
            woodwork_name = input('What is the woodwork\'s name? ')
            woodwork = Woodwork.get_by_name(woodwork_name)
            if woodwork == None:
                print('The woodwork does not exist')
            Woodwork.delete_woodwork(woodwork_name)
        
        elif choice == '13':
            owner_name = input('What is the owner\'s name? ')
            owner = Owner.get_by_name(owner_name)
            if owner == None:
                print('The owner does not exist')
            Owner.delete_owner(owner_name)
        
        elif choice == '14':
            print("Thank you for using our WoodWork Database!")
            break

start()