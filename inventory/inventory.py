import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(2)

'''
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
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)

    ui.print_table(table,['ID','Name','Manufacturer','Purchase Date','Durability'])

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

    new_row = ui.get_inputs(['Name: ','Manufacturer: ','Purchase Date: ','Durability: '],"Please, give me the specs.")
    added_id = common.generate_random(table)
    new_row.insert(0,added_id)
    table.append(new_row)
    data_manager.write_table_to_file("inventory/inventory.csv",table)
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
    
    data_manager.write_table_to_file("inventory/inventory.csv",table)
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

    updated_row = ui.get_inputs(['Name: ','Manufacturer: ','Purchase Date: ','Durability: '],"Please, give me the specs.")
    updated_row.insert(0,id_)
    
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i,updated_row)
            del(table[i+1])
            break

    data_manager.write_table_to_file("inventory/inventory.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been updated.' % id_)

    return table
'''

# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    # your code

    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
