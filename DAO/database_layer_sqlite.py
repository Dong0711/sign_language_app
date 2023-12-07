import sqlite3
class DatabaseLayer:
    def __init__(self) -> None:
        self.db_name='DAO/SignLanguageDB.db'
    def execute_query(self,query):
        try:
            sqlite_connection=sqlite3.Connection(self.db_name)
            cursour=sqlite_connection.cursor()
            cursour.execute(query)
            result=cursour.fetchall()
            print(result)
            cursour.close()
            return result
        except sqlite3.Error as error:
            print(f'error {error}')
        finally:
            if sqlite_connection:
                sqlite_connection.close()
    def execute_scalar(self,query):
        try:
            sqlite_connection=sqlite3.Connection(self.db_name)
            cursour=sqlite_connection.cursor()
            cursour.execute(query)
            result=cursour.fetchone()
            print(f'{result[0]}')
            cursour.close()
            return result
        except sqlite3.Error as error:
            print(f'error {error}')
        finally:
            if sqlite_connection:
                sqlite_connection.close()
    def execute_non_query(self,query):
        try:
            sqlite_connection=sqlite3.Connection(self.db_name)
            cursour=sqlite_connection.cursor()
            cursour.execute(query)
            sqlite_connection.commit()
            cursour.close()
            return 
        except sqlite3.Error as error:
            print(f'error {error}')
        finally:
            if sqlite_connection:
                sqlite_connection.close()
    def get_sign_name(self):
        query='select sign_name from sign_dictionary'
        return self.execute_query(query)
    
    def get_link_and_sign_description(self,selected_item):
        query=f'SELECT sign_description,sign_link_video FROM sign_dictionary WHERE sign_name="{selected_item}"'
        return self.execute_scalar(query)
    def get_history(self):
        query=f'SELECT * FROM sign_history'
        return self.execute_query(query)
        
           
        
data=DatabaseLayer()
data.get_history()