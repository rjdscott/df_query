import pandas as pd
import sqlite3 as sq
import os


class QueryContext:
    def __init__(self, db_path: str = "file::memory:?mode=memory&cache=shared"):
        self.db_path = db_path

    def create_view(self, df: pd.DataFrame, table_name: str):
        """
        Creates a table in sqlite containing the df data using to pandas.to_sql()
        :param df: pandas.DataFrame
        :param table_name: str
        :return: None
        """
        with sq.connect(self.db_path) as conn:
            df.to_sql(table_name, con=conn, if_exists='replace', index=False)
            print(f"created table: '{table_name}' in {self.db_path}")

    def sql(self, sql_query: str):
        """
        Execute a SQL query and return a pandas.DataFrame.
        The syntax must be of the SQLite flavor as sqlite is the
        underlying database.
        :param sql_query: str
        :return: pandas.DataFrame
        """
        with sq.connect(self.db_path) as conn:
            return pd.read_sql(sql_query, con=conn)

    def show_tables(self):
        """
        Dislpay tables contained in the sqlite database instantiated
        with this class
        :return:
        """
        with sq.connect(self.db_path) as conn:
            sql_query = "SELECT name FROM sqlite_master WHERE type='table';"
            return pd.read_sql(sql_query, con=conn)

    def print_table_schema(self, table_name):
        """
        Prints the table columns and types
        :param table_name:
        :return: dict()
        """
        df_tables = self.show_tables()
        if table_name in list(df_tables.name):
            with sq.connect(self.db_path) as conn:
                df = pd.read_sql(f'select * from {table_name} limit 1;', con=conn)
                return dict(df.dtypes)
        pass

    def db_cleanup(self):
        """
        Cleans up the SQLite database if it is being persisted to disk.
        :return: None
        """
        if ':memory:' not in self.db_path and os.path.exists(self.db_path):
            os.remove(self.db_path)
            print(f"database '{self.db_path}' has been removed.")
        else:
            print(f"Database '{self.db_path}' does not exist.")
