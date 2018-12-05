def header():
    print("*****" * 10)
    print("*****************  The movie place ***************")
    print("*****" * 10)


moviedb = [{'Movie Name': 'Bladerunner', 'release year': 1984, 'Director': 'Ridely Scott'},
           {'Movie Name': 'Star Wars', 'release year': 1977, 'Director': 'George Lucas'}]


def add_movie():
    input("We're adding a movie,  Let's start with the name")
    pass


def list_movies():
    pass


def search_movies():
    pass


header()
action = ''
while action.lower() != 'x':
    action = input(
        "Would you like to [a]dd a movie,[l]ist all movies in the library,[s]earch for movies or E[x]it the app?")
    if action.lower() == 'a':
        pass
    elif action.lower() == 'l':
        pass
    elif action.lower() == 's':
        pass
