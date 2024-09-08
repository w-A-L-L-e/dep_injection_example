#!/usr/bin/env python

# Author:           Walter Schreppers
# Description:      Small example to show simplest form of depenency injection 
class GmailClient:
    def __init__(self):
        self.service = 'Gmail client'

    def send(self, message):
        print(f'{self.service} : {message=}')

class FacebookClient:
    def __init__(self):
        self.service = 'Facebook client'

    def send(self, message):
        print(f'{self.service} : {message=}')


class Greeter:
    # we use depencency injection here so we can have a message with different clients
    def __init__(self, client):
        self.client = client

    def talk(self, name):
        # the logic here does not need to know anything about what type of client as long
        # as it has the send or any other methods used here this allows to refactor out common behaviou
        # and avoid code duplication
        self.client.send(f'Hello {name}')
        self.client.send('How is your day?')
        self.client.send(f'Goodbye {name}')
        print()


def add(a,b):
    return a+b

def tuple_vs_lists():
    print("tuple vs list examples:")
    # tuple vs list question I think my explanation was also a bit vague, its maybe better when I actually show it in code:
    tuptest = (2,3)
    listtest = [3,4]

    print( add(*tuptest) )
    print( add(*listtest) )

    # main difference is tuptest is a unique list of values that you cannot change after declaring
    # tuptest[1]= 4 # not allowed

    # a list/array you can however change
    listtest[1] = 5 # this is allowed
    print(add(*listtest))

if __name__ == '__main__':
    # greeter is able to greet using different types of clients that we pass as an object argument
    Greeter(FacebookClient()).talk('Kenny')
    Greeter(GmailClient()).talk('Walter')

    tuple_vs_lists()
