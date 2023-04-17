#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:47:47 2023

@author: laura
"""

# PPHA 30535
# Spring 2023
# Homework 3

# Manyu Luo

# Manyul2
# Manyul2

# Due date: Sunday April 16th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/rating/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, rating, num_stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category = None):
        if category is not None:
            movie_list = [i for i in self.titles if self.movies[i]['category'] == category]
            if len(movie_list) == 0:
                print(f"There's no movie in {category} category.")
                return
            else:
                choice = random.choice(movie_list)
        else:
            choice = random.choice(self.titles)
        movie = self.movies[choice]
        print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")


movies = MovieDataBase()
movies.add_movie('manyu', 1999, 'action', 4, 5)
movies.what_to_watch('comedy')



# **b) The what_to_watch method currently raises a ValueError if you use it
# before entering an movies. Modify it using try/except so that it tells
# the user what they did wrong instead of raising an error.**



class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, rating, num_stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category = None):
        try:
            if category is not None:
                movie_list = [i for i in self.titles if self.movies[i]['category'] == category]
                if len(movie_list) == 0:
                    print(f"There's no movie in {category} category.")
                    return
                else:
                    choice = random.choice(movie_list)
            else:
                choice = random.choice(self.titles)
            movie = self.movies[choice]
            print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")
        except ValueError:
            print("There's no movie in the database.")



lis = MovieDataBase()
lis.add_movie('fast', 2000, 'action', 4.2, 4)
lis.add_movie('furious', 2001, 'comedy', 4.8, 5)
lis.add_movie('cool', 1998, 'action', 4.7, 5)
lis.add_movie('guy', 1965, 'action', 4.8, 5)
lis.what_to_watch('horror')
lis1 = MovieDataBase()
lis1.what_to_watch()

#SOurce:https://www.w3schools.com/python/python_try_except.asp
# c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.


class InteractiveMovieDataBase(MovieDataBase):
    pass

lis2 = InteractiveMovieDataBase()
lis2.what_to_watch()
lis2.add_movie('fast', 2000, 'action', 4.2, 4)
lis2.add_movie('furious', 2001, 'comedy', 4.8, 5)
lis2.add_movie('cool', 1998, 'action', 4.7, 5)
lis2.add_movie('guy', 1965, 'action', 4.8, 5)
lis2.what_to_watch()


# d) Override the add_movie method in your new class so that if it is called
# without arguments, it instead asks for user input to add a title/year/
# category/rating/stars, but if it is called with arguments it behaves as before

class InteractiveMovieDataBase(MovieDataBase):
    def add_movie(self, title=None, year=None, category=None, rating=None, num_stars=None):
        if title is not None and year is not None and category is not None and rating is not None and num_stars is not None:
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
            print(f'{title} ({year}) added to the database.')
        else:
            title = input("Enter the title of the movie: ")
            year = input("Enter the year of the movie: ")
            category = input("Enter the category of the movie: ")
            rating = input("Enter the rating of the movie: ")
            num_stars = input("Enter the number of stars the movie received: ")
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
            print(f'{title} ({year}) added to the database.')    



lis2 = InteractiveMovieDataBase()
lis2.add_movie('fast', 2000, 'action', 4.2, 4)
lis2.add_movie('furious', 2001, 'comedy', 4.8, 5)
lis2.add_movie('cool', 1998, 'action', 4.7, 5)
lis2.add_movie('guy', 1965, 4.8, 5)
lis2.add_movie()
#https://stackoverflow.com/questions/70910500/how-to-make-an-attribute-a-list-to-contain-multiple-items

# e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
# input, so that they can't enter something that makes no sense (e.g. title=None
# or year='dog')


import numbers                            
class InteractiveMovieDataBase(MovieDataBase):
    def add_movie(self, title=None, year=None, category=None, rating=None, num_stars=None):
        if isinstance(title, str) and isinstance(year, int)  and len(str(year)) == 4 \
            and isinstance(category, str) and isinstance(rating, numbers.Number) \
                and (rating >=0  and rating <= 5)and isinstance(num_stars, numbers.Number) \
                    and (num_stars >=0 and num_stars <= 5):
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
            print(f'{title} ({year}) added to the database.')
        elif not isinstance(title, str):
            print('Title should be strings.')
        elif not isinstance(year, int):
            print('Year should be integers.')
        elif len(str(year)) != 4:
            print('Enter a valid year.')
        elif not isinstance(category, str):
            print('Category should be strings.')
        elif not isinstance(rating, numbers.Number):
            print('Rating should be integers or floats.')
        elif rating < 0 or rating > 5:
            print('Enter a valid rating.')
        elif not isinstance(num_stars, numbers.Number):
            print('Number of stars should be integers or floats.')
        elif rating < 0 or rating > 5:
            print('Enter a valid star rating.')
        else:
            title = input("Enter the title of the movie: ")
            year = input("Enter the year the movie was released: ")
            category = input("Enter the category of the movie: ")
            rating = input("Enter the rating of the movie: ")
            num_stars = input("Enter the number of stars the movie received: ")
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
            print(f'{title} ({year}) added to the database.')   
#source:https://docs.python.org/3/library/numbers.html
#source: https://www.w3schools.com/python/ref_func_isinstance.asp

tes = InteractiveMovieDataBase()
tes.add_movie(title = 123, year = 1999, category = 'horror', rating = 4, num_stars = 5)


# f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
# returns a list of all the titles in the database currently, ordered
# highest ranking (by stars) to lowest

class InteractiveMovieDataBase(InteractiveMovieDataBase):
    def movie_rankings(self):
        rank = [(i, self.movies[i]['stars']) for i in self.movies]
        rank = sorted(rank, key = lambda i : i[1], reverse = True)  # cite: to sort based on the second element of tuple
        print(rank)
#source:https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
#https://www.w3schools.com/python/ref_list_sort.asp


lis4 = InteractiveMovieDataBase()
lis4.add_movie('fast', 2000, 'action', 4.2, 2)
lis4.add_movie('furious', 2001, 'comedy', 4.8, 3)
lis4.add_movie('cool', 1998, 'action', 4.7, 4)
lis4.add_movie('guy', 1965, 'action', 4.8, 5)
#lis2.add_movie()
lis4.movie_rankings()


