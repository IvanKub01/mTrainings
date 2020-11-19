
import os
import urllib.parse 
#SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://Ivan:Wingchun3@localhost\\SQLEXPRESS/Ezo'
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Ezo;UID=Ivan;PWD=Wingchun3")
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
#db.get_session('bind_name').execute(query, params)
#SQLALCHEMY_BINDS = {'Employees_auto': 'mssql+pymssql://mssk:Miba123+@Shaplmib013/MSSK_Employees'}
SQLALCHEMY_TRACK_MODIFICATIONS = False