# Project Title - Book REVIEWS API

## description:
it's an fast API for managing books, book reviews, authors, and users.


## to run the app: 

## in Command Prompt  
1. python3 --version
2. pip3 --version
3. python3 get-pip.py

## In terminal
1. pip3 install numpy
2. pip install uvicorn
3. uvicorn app.main:app --reload
4. cd/your project path/> python -m uvicorn app.main:app --reload 

###### ENDPOINTS ######

BOOKS
# to get all books:
http://127.0.0.1:8000/api/book/ 

# to get a book with specific id: 1, 2, 3, 4, 5, 6
http://127.0.0.1:8000/api/book/5

# to get book_id and it's review
http://127.0.0.1:8000/api/book/2/review



AUTHORS
# all authors:
http://127.0.0.1:8000/api/author/

# to geta specific author by ID -  1, 2, 3, 4, 5, 6
http://127.0.0.1:8000/api/author/3


USERS

# to get an user with cpecific id - id's are 1, 7, 9, 14, 16, 17
http://127.0.0.1:8000/api/users/17

# To create an user you should go to database.py and create an new user there, for example: 
create_user('testnutzer9', 'testnutzer9@example.com', 'geheimesPasswort999')
# after creating an user you should comment it out.

# To get all users
http://127.0.0.1:8000/api/users/

# To delete the user / currently not working in my case
In PoweShell
cd 'C:\Users\ea\Desktop\Python.Oszimt\Book Reviews API'
curl.exe -X DELETE http://127.0.0.1:8000/api/users/1







REVIEWS

# To get all reviews
http://127.0.0.1:8000/api/review/

# to get specific review with an id. 1, 2, 3, 4, 5, 6
http://127.0.0.1:8000/api/review/1


GENRES

# To get all genres
http://127.0.0.1:8000/api/genre/

# to get specific genre with an id.
http://127.0.0.1:8000/api/genre/3






