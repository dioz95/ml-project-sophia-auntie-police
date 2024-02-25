import pickle
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

model = pickle.load(open('gbr_model_best_features.sav', 'rb'))

status_ratings_count = True
status_num_pages = True
status_text_reviews_count = True
status_language_code = True
status_published_date = True

print("---------------------------------------")
print("WELCOME TO BOOK'S RATING PREDICTOR APP")
print("---------------------------------------")

print("Welcome to book's rating predictor app.")
print("Please answer these questions to get your predictions of your book's average rating.")

print("\n")

while status_ratings_count == True:
    try:
        ratings_count = int(input("1.How many times do you want your books to be rated? "))
        status_ratings_count = False
        
        continue
    except ValueError as ve:
        print("Value must be numeric")

print("\n")
        
while status_num_pages == True:
    try:
        num_pages = int(input("2. How many pages does your book contain? "))
        status_num_pages = False
    except ValueError as ve:
        print("Value must be numeric")
        
print("\n")

while status_text_reviews_count == True:
    try:  
        text_reviews_count = int(input("3. How many times do you want your books to be reviewed? "))
        status_text_reviews_count = False
    except ValueError as ve:
        print("Value must be numeric")
        
print("\n")

while status_language_code == True:
    language_code_list = ['eng', 'fre', 'spa', 'mul', 'grc', 'enm', 'ger', 'jpn', 'ara',
                           'nl', 'zho', 'lat', 'por', 'srp', 'ita', 'rus', 'msa', 'glg',
                           'wel', 'swe', 'nor', 'tur', 'gla', 'ale']
    print(f"4. What is the language code of your book? The value must be in the: ")

    for index, code in enumerate(language_code_list):
        print(f"{index+1}. {code}")

    language_code = input("").lower().strip()

    if language_code not in language_code_list:
        print("The language code is not in the list")
    else:
        status_language_code = False

print("\n")   
        
while status_published_date == True:
    try:
        published_date = input("When was your book being published (YYYY-MM-DD)? ")
        published_date = datetime.strptime(published_date, "%Y-%m-%d")
        status_published_date = False
    except ValueError as ve:
        print("Wrong date format")
        
print("\n")

reference_date = datetime.strptime("2023-12-01", "%Y-%m-%d")
age_year = relativedelta(reference_date, published_date).years
age_month = (reference_date.year - published_date.year) * 12 + reference_date.month - published_date.month
age_day = (reference_date - published_date).days


data = pd.DataFrame(
    {
        'ratings_count' : [ratings_count],
        'num_pages' : [num_pages],
        'text_reviews_count' : [text_reviews_count],
        'language_code' : [language_code],
        'days_from_reference_date' : [age_day],
        'months_from_reference_date' : [age_month],
        'years_from_reference_date' : [age_year]
    }
)

print(f"Your predicted book's average rating is {model.predict(data)[0].round(2)} :)")