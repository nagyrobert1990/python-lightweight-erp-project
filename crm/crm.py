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

    longest = [["",None]]
    for i in range(len(table)):
        if len(table[i][1]) > len(longest[0][0]):
            longest = [[table[i][1],table[i][0]]]
        elif len(table[i][1]) == len(longest[0][0]):
            longest.append([table[i][1],table[i][0]])

    lst = quicksor(longest)
    
    return lst[0][1]


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
