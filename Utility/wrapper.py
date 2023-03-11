import json
import pandas as pd
import requests

"""
Created by      : Muhammad Faris Muzakki
Last updated at : 11/03/2023
"""

class Wrapper:
    def __init__(self, url, response_life_time=0):
        self.url = url
        self.response_life_time = response_life_time
        self.data = None
        self.usd_value = 15502.55 # can be made dynamic with the API from google
        self.refresh_data()
    
    def refresh_data(self):
        """
        replace current data with data from endpoint
        """
        # get data from api
        response = requests.get(self.url)
        response.raise_for_status()
        response_value = response.text
        response_value = json.loads(response_value)
        self.data = pd.DataFrame(response_value)

        # standardize data types
        self.normalize_data_type()

        # get usd to idr
        self.usd_value = 15502.55 # can be made dynamic with the API from google
        price_in_usd = [round(x/self.usd_value, 4) for x in self.data['price']]
        self.data['price_in_usd'] = price_in_usd

    def normalize_data_type(self):
        self.data = self.data.astype({
            "uuid": object,
            "komoditas": object,
            "area_provinsi": object,
            "area_kota": object,
            "size": float,
            "price": float,
            "timestamp": int
        })

    def get_data(self, order_by = [], ascending=True, limit=0):
        """
        obtaining current data 
        """
        result = self.data.sort_values(order_by, ascending=ascending)
            
        return result.to_dict('records') if limit == 0 else \
            result.head(limit).to_dict('records')
    
    def get_columns_name(self):
        """
        obtaining all columns name
        """
        return self.data.columns.tolist()
    
    def get_by_id(self, id):
        """
        obtaining datum selected by id
        """
        return self.data[self.data['uuid'] == id] \
            .to_dict('records')[0] if self.data[self.data['uuid'] == id] \
            .to_dict('records') else None
    
    def filter_by_column(self, column_name, value):
        """
        obtaining data selected by column value
        column name : area_provinsi, area_kota, komoditas
        """
        return self.data[(self.data[column_name]).str.lower() == value.lower()] \
            .to_dict('records')

    def filter_by_range(self, column_name, start, end, is_convert=True):
        """
        obtaining data selected by range for spesific column
        """
        data = self.data[(self.data[column_name] >= start) & 
            (self.data[column_name] <= end)]

        return data if not is_convert else data.to_dict('records')
    
    def max_value(self, column_name):
        """
        obtaining max value from specific column
        """
        return self.data[self.data[column_name] == self.data[column_name].max()] \
            .to_dict('records')[0] if len(self.data.index) != 0 else None

    def max_value_by_range(self, column_name, start, end):
        """
        obtaining max value from specific column filtered by range
        """
        data = self.filter_by_range('timestamp', start, end, False)
        return data[data[column_name] == data[column_name].max()] \
            .to_dict('records')[0] if len(data.index) != 0 else []

    def min_value(self, column_name):
        """
        obtaining min value from specific column
        """
        return self.data[self.data[column_name] == self.data[column_name].min()] \
            .to_dict('records')[0] if len(self.data.index) != 0 else None
    
    def min_value_by_range(self, column_name, start, end):
        """
        obtaining min value from specific column filtered by range
        """
        data = self.filter_by_range('timestamp', start, end, False)
        return data[data[column_name] == data[column_name].min()] \
            .to_dict('records')[0] if len(data.index) != 0 else None