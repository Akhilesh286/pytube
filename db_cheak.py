from sqldb import dataBase
db = dataBase("bd.sqlite")
select_all = db.select_all("on_off")
print (select_all)