import wikipedia
user_input = input("Enter a word or phrase to search: ")
while user_input != '':
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print(f"Title  : {page.title}")
        print(f"Summary: {page.summary}")
        print(f"Url    : {page.url}")
        user_input = input("Enter a word or phrase to search: ")
    except wikipedia.PageError:
        print(f"{user_input} result not found. Please try again")
        user_input = input("Enter a word or phrase to search: ")
print("Thank you and see you next time")