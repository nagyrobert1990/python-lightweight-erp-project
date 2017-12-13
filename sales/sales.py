import os
import ui
import data_manager
import common


def start_module():
        
    common.submenu_of_managements(0)


def get_lowest_price_item_id(table):
    lowest_price_id = []
    lowest_price = int(table[0][2])

    for i in range(len(table)):
        if int(table[i][2]) < lowest_price:
            lowest_price = int(table[i][2])
    
    for i in range(len(table)):
        if int(table[i][2]) == lowest_price:
            lowest_price_id.append(table[i][0])

    lowest_price_id = list(reversed(common.list_order(lowest_price_id)))

    return lowest_price_id[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    new_table = []

    for line in table:
        curr_year = int(line[5])
        curr_month = int(line[3])
        curr_day = int(line[4])

        if curr_year >= year_from and curr_year <= year_to:
            if curr_month >= month_from and curr_month <= month_to:
                if curr_day >= day_from and curr_day < day_to:
                    new_table.append(line)

    return new_table


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None in case of non-existing id
    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    table = data_manager.get_table_from_file("sales.csv")
    if common.is_id_exists(id) == True:
        for line in table:
            if line[0] == id:
                return line[1]
    
    
def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    if common.is_id_exists(id) == True:
        for line in table:
            if line[0] == id:
                return line[1]


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """
    last_sold_id = ""
    table = data_manager.get_table_from_file("sales/sales.csv")
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[0])
            return last_sold_id


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    last_sold_id = ""
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[0])
            return last_sold_id


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    last_sold_id = ""
    dates = []

    for line in table:
        temp = []
        temp.append(int(line[5]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        dates.append(temp)

    dates = list(reversed(common.list_order(dates)))
    
    for line in table:
        if dates[0][0] == int(line[5]) and dates[0][1] == int(line[3]) and dates[0][2] == int(line[4]):
            last_sold_id = str(line[1])
            return last_sold_id


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    table = data_manager.get_table_from_file("sales/sales.csv")
    sum_of_prices = 0

    for ids in item_ids:
        for line in table:
            if ids == line[0]:
                sum_of_prices += int(line[2])
    
    return sum_of_prices


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    sum_of_prices = 0

    for ids in item_ids:
        for line in table:
            if ids == line[0]:
                sum_of_prices += int(line[2])
    
    return sum_of_prices


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    table = data_manager.get_table_from_file("sales/sales.csv")

    for line in table:
        if sale_id == line[0]:
            return str(line[6])


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    for line in table:
        if sale_id == line[0]:
            return str(line[6])


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    table = data_manager.get_table_from_file("sales/sales.csv")
    customer_ids = set()

    for line in table:
        if line[6] not in customer_ids:
            customer_ids.add(line[6])
    
    return customer_ids


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """

    customer_ids = set()

    for line in table:
        if line[6] not in customer_ids:
            customer_ids.add(line[6])
    
    return customer_ids


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    table = data_manager.get_table_from_file("sales/sales.csv")
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_ids_for_customer_ids = {}

    for ids in all_customer_ids:
        temp = []
        for line in table:
            if ids == line[6]:
                temp.append(line[0])
        sales_ids_for_customer_ids[ids] = temp

    return sales_ids_for_customer_ids


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_ids_for_customer_ids = {}

    for ids in all_customer_ids:
        temp = []
        for line in table:
            if ids == line[6]:
                temp.append(line[0])
        sales_ids_for_customer_ids[ids] = temp

    return sales_ids_for_customer_ids


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    table = data_manager.get_table_from_file("sales/sales.csv")
    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_per_customers = {}

    for ids in all_customer_ids:
        sales_counter = 0
        for line in table:
            if ids == line[6]:
                sales_counter += 1
        sales_per_customers[ids] = sales_counter
    
    return sales_per_customers


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    all_customer_ids = list(get_all_customer_ids_from_table(table))
    sales_per_customers = {}

    for ids in all_customer_ids:
        sales_counter = 0
        for line in table:
            if ids == line[6]:
                sales_counter += 1
        sales_per_customers[ids] = sales_counter
    
    return sales_per_customers
