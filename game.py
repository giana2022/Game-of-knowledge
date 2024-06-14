# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:21:16 2024

@author: Juan
"""
import random
import time
from questions_with_categories import questions_answers, especial_categories

def main():
    game()

def game():
    #variables 
    name = ask_name()
    rounds = 1
    game_over = False
    questions_solved = []
    category = game_presentation()
    right_choice = ["1","2","3","4"]
    points = 0
    
    #game loop
    while not game_over:
        n_option = 0
        #Say the user what round is
        print(f'Round {rounds}')
        
        #Select the question
        input("Press enter to see the question: >")
        question = select_question(rounds,questions_solved,category)
        
        #Shows the questions 
        print(f"Well, {name}...")
        print('Your question is...')
        time.sleep(1)
        print(question[0])
        print('Your options:')
        time.sleep(3)
        for i in question[1]:
            n_option += 1
            print(f'{n_option}. {i}')
        
        #Input of the user and control
        users_answer = input('Write your answer: ')
        while users_answer not in right_choice:
            print('Incorrect input')
            users_answer = input('Write your answer: ')
        users_answer = question[1][int(users_answer)-1]
        
        #Check the users input
        if users_answer == question[2]:
            print("Your answer is right! It was", question[2])
            #Consecuences of the users input
            points = add_points(points,rounds)
            print(f'Your points: {points}')
            print('--------------------------')
            print()
            print()
        else:
        #Conditions of game over
            print('Your answer is wrong! It was', question[2])
            print('Your game is finished')
            game_over = True
        if rounds == 10:
            game_over = True
        
        rounds += 1
    print('Game over!')
    print(f"Your points are: {points}")

def ask_name():
    '''Check if the name is not with numbers and return it'''
    n = None
    while n == None:
        n = input("What's your name? ")
        if n.isalpha():
            return n
        else:
            print('It cannot be a number!')
            n = None

def add_points(point, round_number):
    '''Add pointsaccording to the level'''
    if not isinstance(round_number, int) or round_number < 1:
       raise ValueError("Round number must be a positive integer.")
    
    # Use a dictionary for efficient point lookup and potential extension
    points_per_round = {
         1: 100,
         2: 100,
         3: 500,
         4: 500,
         5: 500,
         6: 750,
         7: 1000,
         8: 1000,
         9: 1500, 
         10: 2000
     }
    # Award points based on the round number using dictionary lookup
    return point + points_per_round.get(round_number, 2000)

def game_presentation():
    '''Presents the game and a short explanation of the game'''
    print('*********Knowledge Lover*********')
    print('Hi! This is a game of questions and answers')
    input('Press enter to continue >')
    print('You must write the number where your choice is')
    input(">")
    print('If you select a wrong option, the game will finish')
    input(">")
    print('Good Luck!!!!')
    print('-----------------------------')
    print('Select a category:')
    print('1. Random category')
    print('2. Science')
    print('3. History')
    print('4. Literature')
    categories = {
        '1':'Random',
        '2':'Science',
        '3':'History',
        '4':'Literature',
        }
    category = input('Enter the number of your choice: ')
    while category not in ['1', '2', '3', '4']:
        print('Invalid choice!')
        category = input('Enter the number of your choice: ')
    for k,v in categories.items():
        if k == category:
            cat_select = v
    print(f'Awesome! You have choiced the {cat_select}')
    return cat_select

def select_question(level, questions_solved, category):
        selected = None    
        '''Here selects a random question from the module questions'''
        if category == 'Random':
            while selected == None:
                if 1 <= level <= 3:
                    q = questions_answers['easy']
                elif 4 <= level <= 6:
                    q = questions_answers['medium']
                elif 7 <= level < 9:
                    q = questions_answers['hard']
                elif level >= 9:
                    q = questions_answers['hardest']
                selected = random.choice(q)
                if level in [4, 7, 9]:
                    time.sleep(1)
                    print()
                    print("Let's raise the difficulty!")
                    print()
                if selected not in questions_solved:
                    questions_solved.append(selected)
                    return selected
                else: 
                    selected = None
        
        else:
        #Here select a category selected by the user
           group_questions = especial_categories
           #Selects the level by category
           while selected == None:
               if 1 <= level <= 3:
                   q = group_questions[category]['easy']
               elif 4 <= level <= 6:
                   q = group_questions[category]['medium']
               elif 7 <= level < 9:
                   q = group_questions[category]['hard']
               elif level >= 9:
                   q = group_questions[category]['hardest']
               selected = random.choice(q)
               if level in [4, 7, 9]:
                   time.sleep(1)
                   print()
                   print("Let's raise the difficulty!")
                   print()
               if selected not in questions_solved:
                   questions_solved.append(selected)
                   return selected
               else: 
                   selected = None
           
    

if __name__ == '__main__':
    main()