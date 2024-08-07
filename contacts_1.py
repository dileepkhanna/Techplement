#command line contact management
contact_file='contacts_txt.txt'

def load_contacts():
    contacts={}
    try:
        with open(contact_file,'r')as file:
            for line in file:
                name,phone,email=line.split(',')
                contacts[name]={'phone':phone,'email':email,}
    except FileNotFoundError:
        print(f'{contact_file}not found.  Creating a new one')
    except Exception as e:
        print(f'An error occurred while loasing contacts:{e}')
    return contacts

def save_contact(contacts):
    with open(contact_file,'w') as file:
        for name,i in contacts.items():
            file.write(f'{name},{i['phone']},{i['email']}\n')

def add_contact(contacts):
    name=input('enter name:')
    phone=int(input('enter phone number:'))
    email=input('enter email address:')
    contacts[name]={'phone':phone,'email':email}
    save_contact(contacts)
    print('- - - - - - - - - CONTACTS ADD SUCCESSFULLY- - - - - - - - -')

def search_contact(contacts):
    name=input('enter name to search:')
    if name in contacts:
        print(f'name:{name}')
        print(f'phone:{contacts[name]['phone']}')
        print(f'email:{contacts[name]['email']}')
    else:
        print('- - - - - - - - - CONTACTS NOT FOUND- - - - - - - - -')
def update_contact(contacts):
    name=input('Enter name of the contact to update:')
    if name in contacts:
        phone=input('Enter new phone number:')
        email=input('Enter new email address:')
        save_contact(contacts)
        print('contact update successfully')
    else:
        print('contact not found')

def main():
    contacts=load_contacts()
    while True:
        print('- - - - - - - - -CONTACT MANAGEMENT SYSTEM- - - - - - - - -\n')
        print('1.Add Contact')
        print('2.Search Contact')
        print('3.Update Contact')
        print('4.Exit')
        choice=input('Enter Your Choice:')
        if choice=='1':
            add_contact(contacts)
        elif choice=='2':
            search_contact(contacts)
        elif choice=='3':
            update_contact(contacts)
        elif choice=='4':
            break
        else:
            print('Invalid choice. Please try again.')
if __name__=="__main__":
   main()       
            
