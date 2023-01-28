from app import db
from data_prep import app_data_ingestion,inp_data_ingestion
db.create_all()
print(app_data_ingestion())
# print(inp_data_ingestion())

# db.update()

# import datetime

# datetime.datetime.now()

# import sqlalchemy
# import pandas as pd

# from sqlalchemy import inspect

# #2.-Turn on database engine
# # dbEngine=sqlalchemy.create_engine('sqlite:///../database.db') # ensure this is the correct path for the sqlite file. 

# from app import db,  Users,InPatientsData,AppointmentsData

# from sqlalchemy import update

# inp_data = AppointmentsData.query.all()

# print(inp_data)
print("Successfully DB created")