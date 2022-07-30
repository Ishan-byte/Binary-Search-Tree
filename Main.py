from msilib.schema import Binary
from re import A
from BSTNode import *
from BST import *
from Currency_.Dollar import *

if __name__ == "__main__":
    print("\n")
    print("... Program starts here ...")
    print("Welcome to our program that demonstrates the usage of Binary Search Tree for storing Currency objects")
    print("\n")

    # Dollars 
    Dollars = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00]

    # Currency
    Currency = []

    # Creating dollar objects 
    for d in Dollars:
        newObj = Dollar(d)
        Currency.append(newObj)

    # Creating a binary search tree object
    BinarySearchTree  = BST()

    # Binary Search Tree has been seeded
    for currency in Currency:
        BinarySearchTree.insert(currency)
    
    print("Binary Tree Seeded.")
        
    # Operations
    BinarySearchTree.printallTraversals(BinarySearchTree.root)
    print("\n")


    # User Interactivity
    operations = ["1. Add a leaf node", "2. Search a leaf node", "3. Delete a leaf node", "4. Print Output of Traversals", "5. Quit"] 
    user_choice = 0

    while user_choice != 5:
        print("Select an operation: ")
        for operation in operations:
            print(operation)
        
        print("\n")

        user_choice = int(input("Select an specific option: "))
        print("\n")

        if user_choice == 1:
            value = float(input("Enter a value to insert in the BST: "))
            if(value < 0):
                print("Please input a valid value. You cannot enter an negative value for insertion")
                print("\n")
                continue

            elif(BinarySearchTree.search(value) == True):
                print("The value already exists in the Binary Search Tree.")
                print("\n")
                continue

            else:
                print("\n")
                newObj = Dollar(value) 
                BinarySearchTree.insert(newObj)
                print("Successfully inserted in the Binary Search Tree")


        elif user_choice == 2:
            value = float(input("Enter a value to search in the BST: "))
            print("\n")
            if BinarySearchTree.search(value) == True:
                print(f"{value} was found in the Binary search tree")
            else:
                print(f"{value} was not found in the Binary search tree")

        elif user_choice == 3:
            value = float(input("Enter a value to search in the BST: "))
            print("\n")
            if(BinarySearchTree.search(value) == False):
                print("The value doesnot exists in the Binary Search Tree.")
                print("\n")
                continue
            curr = BinarySearchTree.delete(BinarySearchTree.root, value)
            print("Successfully Deleted")


        elif user_choice == 4:
            BinarySearchTree.printallTraversals(BinarySearchTree.root)


        elif user_choice == 5:
            print("End state of the Binary Search Tree")
            print("\n")
            BinarySearchTree.printallTraversals(BinarySearchTree.root)
            print("\n")
            print("*** Program ends ***")
            break

        print("\n")


