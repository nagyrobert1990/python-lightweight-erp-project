import os
import ui
import data_manager
import common


def start_module():

    common.submenu_of_managements(4)

# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    def quicksor(lst):
        if not lst:
            return []
        return (quicksor([x for x in lst[1:] if x <  lst[0]])
                + [lst[0]] +
                quicksor([x for x in lst[1:] if x >= lst[0]]))

    letter_count = 0
    a = []
    the_id = ''
    the_name = ''
    for line in range(len(table)):
        for line_i in range(line, len(table)):
            if len(table[line][1]) < len(table[line_i][1]):
                letter_count = len(table[line_i][1])
                the_id = table[line_i][0]
                the_name = table[line_i][1]
    a.append(the_name)
    for line in range(len(table)):
        if letter_count == len(table[line][1]):
            a.append(table[line][1])
    
    if len(a) > 1:
        the_name = quicksor(a)[0]
        for line in range(len(table)):
            if table[line][1] == the_name:
                the_id = table[line][0]
                break
        
    return str(the_id)


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    subscribe = []
    for line in range(len(table)):
        temp_str = ""
        if table[line][3] == "1":
            temp_str = table[line][2]+";"+table[line][1]
            subscribe.append(temp_str)
    
    return subscribe

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
