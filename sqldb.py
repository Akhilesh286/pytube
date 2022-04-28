"""
#from sqldb import dataBase
db = dataBase(file="db2.db")
colm = "name text , age text"
#db.create_table('sample1',colm)
#col = "(:name,:age)"
val = {
  'name':"akhil",
  'age':"14"
}
#val = {'name':"akhilesh007",'age':"15"}

#insert = db.insert_table('sample1',val,col)

#sselect_all = db.select_all('ample1')
#print (select_all)

#select = db.select(table='sample1',col='age')
#print (select)


#select_condition = db.select_condition(table='sample1',col='*', condition='age>14')
#print (select_condition)

#db.update(table='sample1',SET="name='Akash007'", where="age='15'")

#db.delete('sample1',"age='14'")
"""

import sqlite3


class dataBase:
  def __init__ (self,file):
    self.file = file
    conn = sqlite3.connect(file)
    
    # Create A Cursor
    c = conn.cursor()
    self.c = c
    # Commit our changes
    self.c = c
    self.conn = conn
    # Create A Table
  def create_table(self,table,colm):
    c = self.c
    conn = self.conn
    
    c.execute(f"""CREATE TABLE if not exists {table} ({colm})
    """)
    # Commit our changes
    conn.commit()
    
    # Close our connection
    #conn.close()
  def insert_table (self,table,val,col):
    c = self.c
    conn = self.conn
    
    c.execute(f"INSERT INTO {table} VALUES {col}",val)
    # Commit our changes
    conn.commit()
    
    # Close our connection
    
  def select_all (self,table):
    c = self.c
    conn = self.conn
    
    # Grab records from database
    sh = c.execute(f"SELECT * FROM {table}")
    records = c.fetchall()

    word = ''
    value = ''
    # Loop thru records
    for record in records:
      word = f"{word}\n{record}"
      value = f'{word}'

    # Commit our changes
    conn.commit()

    # Close our connection
    #conn.close()
    return records
  def select (self,table,col):
    c = self.c
    conn = self.conn
    
    # Grab records from database
    sh = c.execute(f"SELECT {col} FROM {table}")
    records = c.fetchall()
    return records
  
  def select_condition (self,table,col, condition):
    c = self.c
    conn = self.conn
    
    # Grab records from database
    sh = c.execute(f"SELECT {col} FROM {table} WHERE {condition} ")
    records = c.fetchall()
    return records
  
  def update (self,table,SET,where):
    c = self.c
    conn = self.conn
    
    sql_update_query = f"""Update {table} set {SET} where {where} """
    c.execute(sql_update_query)
    conn.commit()
        
  def delete (self, table, condition):
    c = self.c
    conn = self.conn
    
    sql_update_query = f"DELETE FROM {table} WHERE {condition} "
    c.execute(sql_update_query)
    # Commit our changes
    conn.commit()

    # Close our connection
    conn.close()