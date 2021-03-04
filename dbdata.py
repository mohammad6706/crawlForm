import mysql.connector



class dbmysql:
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="123456",
      database="dbcrawlfrom"
    )
    self.mycursor = self.mydb.cursor()

  def inserttbl_detail(self,catId,community,countCat,countSend):
    sql = "INSERT INTO tbl_detail (catId,community,countCat,countSend) VALUES (%s,%s,%s,%s)"
    val=(catId,community,countCat,countSend)
    self.mycursor.execute(sql,val)
    self.mydb.commit()
    return True
  def inserttbl_category(self,val):
    sql = "INSERT INTO tbl_category (name) VALUES (%s)"
    val=(val,)
    self.mycursor.execute(sql,val)
    self.mydb.commit()
    return True

  def serchtbl_cat(self,val):
    sql = "SELECT * FROM tbl_category where name=(%s)"
    q = (val,)
    self.mycursor.execute(sql, q)
    myresult = self.mycursor.fetchall()
    return myresult

  def serchtbl_detail(self,val):
    sql = "SELECT * FROM tbl_detail where community=(%s)"
    q = (val,)
    self.mycursor.execute(sql, q)
    myresult = self.mycursor.fetchall()
    if len(myresult)==0:
      return True
    else:
      return False

  def showdatacrawl(self):
      sql = "SELECT \
        tbl_category.name AS category, \
        community, \
        countCat,\
        countSend\
        FROM tbl_detail \
        LEFT JOIN tbl_category ON tbl_detail.catId = tbl_category.id"
      self.mycursor.execute(sql)
      myresult = self.mycursor.fetchall()
      return myresult