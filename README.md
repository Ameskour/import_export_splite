# JSON to MySQL Importer with Progress Bar

This script is designed to read JSON data and import it into a MySQL database. It also includes a progress bar to give a visual representation of how much of the task is complete.

## Prerequisites

You need to install Python and these packages:

- `mysql-connector-python`
- `ijson`
- `tqdm`

Install them using pip:


## Code Explanation

This script uses Python's `mysql.connector` to connect to a MySQL database. It also uses the `ijson` library to read and process the JSON file and `tqdm` to display the progress.

The script starts by establishing a connection to the MySQL server and creating a cursor object.

The script then creates a table `owner_08` in the database `my_db`. The table structure is defined in the `table_query` variable.

Next, the script determines the total number of items in the JSON file using `ijson.items(file, 'item')` to generate a Python generator. The total count is used to setup the `tqdm` progress bar.

The script opens the JSON file again and for each object in the file, checks if the `type` is `'table'` and the `name` is `'owner_08'`. For every item in `obj['data']`, it creates a SQL query to insert the item into the `owner_08` table and executes the query. 

The progress bar is updated after each item is inserted.

Finally, the script commits the changes and closes the cursor and the MySQL connection.

## Running the Script

To run the script, make sure you have the JSON data file named `owner_08.json` in the same directory as your script. Then run the script with Python:

