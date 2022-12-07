# Web scraper to get answers to stack overflow questions from the terminal

import sys
import urllib3
import requests
from bs4 import BeautifulSoup
import pyfiglet

# disable SSL error output
urllib3.disable_warnings()

def main():
    # filter user input for desired search and site
    query, site = filter_query()

    # google based on user query
    google = google_stack(query, site)

    # pull data from stack overflow based on google results
    title, question, best_answer = search_stack(google)

    # formatted stack overflow title output
    print("\n", end="")
    print(pyfiglet.figlet_format("Title...", font = "small", width = 200), end="")
    print("-" * 25, end="\n\n")

    print(title)
    print("\n", end="")

    # formatted stack overflow question output
    print(pyfiglet.figlet_format("Question...", font = "small", width = 200), end="")
    print("-" * 40, end="\n\n")

    print(question.get_text().strip())

    # formatted stack overflow best answer output
    print("\n", end="")
    print(pyfiglet.figlet_format("Best Answer...", font = "small", width = 200), end="")
    print("-" * 53, end="\n\n")

    print(best_answer.get_text().strip())
    print("\n", end="")

# check user input to determine search strategy
def filter_query():
    if len(sys.argv) == 2:
        query = str(sys.argv[1])
        site = "stackoverflow.com"
    elif len(sys.argv) == 1:
        query = (input("What is your query? "))

        print(
        '''
        1. https://stackoverflow.com/ - Q&A for professional and enthusiast programmers
        2. https://serverfault.com/ - Q&A for system and network administrators
        3. https://superuser.com/ - Q&A for computer enthusiasts and power users
        4. https://askubuntu.com/ - Q&A for Ubuntu users and developers
        5. https://unix.stackexchange.com/ - Q&A for users of Linux, FreeBSD and other Un*x-like operating systems
        6. https://codereview.stackexchange.com/ - Q&A for peer programmer code reviews
        7. https://webapps.stackexchange.com/ - Q&A for power users of web applications
        8. https://sqa.stackexchange.com/ - Q&A for software quality control experts, automation engineers, and software testers
        9. https://security.stackexchange.com/ - Q&A for information security professionals
        '''
        )
        
        choice = input("Which site would you like to search? (1-9) ")

        if choice == "1" or choice == "1.":
            site = "stackoverflow.com"
        elif choice == "2" or choice == "2.":
            site = "serverfault.com"
        elif choice == "3" or choice == "3.":
            site = "superuser.com"
        elif choice == "4" or choice == "4.":
            site = "askubuntu.com"
        elif choice == "5" or choice == "5.":
            site = "unix.stackexchange.com"
        elif choice == "6" or choice == "6.":
            site = "codereview.stackexchange.com"
        elif choice == "7" or choice == "7.":
            site = "webapps.stackexchange.com"
        elif choice == "8" or choice == "8.":
            site = "sqa.stackexchange.com"
        elif choice == "9" or choice == "9.":
            site = "security.stackexchange.com"
        else:
            print("\nInvalid entry - Defaulting to https://stackoverflow.com/")
            site = "stackoverflow.com"
    else:
        print("Invalid usage")
        sys.exit()
    
    return query, site

# google search based on user query - search isolated to stack exchange site results
def google_stack(g, s):
    # isolate google search to the provided site variable
    url = (f"https://google.com/search?q=site%3A{s}+") + g

    # assign site data to variable
    google_so = requests.get(url, verify=False)

    # html parse with beautiful soup and assign to a variable
    soup = BeautifulSoup(google_so.content, "html.parser")
    
    # extract all a href url's from the soup data and append to a list
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    # pull url at position 15 in the list and strip off irrelevant text
    return urls[15].strip("/url?q=")

# scrape data from stack site
def search_stack(q):
    # get the page html data and pass to beautiful soup
    page = requests.get(q, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")

    # drop irrelevant header content in question section
    select = soup.find_all("aside")
    for s in select:
        s.decompose()

    # filter page title and filter out irrelevant text
    title = soup.find(class_="question-hyperlink")
    strtitle = str(title.string)
    # if [duplicate] exists in the title, remove it
    if "[duplicate]" in strtitle:
        title = strtitle.replace("[duplicate]", "")
    # if [closed] exists in the title, remove it
    elif "[closed]" in strtitle:
        title = strtitle.replace("[closed]", "")

    # filter page question
    question = soup.find(class_="s-prose js-post-body")

    # filter best answer - exit if no results found
    try:
        filter_answers = soup.find(class_="answer js-answer accepted-answer js-accepted-answer")
        if filter_answers == None:
            filter_answers = soup.find(class_="answer js-answer")
        best_answer = filter_answers.find(class_="s-prose js-post-body")
    except AttributeError:
        print("Query returned no valid results")
        sys.exit()

    # return results
    return title, question, best_answer

if __name__ == "__main__":
    main()
