import ijson
import mysql.connector
from tqdm import tqdm

# establish your MySQL connection
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='my_db')
cursor = cnx.cursor()

# create table query
table_query = (
"CREATE TABLE `owner_08` ("
"`id` INT NOT NULL,"
"`city_code` VARCHAR(45) NULL,"
"`parcel_id` VARCHAR(45) NULL,"
"`address` VARCHAR(200) NULL,"
"`droit` VARCHAR(10) NULL,"
"`siren` VARCHAR(45) NULL,"
"`raison_social` VARCHAR(100) NULL,"
"`sigle` VARCHAR(10) NULL,"
"`date_naissance` DATE NULL,"
"`lieu_naissance` VARCHAR(100) NULL,"
"`nom_prenom` VARCHAR(100) NULL,"
"`nom_prenom_conjoint` VARCHAR(100) NULL,"
"`sexe` VARCHAR(10) NULL,"
"`departement` VARCHAR(10) NULL,"
"`commune` VARCHAR(10) NULL,"
"`prefixe` VARCHAR(10) NULL,"
"`section` VARCHAR(10) NULL,"
"`numero` VARCHAR(10) NULL,"
"`direction` VARCHAR(45) NULL,"
"`batiment` VARCHAR(45) NULL,"
"`entree` VARCHAR(45) NULL,"
"`niveau` VARCHAR(45) NULL,"
"`porte` VARCHAR(45) NULL,"
"`code_droit` VARCHAR(45) NULL,"
"`signification_droit` VARCHAR(100) NULL,"
"`numero_majic` VARCHAR(45) NULL,"
"`is_completed` INT NULL,"
"PRIMARY KEY (`id`));"
)

# create table
cursor.execute(table_query)

# determine the total count of items in JSON
total_count = 0
with open('owner_08.json', 'r') as file:
    objects = ijson.items(file, 'item')
    for obj in objects:
        if obj['type'] == 'table' and obj['name'] == 'owner_08':
            total_count = len(obj['data'])

# open the file
with open('owner_08.json', 'r') as file:
    # get the generator
    objects = ijson.items(file, 'item')

    # setup tqdm
    pbar = tqdm(total=total_count)

    for obj in objects:
        # check the type and name
        if obj['type'] == 'table' and obj['name'] == 'owner_08':
            for item in obj['data']:
                keys = item.keys()
                values = tuple(item[key] for key in keys)
                query = "INSERT INTO owner_08 ({}) VALUES ({});".format(','.join(keys), ','.join(['%s']*len(values)))
                cursor.execute(query, values)

                # update tqdm
                pbar.update(1)

    # close tqdm
    pbar.close()

# commit the changes and close everything
cnx.commit()
cursor.close()
cnx.close()
