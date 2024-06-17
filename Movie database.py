#module import section
import requests #this will send the http request to the server
from bs4 import BeautifulSoup #this will parse the data from the internet
import re  #this will find the pattern in the string
import mysql.connector as mysql #connects mysql to the python

#this function will input the movie data in the mysql
def mysql_connection(name, sno, year, table_name,rating):
    mycon = mysql.connect(host = "localhost", user = "root", password = "ansh@9013");
    cursor = mycon.cursor()
    cursor.execute("show databases;")
    databases = cursor.fetchall()
    database = 'movie'
    if (database,) in databases:
        cursor.execute('use movie;')
        cursor.execute('show tables;')
        data = cursor.fetchall()
        if (table_name,) in data:
            cursor.execute(f"insert into {table_name}(Sno, name, year,rating) values (%s, %s, %s, %s)", (int(sno.replace(',', '')), str(name), int(year), float(rating)))
            mycon.commit()
        else:
            cursor.execute(f'CREATE TABLE {table_name} (Sno BIGINT, name VARCHAR(1000), year BIGINT ,rating float);')


    else:
        cursor.execute('create database movie;')
        cursor.exectue('use movie;')
        cursor.execute(f'CREATE TABLE {table_name} (Sno BIGINT, name VARCHAR(1000), year BIGINT, rating float);')
        cursor.close()
        


#this fucntion will store the presonal data in the sql
def presonal_data():
    mycon = mysql.connect(host = "localhost", user = "root", password = "ansh@9013");
    cursor = mycon.cursor()
    cursor.execute('show databases;')
    data = cursor.fetchall()
    if ("user_info",) in data:
         cursor.execute("use user_info;")
         cursor.execute("create table Presonal_info(Name varchar(50), age int, nationality varchar(50), lang1 varchar(50), lang2 varchar(50), lang3 varchar(50), genre1 varchar(50), genre2 varchar(50), genre3 varchar(50))")
         Name = input("Enter your name here: ")
         print(" ")
         age = int(input("Enter your age here: "))
         print(" ")
         Nationality = input("Enter your country where you live: ")
         print(" ")
         print("Enter your three language you speak or understand :-")
         lang1 = input("Enter language 1: ")
         lang2 = input("Enter language 2: ")
         lang3 = input("Enter language 3: ")
         print(" ")
         print("Enter three movie genre you love to watch:- ")
         genre1 = input("Enter your genre1: ")
         genre2 = input("Enter your genre2: ")
         genre3 = input("Enter your genre3: ")
         cursor.execute(f"insert into Presonal_info(Name, age, nationality, lang1, lang2, lang3, genre1, genre2, genre3) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Name, age, Nationality, lang1, lang2, lang3, genre1, genre2, genre3))
         cursor.commit()

    else:
        print("False")


    
























#urls for movies

movie_dict = {
    'action': f'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,',
    'comedy': 'https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_5',
    'adventure': 'https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2',
    'animation': 'https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_3',
    'biography': 'https://www.imdb.com/search/title/?genres=biography&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_4',
    'crime': 'https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_6',
    'drama': 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7',
    'family': 'https://www.imdb.com/search/title/?genres=family&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_8',
    'fantasy':'https://www.imdb.com/search/title/?genres=fantasy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_9',
    'history':'https://www.imdb.com/search/title/?genres=history&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_11',
    'horror':'https://www.imdb.com/search/title/?genres=horror&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_12',
    'music':'https://www.imdb.com/search/title/?genres=music&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_13',
    'mystery':'https://www.imdb.com/search/title/?genres=mystery&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_15',
    'romantic':'https://www.imdb.com/search/title/?genres=romance&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16',
    'fiction':'https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17',
    'sports':'https://www.imdb.com/search/title/?genres=sport&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_18',
    'thriller':'https://www.imdb.com/search/title/?genres=thriller&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=JEKAM89W670EQQGFARDX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_19'

}
movie_genre_lst = ['action', 'comedy', 'adventure', 'animation', 'biography', 'crime', 'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery', 'romantic', 'fiction', 'sports', 'thriller']


#this fucntion will clear the list properly and sort there serial number and year of the release of the movie seperatly
def clear_list(lst):
    serial_no = lst.pop(0)
    year = lst.pop(-2)
    str = ' '.join(lst)
    return(str, year, serial_no)

#this function will get the all no. of the movies.
def getting_no_of_movies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(class_="desc")
    numbers = (content.text.split(" ")[2])
    return(int(numbers.replace(",", "")))

#this funciton will clean the data
def sorting_data(text):
    dict = {".":" ", "(":" ", ")":" "}
    for i,j in dict.items():
        text = text.replace(i, j)
    return(text.split(" "))


#this function will get the data from the web
def geting_data(url,start, j):
    # send a GET request to the website
    response = requests.get(url+f"desc&start={start}&ref_=adv_prv")

    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all the elements with a specific class
    content = soup.find_all(class_ = 'lister-item-header')#this is for the getting sno, name and year of the release of the movies.
    ratings = soup.find_all(class_ = 'ratings-imdb-rating') #this is for getting of the respective movies
    for i in range(len(ratings)):
        text = "".join(content[i].stripped_strings)
        rating_text = "".join(ratings[i].stripped_strings)
        print(rating_text)
        movie, year, sno = (clear_list(sorting_data(text)))
        mysql_connection(movie, sno, year, j, rating_text)
        


#this loop will intreate through every link and print all the movies of diffrent genre.
for i in movie_genre_lst:
    data = movie_dict[i]
    no_of_movies = getting_no_of_movies(data)
    for j in range (no_of_movies):
        if int(j) % 50 == 0:
            geting_data(data, j, i)
        
            

