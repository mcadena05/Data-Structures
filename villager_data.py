"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file_info = open(filename)
    species = set()

    for line in file_info:
        file_info = line.rstrip()
        word = file_info.split('|')     
        species.add(word[1])
        
    return species



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    file_info = open(filename)
    villagers = []

    for line in file_info:
        file_info = line.rstrip()
        word = file_info.split('|')     
        species = word[1]
        if species == search_string:
            villagers.append(word[0])          
    
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    file_info = open(filename)
    # return_list = [
    #     sorted(fitness = []), sorted(nature = []), sorted(fashion = []), sorted(education = []), sorted(play = []), sorted(music = [])
    # ]
    fitness= []
    fashion = []
    nature= [] 
    education = []
    play = []
    music = []
    
    return_list = [fitness, fashion, nature, education, play, music]
    
    for line in file_info:
        file_info = line.rstrip()
        word = file_info.split('|')     
        hobbies = word[3]
        if hobbies == "Fitness":
            fitness.append(word[0])
            return sorted(fitness)
        elif hobbies == 'Fashion':
            fashion.append(word[0])
        elif hobbies == 'Nature':
            nature.append(word[0])
        elif hobbies == 'Education':
            education.append(word[0])
        elif hobbies == 'Play':
            play.append(word[0])
        elif hobbies == 'Music':
            music.append(word[0])
    
    print(sorted(return_list))

all_names_by_hobby("villagers.csv")

# def all_data(filename):
#     """Return all the data in a file.

#     Each line in the file is a tuple of (name, species, personality, hobby,
#     saying).

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[tuple[str]]: a list of tuples containing strings
#     """

#     all_data = []

#     # TODO: replace this with your code

#     return all_data


# def find_motto(filename, villager_name):
#     """Return the villager's motto.

#     Return None if you're not able to find a villager with the
#     given name.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name

#     Return:
#         - str: the villager's motto or None
#     """

#     # TODO: replace this with your code


# def find_likeminded_villagers(filename, villager_name):
#     """Return a set of villagers with the same personality as the given villager.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name
    
#     Return:
#         - set[str]: a set of names

#     For example:
#         >>> find_likeminded_villagers('villagers.csv', 'Wendy')
#         {'Bella', ..., 'Carmen'}
#     """

#     # TODO: replace this with your code
