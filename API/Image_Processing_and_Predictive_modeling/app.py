from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

import random
import pandas as pd

from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)



# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('Curr', type=bool)
parser.add_argument('Predict', type=bool)
parser.add_argument('All', type=bool)

# Mongo DB connection


User = 'DisJoin'
Pass = '1234'
conn = MongoClient('mongodb+srv://DisJoin:<password>@cluster0-bk4u2.mongodb.net/<dbname>?retryWrites=true&w=majority')


mydb = conn["DisJoin_data"]
Col1 = mydb["Current_data"]
Col2 = mydb["Predict_data"]




def Get_data(A = False,C = False ,P = False ):


        df_C = pd.DataFrame(list(Col1.find())).drop('_id',axis = 1)
        df_P = pd.DataFrame(list(Col2.find())).drop('_id',axis = 1)


        if(A == True):
            return df_C.merge(df_P, on="Date_time", how="left")

        if(C == True):
            return df_C

        if(P == True):
            return df_P

        return False


class CP_data(Resource):

    def get(self,):

        args = parser.parse_args()
        Curr =  args['Curr']
        Predict =  args['Predict']
        All =  args['All']

        if(All == True):

            DF = {}
            df = Get_data(A = True)
            for i in range(len(df)):
                ll = str(df['count'][i]) +"   "+ str(df['Predict'][i])
                DF[df['Date_time'][i]] = str(ll)
            return DF

        elif(Curr==True):

            DF = {}
            df_C = Get_data(C = True)
            for i in range(len(df_C)):
                DF[df_C['Date_time'][i]] = str(df_C['count'][i])
            return DF

        elif(Predict==True):

             DF = {}
             df_P= Get_data(P = True)
             for i in range(len(df_P)):
                 DF[df_P['Date_time'][i]] = str(df_P['count'][i])
             return DF

        else :

            return dict()

api.add_resource(CP_data, '/find')


if __name__ == '__main__':
    app.run(debug=True)
