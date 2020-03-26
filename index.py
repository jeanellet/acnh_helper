import numpy as np
import pandas as pd


def remove_index(df):
    blankIndex = [''] * len(df)
    df.index = blankIndex


def initialize_data():
    bugs = pd.read_csv("Bugs.csv")
    fish = pd.read_csv("Fish.csv")
    fossils = pd.read_csv("Fossils.csv")
    nook_miles = pd.read_csv("NookMiles.csv")

    data = [bugs, fish, fossils, nook_miles]

    for d in data:
        remove_index(d)

    print("Hello! I am the ACNH Helper.")

    return data


def sort_by(df):
    print("Enter 'b' to go back")
    print("Here are the columns to sort by.")
    i = 1
    for col_name in df.columns:
        print(str(i)+": "+col_name)
        i += 1
    choice = input("Enter index of column to sort by:")

    if choice == 'b':
        return
    choice = int(choice)
    sorted = df.sort_values(by=[df.columns[choice-1]], na_position="first")
    print(sorted.to_string())

    sort_by(df)


def ask_user():
    print("--------------------------------------------------")
    print("What would you like to do? Enter number of choice.")
    print("1: Check bug")
    print("2: Check fish")
    print("3: Check fossil")
    # print("4: Check NookMile achievement")
    print("4: Nothing")

    # select a valid choice
    while True:
        try:
            choice = int(input("Selection: "))
            if choice < 1 or choice > 4:
                print("Please select a valid choice")
            else:
                break
        except ValueError:
            print("Please select a valid choice")

    # select a valid item
    while True:
        item, table, col_name = get_table(choice)
        if not item and not table:
            return 0
        # go back to selecting a category
        if item == 'b':
            return 1
        if item == 'all':
            print(table.to_string())
            sort_by(table)
            return 1
        item = item.capitalize()
        result = table.loc[table[col_name] == str(item)]
        if result.empty:
            print("No results found! Please spell correctly.")
        else:
            break

    # got valid name
    print("Here's some info on your selection:")
    print("--------------------------------------------------")
    print(result)
    return 1


# set variables according to choice
def get_table(choice):
    print("Enter 'b' to go back, 'all' for entire list")
    # Bug
    if choice == 1:
        table = bugs
        item = input("-----BUG-----\nEnter name of bug: ")
        col_name = "Bug"
    # Fish
    elif choice == 2:
        table = fish
        item = input("-----FISH-----\nEnter name of fish: ")
        col_name = "Fish"
    # Fossil
    elif choice == 3:
        table = fossils
        item = input("-----FOSSIL-----\nEnter name of fossil: ")
        col_name = "Fossil"
    # Nook Miles
    # elif choice == 4:
    #     table = nook_miles
    #     item = input("Enter name of Nook Mile achievement: ")
    #     col_name = "Task"
    # Nothing
    elif choice == 4:
        return 0, 0, 0
    else:
        print("ERROR: Invalid choice number.")
        return 0, 0, 0
    return item, table, col_name


if __name__ == '__main__':
    bugs, fish, fossils, nook_miles = initialize_data()

    print(nook_miles)
    while ask_user():
        pass

    print("Goodbye!")

