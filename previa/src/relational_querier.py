import sqlite3
from sqlite3.dbapi2 import Cursor, Connection
from typing import Dict, List, Tuple, Union

## SQLite3 datatypes
## 
## NULL. The value is a NULL value.
## INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
## REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
## TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
## BLOB. The value is a blob of data, stored exactly as it was input.


class RelationalQuerier:
	conn : Connection = None
	c : Cursor = None

	def __init__(self):
		# temporary database
		#self.conn = sqlite3.self.connect(':memory:')

		# this line already checks if the db exists
		RelationalQuerier.conn = sqlite3.connect('breath.db')
		
		# create db cursor
		RelationalQuerier.c = RelationalQuerier.conn.cursor()

		# create table Sintomas
		RelationalQuerier.c.execute(
			"""
			CREATE TABLE IF NOT EXISTS Sintomas(
			Id INTEGER PRIMARY KEY
			Tipo TEXT,
			Ano INTEGER,
			Mês INTEGER,
			Dia INTEGER,
			Cidade TEXT,
			Paciente FOREIGN_KEY)
			""")

		# create table Clima
		RelationalQuerier.c.execute(
			"""
			CREATE TABLE IF NOT EXISTS Clima(
			id INTEGER PRIMARY KEY,
			prcp REAL,
			stp REAL,
			smax REAL,
			smin REAL,
			gbrd REAL,
			temp REAL,
			dewp REAL,
			tmax REAL,
			tmin REAL,
			dmax REAL,
			dmin REAL,
			hmax REAL,
			hmin REAL,
			hmdy REAL,
			wdct REAL,
			gust REAL,
			wdsp REAL,
			regi TEXT,
			prov TEXT,
			wsnm TEXT,
			inme INTEGER,
			lat REAL,
			lon REAL,
			elvt REAL,
			date_time DATETIME)
			""")
			
		RelationalQuerier.conn.commit()
	
	def query(self, query:str) -> Tuple[bool, Union[List[Dict[str, str]], None]]:
		"""Executes the desired query and fetch its results if there is any
        """
		result = None
		sucess = True
		
		try:
			result = RelationalQuerier.c.execute(query).fetchall()
			sucess = True
		except Exception:
			pass
		
		return sucess, result 

	def querymany(self, query:str) -> Tuple[bool, Union[List[Dict[str, str]], None]]:
		"""Executes the desired query and fetch its results if there is any
        """
		return RelationalQuerier.c.executemany(query).fetchall()

	def cancel(self):
		"""Close the database connection once the program is done with it.
		"""
		RelationalQuerier.conn.rollback()

	def commit(self):
	   RelationalQuerier.conn.commit()

	def _close(self):
		"""Close the database connection once the program is done with it.
		"""
		RelationalQuerier.conn.close()

	def __del__(self):
		self._close()