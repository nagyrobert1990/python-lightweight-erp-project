import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(1)
    
'''
def id_existance(table,id_):
    for i in range(len(table)):
        if table[i][0] == id_ :
            return True
    return False


def show_table(table):
    ui.print_table(table,['ID','Title','Manufacturer','Price','In Stock'])
    pass


def add(table):
    new_row = ui.get_inputs(['Title: ','Manufacturer: ','Price: ','In Stock: '],"Please, give me the specs.")
    added_id = common.generate_random(table)
    new_row.insert(0,added_id)
    table.append(new_row)
    data_manager.write_table_to_file("store/games.csv",table)
    show_table(table)
    ui.print_error_message('The specs are added with ID: ' + added_id)

    return table


def remove(table, id_):    
    for i in range(len(table)):
        if table[i][0] == id_:
            del(table[i])
            break
    
    data_manager.write_table_to_file("store/games.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been removed.' % id_)

    return table


def update(table, id_):
    updated_row = ui.get_inputs(['Title: ','Manufacturer: ','Price: ','In Stock: '],"Please, give me the specs.")
    updated_row.insert(0,id_)
    
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i,updated_row)
            del(table[i+1])
            break

    data_manager.write_table_to_file("store/games.csv",table)
    show_table(table)
    ui.print_error_message('The row with ID: %s has been updated.' % id_)

    return table
'''

# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
