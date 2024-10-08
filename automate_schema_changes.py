import mysql.connector
from mysql.connector import Error
import os

def deploy_database_changes():
    try:
        # Fetch environment variables
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')

        # Establish a connection to the MySQL database using environment variables
        connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )

        if connection.is_connected():
            print(f"Connected to the database {db_name} at {db_host}")

            # Create a cursor object
            cursor = connection.cursor()

            # Read SQL file
            sql_file_path = "update_projects_schema.sql"
            with open(sql_file_path, 'r') as file:
                sql_script = file.read()

            # Execute the SQL script
            for statement in sql_script.split(';'):
                if statement.strip():  # Skip empty statements
                    cursor.execute(statement)
                    print("Executed SQL statement successfully")

            # Commit the changes
            connection.commit()
            print("SQL script executed successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    deploy_database_changes()
