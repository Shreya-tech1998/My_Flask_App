import cx_Oracle

# create a connection string 
# <username><password>@<dbhostaddress>:<dbport>/<dbservicename>
# username = BULLFLIX_PY, Password = usf1956!, hostname reade.forest.usf.edu , port 1521, SID: cdb9
# f"{username}/{password}@{hostname}:{port}/{sid}"
conStr = 'BULLFLIX_PY/usf1956!@reade.forest.usf.edu:1521/cdb9'

connect = cx_Oracle.connect(conStr)
cur = connect.cursor()

cur.close()
connect.close()