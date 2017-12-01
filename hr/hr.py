# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    opts = ["Show Table","Add","Remove","Update"]

    while True :

        ui.print_menu("Human Rsources Manager: ", opts, "Back to Main Menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file("hr/persons.csv")
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_number = ''.join(ui.get_inputs(["ID: "], "The ID of the line you want to remove? press (0) to cancel"))
            if id_existance(table,id_number) == False:
                if id_number == "0":
                    pass
                else:
                    ui.print_error_message('ID: %s does not exist in the file.' % id_number)
                    pass
            else:
                remove(table,id_number)
        elif option == "4":
            update_id = ''.join(ui.get_inputs(["ID: "], "The ID of the line you want to update? press (0) to cancel"))
            if id_existance(table,update_id) == False:
                if id_number == "0":
                    pass
                else:
                    ui.print_error_message('ID: %s does not exist in the file.' % update_id)
                    pass
            else:
                update(table,update_id)
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")

    if option == "0":
        pass

def id_existance(table,id_):

    for i in range(len(table)):
        if table[i][0] == id_ :
            return True
    
    return False

def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    ui.print_table(table,['ID','Name','Birth Date'])

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

    new_row = ui.get_inputs(['Name: ','Birth Date: '],"Please, give me the specs.")
    added_id = common.generate_random(table)
    new_row.insert(0,added_id)
    table.append(new_row)
    data_manager.write_table_to_file("hr/persons.csv",table)
    show_table(table)
    ui.print_error_message('The specs are added with ID: ' + added_id)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    for i in range(len(table)):
        if table[i][0] == id_:
            del(table[i])
            break
    
    data_manager.write_table_to_file("hr/persons.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been removed.' % id_)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    updated_row = ui.get_inputs(['Name: ','Birth Date: '],"Please, give me the specs.")
    updated_row.insert(0,id_)
    
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i,updated_row)
            del(table[i+1])
            break

    data_manager.write_table_to_file("hr/persons.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been updated.' % id_)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
