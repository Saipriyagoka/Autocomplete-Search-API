import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , "Mve_Project.settings")

import django
django.setup()

#fake pop script

from basic_app.models import Movie_detail
import pandas as pd
def populate():
    df_movie_detail = pd.read_csv(r"C:\Users\saipriya\Downloads\movies.tsv")
    for index,row in df_movie_detail.iterrows():
        movie_title = row['title_Name']
        movie_titleid = row['tconst']
        movie_rating=row['rating']
        movie_cast = row['cast']
        Movie_detail.objects.get_or_create(name = movie_title , titleid = movie_titleid , rating = movie_rating , cast = movie_cast)[0]

if __name__ == "__main__":
    print('populating script')
    populate()
    print('populating completed')
