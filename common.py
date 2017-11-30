# implement commonly used functions here

from random import randint
import string

# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''

    # your code

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