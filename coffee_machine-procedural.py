

# from os import fstatvfs
from functools import reduce
import random
from traceback import print_tb
import headman_game as headman

turnOn = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def printReportOfResources():
    print(f'''
        Water: {resources['water']}
        Milk: {resources['milk']}
        Coffee: {resources['coffee']}
    ''')

def checkResourcesIfEnough(coffeeType):
    
    v1 = resources['water']
    v2 =  getIngredients(coffeeType, 'water')
    if ( v1 < v2):
        return 0
    elif(resources['water'] < getIngredients(coffeeType, 'milk')):
        return 0
    elif(resources['water'] < getIngredients(coffeeType, 'coffee')):
        return 0
    return 1

def getIngredients(coffeeType, ingredient):
    if (coffeeType == 'espresso' and ingredient == 'milk'):
        return 0
    return MENU[coffeeType].get('ingredients')[ingredient]

def reduceResource(coffeeType):
    global resources # INCELEEEEEEE
    
    newResources = {
        'water': resources['water'] - MENU[coffeeType].get('ingredients')['water'],
        'milk':  resources['milk'] if coffeeType == 'espresso' else  resources['milk'] - MENU[coffeeType].get('ingredients')['milk'],
        'coffee': resources['coffee'] - MENU[coffeeType].get('ingredients')['coffee']
    }
    resources = newResources

def calculateCoins():
    terminate = ''
    totalCoins = 0
    while(terminate != 'okay'):
        coins = input(f'total coins: {totalCoins}\n please insert coins or type \'okay\' to terminate -->')

        if (coins == 'okay'):
            coins = coins
        elif('.' in coins):
            coins = float(coins)
        else:
            coins = int(coins)
        
        if (not (isinstance(coins, int) or isinstance(coins, float)) and coins != 'okay'):
            print('\n\tplease inert a coin or type \'okay\' you motherfucker!!\n')
            continue
        if (coins == 'okay'):
            terminate = 'okay'
            break
        print(type(coins))

        totalCoins = totalCoins + coins
    return totalCoins
        

def makeCoffee():
    # def makeEspresso():
    #     print()

    # def makeLatte():
    #     print()

    # def makeCappuccino():
    #     print()

    coffeeChoice = input('What would you like? (espresso / latte / cappuccino) ')
    if(not coffeeChoice in MENU):
         coffeeChoice = input('yanlis oldu.. What would you like? (espresso / latte / cappuccino) ')
    if (coffeeChoice == 'report'):
        printReportOfResources()
    isEnough = checkResourcesIfEnough(coffeeChoice)
    if (not isEnough):
        print('resources is not enough')
        turnOn = False
        return
    print('please insert coin')
    coins = calculateCoins()

    if (coins < MENU[coffeeChoice].get('cost')):
        print('Sorry that\'s not enough money. Money refunded.')
        turnOn = False
        return
    elif(coins > MENU[coffeeChoice].get('cost')):
        change = coins - MENU[coffeeChoice].get('cost')
        print(f'drink is in progress, here {change} dollars in change')
        print('report before purchasing latte')
        printReportOfResources()
        reduceResource(coffeeChoice)
        print('report after purchasing latte')
        printReportOfResources()
        
    else:
        print('drink is in progress')
        printReportOfResources()
        print('report before purchasing latte')
        printReportOfResources()
        reduceResource(coffeeChoice)
        print('report after purchasing latte')
        printReportOfResources()
    print('Here is your latte. Enjoy!”.')
    turnOn = False

while turnOn:
    makeCoffee()



# print(calculateCoins())

# checkResourcesIfEnough('latte', )

# print(getIngredients('espresso', 'milk'))

# print('5.5'.isdigit())
# print(isinstance('5.5', float))




