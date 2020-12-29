# Beginner - Higher Lower Game Project

import random
from os import system
from day014_art import logo, vs
from day014_game_data import data

def get_random_data():
    return random.choice(data)

def format_data(data):
    """
    資料格式化
    """
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print(logo)
    
    score = 0
    is_continue = True
    compare_a = get_random_data()
    against_b = get_random_data()
    
    while is_continue:
        compare_a = against_b
        against_b = get_random_data()
        
        while compare_a == against_b:
            against_b = get_random_data()
        
        print(f"Compare A: {format_data(compare_a)}.")
        print(vs)
        print(f"Against B: {format_data(against_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = compare_a["follower_count"]
        b_follower_count = against_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        
        system("cls")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()