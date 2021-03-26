# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:31:00 2021

@author: Sylwester
"""



import random
import time
import pathlib
import hashlib
import operator

level = 1
score = 1
rounds = 3
limit = 30

def sign_up():
    username = input("Enter a username: ")
    while True:
        password = input("Enter a password (6 character long): ")
        if len(password) < 6:
            password = input("Enter a password (6 character long): ")
        else:
            break
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
    # print(hashed_password)
    with open("credentials.txt", mode="w") as writable_password:
        writable_password.write(username+"\n")
        writable_password.write(hashed_password+"\n")

    log_in()


def log_in():
    print("Please, enter your usarname and password to sign in")
    username = input("Username: ")+"\n"

    while True:
        password = input("Password (6 character long): ")
        if len(password) < 6:
            password = input("Password (6 character long): ")
        else:
            break

    with open(".credentials.txt", mode="r") as credentials:
        user_data = credentials.readlines()
        for i in user_data:
            # print(i)
            if i == username and hashlib.sha1(password.encode("utf-8")).hexdigest()+"\n" == user_data[user_data.index(i)+1]:
                print("You have succesfully signed in")
                start_game()
                break


def start_game(limit):
    start = "ll"
    start = input("Please press any key to start the game")
    # print(start)
    if start != "ll" and level == 1:
        level_one(limit)


overall = 0


def level_one(limit):
    global score
    global overall
    global rounds


    while rounds > 0:

        if score <= 0:
            return print("You lost!")
        answer = 0
    
        random_operator = random.choice(["+", "-"])
        if random_operator == "+":
            first_number = random.randint(1, limit/2)
            second_number = random.randint(1, limit/2)
            response = input(f"{first_number} + {second_number}: ")
            answer = first_number + second_number
            if int(response) == answer:
                score += 10
                overall += 10
                rounds -= 1
                print(score)
                level_one(limit)
            else:
                score -= 10
                rounds -= 1
                print(score)
                level_one(limit)

        else:
            first_number = random.randint(1, limit)
            second_number = random.randint(1, first_number)
            response = input(f"{first_number} - {second_number}: ")
            answer = first_number - second_number
            if int(response) == answer:
                score += 10
                rounds -= 1
                print(score)
                level_one(limit)
            else:
                score -= 10
                rounds -= 1
                print(score)
                level_one(limit)
        # print(first_number, second_number, answer)

# def main():

# if __name__ = "__main__":
#     main()
# sign_up()
# log_in()
start_game(limit)
# I want to implement

# old project 22

