# Coffee Shop Full Stack

### AUTH0 Account

```Python3
AUTH0_DOMAIN = 'franknguyenvd.au.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'localhost:5000'
```

### Manager Account
```Python3
Username = manager@udacity.com
Password = @Udacity1
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5oeWxCOTlDSndqcGh6c294ZEFNSSJ9.eyJpc3MiOiJodHRwczovL2ZyYW5rbmd1eWVudmQuYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYTI2NjhjZWY0ODIyMDA3MDBjOTA1ZCIsImF1ZCI6ImxvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjIxMjU2MzExLCJleHAiOjE2MjEzNDI3MTEsImF6cCI6Im5EeWRiQ2FSYk5BdWx0aUJMejVwOUp4REdSU3hoWUlIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.QZWkRIRa8sx0bbDhP7G0Lj7vqfPjmiXCrTeJw2ncOQPLKQJmWYLKeOBonVL6UinLSLGb5fuR998GJGMsCiUdUBgQcWf7LXcI3KgQflhQzKeCVGfrmw4X_BWCr-bU9UHQ2FVa03i_g9nMEOqalrUrKPeIugLwElxnA9oj5K02WvSzmFO2YeCvTYmH7ssBjdOTlIweVC69R-xlGB7jg5ww8LMQ1IZv-HXwdsCgiKYXkA_ur0Q72AIHDTQDQ6xIs0ptKZ0hMq0ypr893hse57w4MCgtU7vG4jg2Gtj4HzEvLaryreQSUKPnurox7XdD6V1Pya9VrCS-oOdQ466GASS4SA'
```

### Barista Account
```Python3
Username = barista@udacity.com
Password = @Udacity1
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5oeWxCOTlDSndqcGh6c294ZEFNSSJ9.eyJpc3MiOiJodHRwczovL2ZyYW5rbmd1eWVudmQuYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYTI2NjI3M2VjOWRmMDA2OWEwNjJhNyIsImF1ZCI6ImxvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjIxMjU2MTQzLCJleHAiOjE2MjEzNDI1NDMsImF6cCI6Im5EeWRiQ2FSYk5BdWx0aUJMejVwOUp4REdSU3hoWUlIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.zUtD0PQjLwM_k7mDLiR833rKf4rPi1e8gF385Y_YEXabk_vuUGkldMcJmLaNlOTVLmiqt99y5-gMV2tA0GpkJhjxn-EUJ1lN3CfLzMa9EXgKTIQsvyMr7NLhbRGTu4dCAAp7ddSxRYBQ-Op5Uh9XUdDltlCuB_K91w8OoBjgW3q1fCiY4085qC-iNQEG3fgO2V1b5Hq9w7gylUYW08L_4WuWW_tGkND7IWQWnYZ6vh5eSE7WHi_XyYBQsiyYcQIkbnZwYi3f0q0QHZzroCfWRDeaqlyi7SpFtsArMUD8rViu9n10qV-EySgc5qSuqgGFuIUpcOYVNU-Xpy4B9wNm0w'
```

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)
