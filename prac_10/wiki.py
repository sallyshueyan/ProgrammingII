import wikipedia
user_input = input("Enter a word or phrase to search: ")

page = wikipedia.page(user_input, auto_suggest=False)
print(f"Title  : {page.title}")
print(f"Summary: {page.summary}")
print(f"Url    : {page.url}")
user_input = input("Enter a word or phrase to search: ")