#!/usr/bin/env python

# Author: Walter Schreppers
# Small example to show depenency injection 

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

    def greet(self):
        self.client.send('Hello world')


def add(a,b):
    return a+b


if __name__ == '__main__':
    # greeter is able to greet using different types of clients that we pass as object argument
    msg1 = Greeter(FacebookClient())
    msg2 = Greeter(GmailClient())

    msg1.greet()
    msg2.greet()

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
