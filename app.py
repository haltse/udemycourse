def header():
    print("*****" * 10)
    print("*****************  The movie place ***************")
    print("*****" * 10)


moviedb = [{'Movie Name': "", 'release year': "", 'Director': ""},
           {'Movie Name': 'Bladerunner', 'release year': 1984, 'Director': 'Ridely Scott'},
           {'Movie Name': 'Star Wars', 'release year': 1977, 'Director': 'George Lucas'}]


def add_movie():
    name = input("We're adding a movie,  Let's start with the name")
    year = input("which year was it released?")
    direct = input("And who directed it?")
    moviedb.append({'Movie Name': name, 'release year': year, 'Director': direct})


def list_movies():
    # allmovies =[items for items in moviedb]
    for k in range(0, len(moviedb)):
        print(item for item in moviedb[k].items())



def search_movies():
    pass


header()
action = ''
while action.lower() != 'x':
    action = input(
        "Would you like to [a]dd a movie,[l]ist all movies in the library,[s]earch for movies or E[x]it the app?")
    if action.lower() == 'a':
        add_movie()
    elif action.lower() == 'l':
        list_movies()
    elif action.lower() == 's':
        pass
