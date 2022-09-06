import choice
import view
import add
import delete
import edit


def main():
    """The starting point function of the program"""
    while True:
        choice.choices()
        usrchoice = input("\nEnter Number: ")
        if usrchoice == '1':
            view.viewData()
        elif usrchoice == '2':
            add.addData()
        elif usrchoice == '3':
            delete.delete()
        elif usrchoice == '4':
            edit.editData()
        elif usrchoice == '5':
            break
        else:
            print('You did not make a valid choice, try again.')
            main()

main()