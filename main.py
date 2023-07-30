import psycopg2

connecting = psycopg2.connect(host="localhost", dbname="postgres", user="postgres"
                        , password="230110", port="5432")

cursor = connecting.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")

cursor.execute("""INSERT INTO person (id,name,age,gender) VALUES
(1, 'Spencer', 23, 'm'),
(2, 'Thomas', 11, 'm'),
(3, 'Lourdes', 58, 'f'),
(4, 'Eduardo', 27, 'm'),
(5, 'Mateo', 11, 'm');
""")

cursor.execute("""CREATE TABLE weather(
               id INT PRIMARY KEY,
               city varchar(80),
               lowtemp int,
               hightemp int,
               date date
); 
""")
cursor.execute("""INSERT INTO weather VALUES (1, 'Lima', 14, 22, '2023-07-30'); 
""")

#cursor.execute("""SELECT * from person WHERE name = 'Lourdes';""")
#print(cursor.fetchone())



connecting.commit()

cursor.close()
connecting.close()