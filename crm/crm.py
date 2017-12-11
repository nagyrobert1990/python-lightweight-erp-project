# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    os.system('clear')

    opts = ["Show Table","Add","Remove","Update"]

    while True :

        ui.print_menu("Customer Relationship Management: ", opts, "Back to Main Menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file("crm/customers.csv")
        os.system('clear')
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
    # name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)

    ui.print_table(table,['ID','Name','Email','Subscribed'])

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

    new_row = ui.get_inputs(['Name: ','Email: ','Subscribed: '],"Please, give me the specs.")
    added_id = common.generate_random(table)
    new_row.insert(0,added_id)
    table.append(new_row)
    data_manager.write_table_to_file("crm/customers.csv",table)
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
    
    data_manager.write_table_to_file("crm/customers.csv",table)
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

    updated_row = ui.get_inputs(['Name: ','Email: ','Subscribed: '],"Please, give me the specs.")
    updated_row.insert(0,id_)
    
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i,updated_row)
            del(table[i+1])
            break

    data_manager.write_table_to_file("crm/customers.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been updated.' % id_)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass
