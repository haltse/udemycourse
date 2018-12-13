def header():
    print("*****" * 10)
    print("*****************  The movie place ***************")
    print("*****" * 10)


moviedb = [{'Movie Name': "Movie Name", 'release year': "release year", 'Director': "Director"},
           {'Movie Name': 'Bladerunner', 'release year': 1984, 'Director': 'Ridely Scott'},
           {'Movie Name': 'Ghostbusters', 'release year': 1984, 'Director': 'Ivan Reitman'},
           {'Movie Name': 'Star Wars', 'release year': 1977, 'Director': 'George Lucas'}]


def add_movie():
    name = input("We're adding a movie,  Let's start with the name")
    year = input("which year was it released?")
    direct = input("And who directed it?")
    moviedb.append({'Movie Name': name, 'release year': year, 'Director': direct})


def list_movies(woot):
    # allmovies =[items for items in moviedb]
    print(str({woot[0]['Movie Name']}), {woot[0]['release year']}, {woot[0]['Director']})
    for k in range(1, len(woot)):
        # print(woot[k].values())
        print(str({woot[k]['Movie Name']}), {woot[k]['release year']}, {woot[k]['Director']})


def search_movies():
    action = input("Would you like to find a movie by [t]itle, [y]ear released or by [d]irector?")
    if action.lower() == 't':
        search = input('What is the title?')
        for k in range(1, len(moviedb)):
            if moviedb[k]['Movie Name'] == str(search):
                print(
                    f" the title is {moviedb[k]['Movie Name']} which was released in {moviedb[k]['release year']} and was directed by {moviedb[k]['Director']}")
                continue
            else:
                print("I'm sorry I can't find that movie")
    elif action.lower() == 'y':
        search = input('What year was it released ?')
        for k in range(1, len(moviedb)):
            if moviedb[k]['release year'] == search.strip():
                print(
                    f" the title is {moviedb[k]['Movie Name']} which was released in {moviedb[k]['release year']} and was directed by {moviedb[k]['Director']}")
                continue
            else:
                print("I'm sorry I can't find that movie")
        pass
    elif action.lower() == 'd':
        pass

def return_matches(search_term,search_type):
    pass



header()
action = ''
while action.lower() != 'x':
    action = input(
        "Would you like to [a]dd a movie,[l]ist all movies in the library,[s]earch for movies or E[x]it the app?")
    if action.lower() == 'a':
        add_movie()
    elif action.lower() == 'l':
        list_movies(moviedb)
    elif action.lower() == 's':
        search_movies()
