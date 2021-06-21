import re
import pytest

class Movies:
    """
    Analyzing data from movies.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path = path_to_the_file
        with open(self.path, 'r') as f:
            self.data = f.read().split('\n')
            del (self.data[0])
        self.movies = self.parse_movies()

    def parse_movies(self):
        d = {}
        for item in self.data:
            try:
                split_left = item.split(',', maxsplit=1)
                if split_left:
                    id = split_left[0]
                    title, genres = split_left[1].rsplit(',', maxsplit=1)
                    genres = genres.split('|')
                    year = re.search(r"\((\d{4})\)", title)
                    if year:
                        year = year.groups()
                        year = int(year[0] if year.__len__() > 0 else 0)
                    else:
                        year = 0
                    title = re.search(r'(.*?)(?:\s+\(\d{4}\))', title)
                    if title:
                        title = title.groups()
                        title = title[0] if title.__len__() > 0 else None
                    d[id] = {'title': title,
                             'year': year,
                             'genres': genres}
            except:
                pass
        return d

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts.
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        release_years = {}
        for k, v in self.movies.items():
           release_years[v['year']] = release_years.get(v['year'], 0) + 1
        release_years = dict(sorted(release_years.items(), key=lambda item: item[1], reverse=True))
        return release_years

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        genres = {}
        for k, v in self.movies.items():
            for genre in v['genres']:
                genres[genre] = genres.get(genre, 0) + 1
        genres = dict(sorted(genres.items(), key=lambda item: item[1], reverse=True))
        return genres

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movies = {}
        for k, v in self.movies.items():
            movies[v['title']] = v['genres'].__len__()
        movies = dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))
        movies = dict(list(movies.items())[:n])
        return movies


class Ratings:
    """
    Analyzing data from ratings.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path = path_to_the_file
        with open(self.path, 'r') as f:
            self.data = f.read().split('\n')
            del (self.data[0])
        self.ratings = self.parse()

    def parse(self):
        d = {}
        for item in self.data:
            try:
                split_left = item.split(',', maxsplit=1)
                if split_left:
                    id = split_left[0]
                    title, genres = split_left[1].rsplit(',', maxsplit=1)
                    genres = genres.split('|')
                    year = re.search(r"\((\d{4})\)", title)
                    if year:
                        year = year.groups()
                        year = int(year[0] if year.__len__() > 0 else 0)
                    else:
                        year = 0
                    title = re.search(r'(.*?)(?:\s+\(\d{4}\))', title)
                    if title:
                        title = title.groups()
                        title = title[0] if title.__len__() > 0 else None
                    d[id] = {'title': title,
                             'year': year,
                             'genres': genres}
            except:
                pass
        return d

    class Movies:
        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts.
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            return ratings_by_year

        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            return ratings_distribution

        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings.
            It is a dict where the keys are movie titles and the values are numbers.
     Sort it by numbers descendingly.
            """
            return top_movies

        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            return top_movies

        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            return top_movies

    class Users:
        """
        In this class, three methods should work.
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """


class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path = path_to_the_file
        with open(self.path, 'r') as f:
            self.data = f.read().split('\n')
            del (self.data[0])
        self.tags = self.parse()

    def parse(self):
        return [i.split(',') for i in self.data]

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        d = {}
        for i in self.tags:
            try:
                d[i[2]] = d.get(i[2], 0) + 1
            except:
                pass
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        big_tags = dict(list(d.items())[:n])
        return big_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        return big_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        return big_tags

    def most_popular(self, n):
        """
        The method returns the most popular tags.
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        return popular_tags

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        return tags_with_word


class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """

    def get_imdb(list_of_movies, list_of_fields):
        """
The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
     Sort it by movieId descendingly.
        """
        return imdb_info

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        return directors

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        return budgets

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        return profits

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
     Sort it by runtime descendingly.
        """
        return runtimes

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
     The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        return costs

class Test:

    def test_movies(self):
        movies = Movies('movies.csv')
        assert type(movies.dist_by_release()) == dict
        assert list(movies.dist_by_release().values()) == list(sorted(movies.dist_by_release().values(), reverse=True))
        assert type(movies.dist_by_genres()) == dict
        assert list(movies.dist_by_genres().values()) == list(sorted(movies.dist_by_genres().values(), reverse=True))
        assert type(movies.most_genres(3)) == dict
        assert list(movies.most_genres(3).values()) == list(sorted(movies.most_genres(3).values(), reverse=True))

    def test_tags(self):
        tags = Tags('tags.csv')
        assert type(tags.most_words(10)) == dict
        assert list(tags.most_words(10).values()) == list(sorted(tags.most_words(10).values(), reverse=True))

if __name__ == '__main__':
    movies = Movies('movies.csv')
    print(movies.dist_by_release())
    print(movies.dist_by_genres())
    print(movies.most_genres(3))
    ratings = Ratings('ratings.csv')
    links = Links('links.csv')
    tags = Tags('tags.csv')
    print(tags.most_words(5))
