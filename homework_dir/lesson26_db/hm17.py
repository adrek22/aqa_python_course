import sqlite3


class DBManagerSQLite:
    def __init__(self, path_to_db: str, table_name: str, create_table_columns: str):
        self.path_to_db = path_to_db
        self.create_table_columns = create_table_columns
        self.table_name = table_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self._connect()
        print('DB connection is established')
        self._create_table()
        return self

    def _connect(self):
        self.connection = sqlite3.connect(self.path_to_db)
        self.cursor = self.connection.cursor()

    def _create_table(self):
        query = f'CREATE TABLE IF NOT EXISTS {self.table_name} {self.create_table_columns}'
        self._execute_query(query, (), f'{self.table_name} DB table is created')

    def _delete_table(self):
        query = f'DROP TABLE IF EXISTS {self.table_name}'
        self._execute_query(query, (), f'{self.table_name} DB table is deleted')

    def add_data(self, columns: str, data: tuple):
        placeholders = ', '.join('?' * len(data))
        query = f'INSERT INTO {self.table_name} {columns} VALUES ({placeholders})'
        self._execute_query(query, data, f'Data {data} is added into {self.table_name} table with columns {columns}')

    def update_data(self, column: str, value: str, condition: str):
        query = f'UPDATE {self.table_name} SET {column} = ? WHERE {condition}'
        self._execute_query(query, (value,),
                            f'{column} is updated with {value} in {self.table_name} table where {condition}')

    def select_all(self):
        print(f"View all values from {self.table_name} table:")
        query = f'SELECT * FROM {self.table_name}'
        return self._execute_query(query, fetch=True)

    def select_by_condition(self, condition: str):
        print(f"View values from {self.table_name} table by {condition}:")
        query = f'SELECT * FROM {self.table_name} WHERE {condition}'
        return self._execute_query(query, fetch=True)

    def delete_data(self, condition: str):
        query = f'DELETE FROM {self.table_name} WHERE {condition}'
        self._execute_query(query, (), f'Row is deleted from {self.table_name} table where {condition}')

    def _execute_query(self, query: str, params=(), log_message=None, fetch=False):
        self.cursor.execute(query, params)
        self.connection.commit()
        if log_message:
            print(log_message)
        if fetch:
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._delete_table()
        self.connection.close()
        print('DB connection is closed')


if __name__ == "__main__":
    table_attributes = '''(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )'''

    products = [
        ("Orange", 0.5, 100),
        ("Apple", 0.3, 200),
        ("Banana", 0.2, 150)
    ]

    with DBManagerSQLite(path_to_db='shop.db', table_name='products', create_table_columns=table_attributes) as db_manager:
        for product in products:
            db_manager.add_data(columns='(name, price, quantity)', data=product)
        db_manager.select_all()
        db_manager.select_by_condition('price > 0.25')
        db_manager.update_data(column='price', value='0.25', condition='name = "Banana"')
        db_manager.select_all()
        db_manager.delete_data('name = "Apple"')
        db_manager.select_all()
