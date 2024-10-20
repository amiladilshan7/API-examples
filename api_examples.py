# -*- coding: utf-8 -*-
"""API_Examples.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fdIzs2sySivp5qrUCAtl1yEUftZDBt6j

#  RandomUser API

To start using the API we can install the randomuser library running the pip install command.
"""

!pip install randomuser
!pip install pandas

"""Then, we will load the necessary libraries."""

from randomuser import RandomUser
import pandas as pd

"""First, we will create a random user object, r."""

r = RandomUser()

"""Then, using generate_users() function, we get a list of random 10 users."""

some_list = r.generate_users(10)
some_list

name = r.get_full_name()

"""Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users."""

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

## generate photos of the random 10 users.

for user in some_list:
    print (user.get_picture())

"""To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users."""

def get_users():
    users =[]

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})

    return pd.DataFrame(users)

get_users()

df1 = pd.DataFrame(get_users())  #we have a pandas dataframe that can be used for any testing purposes that the tester might have.

"""# Fruityvice API

We will start by importing all required libraries.
"""

import requests
import json

"""We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format."""

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

"""We will retrieve results using json.loads() function."""

results = json.loads(data.text)

"""We will convert our json data into pandas data frame."""

pd.DataFrame(results)

"""*The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.*"""

df2 = pd.json_normalize(results)
df2

"""Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry."""

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

"""Let's find out how many calories are contained in a banana."""

cal_banana = df2.loc[df2["name"] == 'Banana']
cal_banana.iloc[0]['nutritions.calories']

"""# Official Joke API
This API returns random jokes from a database. The following URL can be used to retrieve 10 random jokes.

https://official-joke-api.appspot.com/jokes/ten

Using requests.get("url") function, load the data from the URL.
"""

data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

"""Retrieve results using json.loads() function."""

results2 = json.loads(data2.text)

"""Convert json data into pandas data frame. Drop the type and id columns."""

df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
df3

