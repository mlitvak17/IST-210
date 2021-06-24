# -*- coding: utf-8 -*-
"""Final Group 21 Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JARDVlXr_p0L87585rPfs4Cb6wc1Zhpo

Group 21 Final Project: Highway Roasted Peanut Stand
By:


*   Mauricio Litvak
*   Casey Brennan
*   Scott Morelli
*   Conor Whitlark

Intro: Our group, group 21 originally decided to do our project on something that was unique. We wanted to make sure that no other group could possibly have the same idea. After some discussion we came up with the ingenious idea of roasted peanuts along the highway for maximum traffic. Our group designed our project from a business perspective keeping in mind all the important attributes about running a business. We began by picking key entities related to our business such as location, peanuts, employees. We then came up with attributes relating to each entity and created our diagram. We came to our final ER Diagram through trial and error and finalizing our best business model.

[Vid](https://www.youtube.com/watch?v=U219M_cCDoU)

![alt text](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Group%202%20Assignment.drawio#R7V1dd5u4Fv01XmvuQ7P4MP54jO0k7dTt5Ma5vcm8dClGtrnFiGJ5HPfXX4FRDEgmJBYgzWimqzUC5IPO1uawdTju2OP1800EwtUX5EK%2FYxnuc8eedCxrOBiQv%2BOG%2FaGhb5iHhmXkuYemTMPM%2BwXTRiNt3Xou3OQOxAj52AvzjXMUBHCOc20gitAuf9gC%2BflvDcESMg2zOfDZ1v96Ll4dWgeOcWz%2FCL3lin6zaaR71oAenDZsVsBFu0yTfdWxxxFC%2BPBp%2FTyGfjx2dFwO512f2PtiWAQDXOWEq9F0And3fz6Yy2AJR8HjCk8%2BpL38BfxtesFTNAfYQ0FqNN7TkdjsvLUPArI1WqAAz9I9BtmerzzfnYI92saWbDCY%2F6BboxWKvF%2FkeOCTXSZpILsjnDra6sW9eb4%2FRj6Kku%2BxoRH%2FnztzFveYflcEN%2BTcW3rZZqHpC3jOHTgFG0ytRL4Pwo33lNgdn7gG0dILRghjtE4Pold5nTdqkfxH9gPfWwakbU6%2BC0Z0LA5XY3bJNusWOsYwwvA505S66QaiNcTRnhyS7rXtFDJ7OheGh%2B3dEYFmLz1mlUVft5siP0X98qXvIzDIhxQbb8CJVYIT49J1yWBvWMSsQBh%2FJIOBPeDfkfkJgmW8d4RRmA64DxfUQVF6JfHnJ%2BoUMzPoh2NH8Uh6ZIpeps1rz3WTXrNIClAC1U0I5l6wnB6%2Bxe4em%2B7Sb4ubEOly4Sezc0U6g0FsDcIAg6cXkIfIC3Ayrs6I%2FCHDPzYunI5DrnRMts3jNvkTHx7hMQo2OAJeggRIkLiDMRpHboTCe4I9SK82O6GcAqgsLqhKZ%2FPrSEuRReZfJWBRQArHlc3g6vbz2Th6yk5oDiaqwimPHWHQeQ0d8WWmwH8nDqwTOHi5Taa25e5EOXxkAGE3iYcug4f7CCwW3rwecjFeR0PSmeLM0gCTOBWZhDKOcOQ4DHLa5pEDcpQlke4JCAgjkdqg0GOgMAshdEnT1Ft7WFOJ3FQysFqmkr6mErFU0jsBAfmpZMBA4ZtHniA938N7zSNy84hpDFomkqEmErFEMjiBAfmJhOqZIrGg%2BaNe%2FrC71fjDrOtp2GTlWU0gZxHIyzSsjUFEgOH%2B9%2B9wc3n9a2t83z0%2FfQv32%2B6%2FOVL9dbSHEUd21UJ9pxmh3szr9I5VlTBE6PRckLA6%2FdXPrReuyTV%2BmtRzw9ECPRdMpXNYSoGea7EW6M%2B8DZVOU6kFeq7lrEA%2FRhstqdUWyoqhkSbVea7FWp0XzCBKqPNcyznqfHz5mkGkZpAmRXmuxVqUF8wgSojyXMtZUX7qLQiDGLMQcPLWNJHIRCSNqvJck7UqL5hJlFDl%2BejVqrxy%2FNGkKs83WavygglEZVWeo7iuQx%2FtIdTKfHvKfG%2BQl%2BZtyhDtSfMmK6VSpGhpXgJp%2FpQmK682b7JirBbnBdyN7BNIkF%2BdN1md9StYa3Gt4Zj2zVTSuj5vsqps20SiekzrnACBAk%2FFrNZ6u4p9pmlEbhppXaQ3WWlW08h5NNI%2FAQIFaIQVWn9HT6Th3sO%2BJhPZyaR9od6qQZ39h7PJ8AQK5GcTqwbVVVNIzRTSulZPQaIpRFjq4iktViqtfvJwNf2%2BnX56ND95Qd8K%2Bzfbz5wM%2BvF2Q1wJIxYTWqnvtKPUV0%2Bi79eFE5YzKE60UN%2BoUF86i6XU6bkW6xz6M29EpbNUapWeazm7bHMDA5d3F9LxrJh4VgyRNKnScy3WWfSCOUSJLHqu5ex6zf0%2BjHNg0YL89Q2uvLnW2GQnlCb1eq7FOqleMKEokVTPtZxdubkGa8%2Ff%2F%2FZIuvv6L00lclNJo2o912SdVi%2BYS5RIq%2Bejl124uVzqaER2Cqmq1tu14UZn1gvmkPoz6%2BsDAyvDzoirXRYRWqvvNKPVFwvTd82KishLo3iUsOJqghKt1Eug1L95wbh1qV6n1NdzG1IipZ5vOiu6Hryno9lGo9k3c0nrar3OqRdOI0rk1PNNZ6VWXfZGARZpXaLXKfXCWUSJlHq%2B6azIelj20ywiNYu0r87rXHrhNKJELj0fDKzOGtPIH4uvW13KU3ouqSrT1wcfVpm9bl0kUZxN6k%2Brrw8OrAT7EeFbH2BdAkee4vTNVsDhA4UVV3V1eon0euuUSiuvXm%2Bx6qzW6wXcjWpPjK0PEazqqivUNx7Wvp1KWpfrLZ0MK5pF1M2GtVjVVcv1CrBI63K9pdNgRbOIunmwNiu66kr16pBJ%2B6q9rRNiBbPJy5RUkE1Y2VVTiOwU0mQFHD5qWHVWU8h5FHJqyUb%2BCjh2hWQS6C4hFRPJQHh4fwd9gD0UXB33MGO3wmsqzcPAvYyixGdXd2sQuH8cmCFW7Hk74LOHH%2Bi55PNj7NcLJ92aUCU%2B2djTjYAMx0N2I3NWvHk8Ldmi57EuTj23QdtoDsvmfkrrmPLIqQNprms8jqUUkaUEg4uCtDFKxv8vmDOYh430O27jCXFcCOjlFwJMwyrA63Dt6VlHhDEdmYWehsWODmPDdJRA9eXC34%2FeLktl%2F9lw1pjIrMR5SCarOKWUwazInBR1ffAE%2FRGY%2F1hGaBu4vOWdqkRy%2FpNNepZxYfSGZs459P2v94KHHoIWiw2sx52sdv9bfFcnTT2DfeH4n%2BfVD4TPujTmoG61pXcrK8BTt1rarclkdQamal61K%2BhaOnIo%2B6nW1wOHoWSBg2Xl7%2FcDq5AZUDVwsKmGl3bUc6xmAwc28UDtwOH81MPjLcYwbOUiB3ap7m9xixHmVuOib9JBol61pPcq%2B3CqvVqYrD2Hcpkyk5VyfXORAwrgPfoCgj0bO2R3vSd6qBQFXI2mE7i7%2B%2FPBXAZLOAoeV3hCq7lIc3O3jfzN3SqW033vzb1L9bGGbu4OqwpM0Rxg6CpLGS9TRoQwYFp5xpCfMCq8N9sOYbzz0aE2oinVH7PPG6W%2FcycNJTndPCX1jEIXVSmpV%2BjIKXZUNyVxXvbFYLGIKckY7dXlpfMTujLPHV0qqatCTD12NZ4GqLa68alQpzrWQLG7TY8NT%2F8OKrQ4rxoX3T4NSCR2Y4VlbrFBwy8YoUxo4Mbv%2BnQyLyedPFKJIGLIBhFlVfiliSG6TkGzpFfy1hjCKXTUL3ZUcwzRYzXL2QqFm9gC9m0GVWipd34hqOyTzUB6WuKscRqHu4uZZDQZCt9jRDrTcay8Xil%2F4MA%2BphpUrdQuTYLB4cBWzKe8d4B6Pk7DgpxPez%2B3iO74sEkChsvY%2Bd3w%2BbiTfFrG%2F17dkV0TDywjsKY9EgsPnR4OqYCZDY7QD1hItivJv3sdObuVh%2BEsBEkwsItAnJiXYAi6r8UQ1d9EtmjdLio1sm8i20NOTCCiaOinnz8%2FLic3nz9Puvd9p%2F%2FwcfDB5RUNnceviHsBuyaYDRpRhFdoiQLgZwPG%2FHgdj5miJHcydtz%2FIMb7NKgEW4wKYWUa2h3DucdsNFe%2BjG2%2BLYwskbeSXWkUa5RJZMdgt3KQyXdD1RjTrBhkHqnHtMwzYwMaTxZeo%2B8VczNPhIE1sRZ%2FHJXPuCmfpSKWQ4c0Efu9eKA5j%2FkTanSq8mvcNTuVzPKBU1jbkEmmKKO8bLkCCIIt1oVS5Klq3qdFoBuplMKFCatJ1lyfS5dJeQOFVQZYC1VSuBbrHyA98z2g0kkqdY0UruVsotVXsNbFDWp7mVAMjTRZIYVrsS5tIJhBlKhswLWcXZzQRZbkZ5Amq6NwLdY%2FYCyYQZT4AWOu5axmNQN%2BXBrlNvLmOhaRnEkaLY3CNVlXaxNMJUoUa%2BOjt4ba9po%2F6uWPJuui8E3WpZUEE0j9vzX6DjCQzQjFS%2FFHFT8C4eoLcmF8xP8B)

Specifics into ER diagram : Our ER diagram was designed in a way to have the stand at the center of focus. We wanted all the other tables to connect to one central location, being the Stand. All of the tables had in common the relationship to the stand so it worked out well. We also wanted to have 2 groups of related data off to the sides. We included the equipment in one group, being the fryer and hotplate. We included customers and employees in the other group being our people area. Specifically for customer we included some unique attributes such as gender, type of vehicle, age, family or no family. We did this in order to collect data relating to our marketing strategy in the future. Analyzing this data could prove useful in figuring out which customer stops for peanuts the most.

Discuss how you created your database, tables, and inserted data: The database was created to follow the proper ER diagram afromentioned. It uses a central table entitled "Stand" which has 6 sub tables directly connected to it through cardinality. Each table was created using "create table" and data and constraints were added using attributes in the create section of the sql code. Then data was inserted using "insert" sql commands. This was done for each table and foreign keys were used to connect each table to the central table "stand".

Specifics into ER diagram : Our ER diagram was designed in a way to have the stand at the center of focus. We wanted all the other tables to connect to one central location, being the Stand. All of the tables had in common the relationship to the stand so it worked out well. We also wanted to have 2 groups of related data off to the sides. We included the equipment in one group, being the fryer and hotplate. We included customers and employees in the other group being our people area. Specifically for customer we included some unique attributes such as gender, type of vehicle, age, family or no family. We did this in order to collect data relating to our marketing strategy in the future. Analyzing this data could prove useful in figuring out which customer stops for peanuts the most.# Database
"""

import sqlite3 # Once imported in a single notebook, it is available to us throughout the rest of the notebook.

# connect to database, if not there, create it.
connectionToDatabase = sqlite3.connect('PeanutData')

cursor = connectionToDatabase.cursor()

"""# Stand"""

cursor.execute('''create table IF NOT EXISTS Stands (StandID real PRIMARY KEY, Color text, Size text, Type text, TypeOfNut text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Stands (StandID, Color, Size, Type, TypeOfNut) VALUES (0006, 'Red', 'Small', 'Highway', 'Cashew')");
connectionToDatabase.commit()

cursor.execute('''select * from Stands;''')
for row in cursor.fetchall():
  print (row)

"""# Location Address"""

cursor.execute('''create table IF NOT EXISTS Locations (LocationAddress text PRIMARY KEY, Traffic text, SpeedLimit real, Visibility text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Locations (LocationAddress, Traffic, SpeedLimit, Visibility) VALUES ('Mile Marker 203', 'Moderate', 70, '3 miles')");
connectionToDatabase.commit()

cursor.execute('''select * from Locations;''')
for row in cursor.fetchall():
  print (row)

"""# Peanuts"""

cursor.execute('''create table IF NOT EXISTS Peanuts (PeanutsID text PRIMARY KEY, type text, price real, brand text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Peanuts (PeanutsID, type, price, brand) VALUES ('1928211', 'Honey Roasted', 19.99, 'Joes')");
connectionToDatabase.commit()

cursor.execute('''select * from Peanuts;''')
for row in cursor.fetchall():
  print (row)

"""# Hot Plates"""

cursor.execute('''create table IF NOT EXISTS Cooker (HotplateID text PRIMARY KEY, amount text, cost real, brand text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Cooker (HotplateID, amount, cost, brand) VALUES ('6933588', '1', 150, 'Jeromes')");
connectionToDatabase.commit()

cursor.execute('''select * from Cooker;''')
for row in cursor.fetchall():
  print (row)

"""# Employees"""

cursor.execute('''create table IF NOT EXISTS Employees (EmployeeID text PRIMARY KEY, Name text, Phone real, Job text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Employees (EmployeeID, Name, Phone, Job) VALUES ('1668978', 'Louis', 8524551273, 'Janitor')");
connectionToDatabase.commit()

cursor.execute('''select * from Employees;''')
for row in cursor.fetchall():

  print (row)

"""# Customer"""

cursor.execute('''create table IF NOT EXISTS Customer (CustomerID text PRIMARY KEY, Gender text, Family text, Age real)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Customer (CustomerID, Gender, Family, Age) VALUES ('8753492', 'Female', 'Yes', 56)");
connectionToDatabase.commit()

cursor.execute('''select * from Customer;''')
for row in cursor.fetchall():

  print (row)

"""# Fryers"""

cursor.execute('''create table IF NOT EXISTS Fryer (EquipmentID text PRIMARY KEY, Cost real, Size text, Expiration text)''')
connectionToDatabase.commit()

cursor.execute("INSERT INTO Fryer (EquipmentID, Cost, Size, Expiration) VALUES ('1383', 450, 'Large', '10')");
connectionToDatabase.commit()

cursor.execute('''select * from Fryer;''')
for row in cursor.fetchall():

  print (row)

"""Scenario : John is a roasted peanut phenom who loves to enjoy the sweet taste of roasted peanuts. John is driving down i80 with his family of 3 in the Subaru Outback he owns. John is going 80 miles an hour when he sees the roasted peanuts sign along the highway. He immediately begins to desire the roasted peanuts. He tells his family hey, how would you guys like to get some snacks and they reply with we would love to. John slams on the breaks and pulls off to our roasted peanut stand conveniently placed alongside the rest stop. John and his family come to the stand where we have an employee working hard. John notices the prices of our roasted peanuts and thinks they are a little expensive but he knows that he already pulled off the highway and has to make a purchase at this point, John does not want to let his kids down. John and his family purchase 4 bags of roasted peanuts and leave the stand satisfied as they are delicious. John knows that next time he drives this same highway he will pull back up to roasted highway peanuts again.

**What are the Price Options in Descending order?**
"""

cursor.execute('''select * from Peanuts ORDER BY price DESC ''')
for row in cursor.fetchall():
  print (row)

"""John and hs family are really hungry so they know that they need at least four bags of peanuts.  Although, once they get to the stand they realize that many of the peanut options are a bit more pricey than they anticipated.  Nonetheless, they are on the side of a highway and have no other option than to buy the peanuts.  John wants to save as much money as possible on the purchase, so he is curious to see what the cheapest option is.  After running the SQL query, he finds that the cheapest options are plain and roasted peanuts.  John knows his kids and wife love roasted peanuts, so he decides to go with the roasted peanuts.  Four bags of peanuts later, their stomachs are full and John didn't break the bank, solid win-win all around.

**How Many Fryers Does the Stand Own?**
"""

cursor.execute('''select COUNT(EquipmentID) from Fryer ''')
for row in cursor.fetchall():
  print (row)

"""John wants to buy four bags of peanuts which is quite the hefty order.  In order to satisfy John and his order in a timely manner, the owners of the stnad need to know how many fryers are available.  Once they know, they can give John a rough estimate of how much time it will take them, and it will also tell them how many employees they need to allocate to each fryer.  After running the SQL query, they find that there are five fryers, so they can tell John it will take about 10 minutes and assign each Fry Cook to two fryers a piece.

**What is the Brand of Peanuts that the Stand Uses?**
"""

cursor.execute('''select brand from Peanuts''')
for row in cursor.fetchall():
  print (row)

"""John is very satisifed with the quality of peanuts that he received from the peanut stand.  So satisfied in fact, that he decided he needed to know what brand of peanuts the stand used so he could go home and try to recreate the roasted peanuts for the holidays.  John discovered that the stand uses the same brand for all of their peanuts.  Luckily for John, he lives right next to a Trader Joes and they are fully stocked with Joe's Peanuts!  He is already on thin ice with his marriage, and this could be the perfect holiday appetizer to win over his in-laws and impress his wife.  Thank goodness he could find out what brand they used!"""