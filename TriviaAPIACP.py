#using true or false option for all categories

import requests
import random
import html

def animalQuestions():
    animal_API_URL = "https://opentdb.com/api.php?amount=5&category=27&type=boolean"
    response = requests.get(animal_API_URL)
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0 and data ["results"]:
            return data["results"]
    return None

def generalQuestions():
    general_API_URL = "https://opentdb.com/api.php?amount=5&category=9&type=boolean"
    response = requests.get(general_API_URL)
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0 and data ["results"]:
            return data["results"]
    return None
        
def vehicleQuestions():
    vehicle_API_URL = "https://opentdb.com/api.php?amount=5&category=28&type=boolean"
    response = requests.get(vehicle_API_URL)
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0 and data ["results"]:
            return data["results"]
    return None

def run_quiz():
    score = 0
    print("Welcome to the quiz API! Which quiz would you like?")
    answer = input("Animal (1), General (2), or Vehicle (3) ? Please enter your answer. ")

    if answer.lower() == "animal" or answer == "1":
        questions = animalQuestions()

    elif answer.lower() == "general" or answer == "2":
        questions = generalQuestions()

    elif answer.lower() == "vehicle" or answer == "3":
        questions = vehicleQuestions()
    else:
        print("Invalid option.")
        return
    
    for q in questions:
        question_content = html.unescape(q["question"])
        correct_answer = q["correct_answer"]

        print("\n" + question_content)
        user_answer = input("True or False?").capitalize()

        if user_answer == correct_answer:
            print("Correct.")
            score += 1
        else: print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"\nHere is your final score: {score}/{len(questions)}")

run_quiz()