from random import randint
import string
import os
import ui
import data_manager


def generate_random(table):
    generated = ''
    list_lowercase = string.ascii_lowercase
    list_uppercase = string.ascii_uppercase
    list_numbers = string.digits
    list_misc = ["!","@","#","$","%","^","&","*","(",")","?"]
    
    while True :

        while len(generated)<8:
            choose = randint(0,3)
            generated = generated + list_lowercase[randint(0,len(list_lowercase)-1)] + list_uppercase[randint(0,len(list_uppercase)-1)] + list_numbers[randint(0,len(list_numbers)-1)] + list_misc[randint(0,len(list_misc)-1)]
            if choose == 0:
                randomchar = randint(0,len(list_lowercase)-1)
                generated = generated + list_lowercase[randomchar]
            elif choose == 1:
                randomchar = randint(0,len(list_uppercase)-1)
                generated = generated + list_uppercase[randomchar]
            elif choose == 2:
                randomchar = randint(0,len(list_numbers)-1)
                generated = generated + list_numbers[randomchar]
            else:
                randomchar = randint(0,len(list_misc)-1)
                generated = generated + list_misc[randomchar]

        for i in range(len(table)):

            if table[i][0] != generated:

                return generated


def submenu_of_managements(management):
    submenu_titles = ["Sales Manager: ","Store Manager: ","Inventory Manager: ", "Human Resources Manager: ","Customer Relationship Management: ","Accounting Manager: "]
    file_paths = ["sales/sales.csv","store/games.csv","inventory/inventory.csv","hr/persons.csv","crm/customers.csv","accounting/items.csv"]
    title_line_outputs = [['ID','Title','Price','Month','Day','Year','Customer ID'],
    ['ID','Title','Manufacturer','Price','In Stock'],
    ['ID','Name','Manufacturer','Purchase Date','Durability'],
    ['ID','Name','Birth Date'],
    ['ID','Name','Email','Subscribed'],
    ['ID','Month','Day','Year','Type','Amount']]
    title_line_inputs = [['Title: ','Price: ','Month: ','Day: ','Year: ','Customer ID: '],
    ['Title: ','Manufacturer: ','Price: ','In Stock: '],
    ['Name: ','Manufacturer: ','Purchase Date: ','Durability: '],
    ['Name: ','Birth Date: '],
    ['Name: ','Email: ','Subscribed: '],
    ['Month: ','Day: ','Year: ','Type: ','Amount: ']]

    os.system('clear')
    opts = ["Show Table","Add","Remove","Update"]
    
    while True :
        ui.print_menu(submenu_titles[management], opts, "Back to Main Menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(file_paths[management])
        os.system('clear')

        if option == "1":
            show_table(table, title_line_outputs[management])
        elif option == "2":
            add(table,title_line_inputs[management],title_line_outputs[management],file_paths[management])
        elif option == "3":
            id_number = ''.join(ui.get_inputs(["ID: "], "The ID of the line you want to remove? press (0) to cancel"))
            if id_existance(table,id_number) == False:
                if id_number == "0":
                    pass
                else:
                    ui.print_error_message('ID: %s does not exist in the file.' % id_number)
                    pass
            else:
                remove(table,id_number,file_paths[management])
                show_table(table,title_line_outputs[management])
                ui.print_error_message('The row with ID: %s has been removed.' % id_number)
        elif option == "4":
            update_id = ''.join(ui.get_inputs(["ID: "], "The ID of the line you want to update? press (0) to cancel"))
            if id_existance(table,update_id) == False:
                if update_id == "0":
                    pass
                else:
                    ui.print_error_message('ID: %s does not exist in the file.' % update_id)
                    pass
            else:
                update(table,update_id,title_line_inputs[management],file_paths[management])
                show_table(table,title_line_outputs[management])
                ui.print_error_message('The row with ID: %s has been updated.' % update_id)
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

def show_table(table,title_line_out):
    ui.print_table(table,title_line_out)
    pass

def add(table,title_line_in,title_line_out,filename):
    new_row = ui.get_inputs(title_line_in,"Please, give me the specs.")
    added_id = generate_random(table)
    new_row.insert(0,added_id)
    table.append(new_row)
    data_manager.write_table_to_file(filename,table)
    show_table(table,title_line_out)
    ui.print_error_message('The specs are added with ID: ' + added_id)

    return table

def remove(table, id_, filename):
    for i in range(len(table)):
        if table[i][0] == id_:
            del(table[i])
            break
    
    data_manager.write_table_to_file(filename,table)
    
    return table


def update(table, id_, title_line_in, filename):
    updated_row = ui.get_inputs(title_line_in, "Please, give me the specs.")
    updated_row.insert(0,id_)
    
    for i in range(len(table)):
        if table[i][0] == id_:
            table.insert(i,updated_row)
            del(table[i+1])
            break

    data_manager.write_table_to_file(filename,table)
    
    return table