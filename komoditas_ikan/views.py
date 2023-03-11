from Utility.wrapper import Wrapper

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

import json

class KomoditasView(View):

    ENDPOINT = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'

    def __init__(self):
        super(KomoditasView, self).__init__()
        self.wrapper = Wrapper(self.ENDPOINT)

    def get(self, request):

        self.fill_request(request)
        data = self.wrapper.get_data(request.GET['order_by'].replace(' ','').split(','),
            True if request.GET['ascending'] == 'True' else False, int(request.GET['limit']))

        data_by_id = self.wrapper.get_by_id(request.GET['filter_id'])
        
        data_by_range = self.wrapper.filter_by_range(request.GET['range_name'],
            int(request.GET['start']), int(request.GET['end']))
        
        data_by_column_value = self.wrapper.filter_by_column(request.GET['filter_column'],
            request.GET['column_value'])

        max_column = self.wrapper.max_value(request.GET['max_column'])
        max_column_by_range = self.wrapper.max_value_by_range(request.GET['max_column_by_range'],
            int(request.GET['start_max']), int(request.GET['end_max']))

        min_column = self.wrapper.min_value(request.GET['min_column'])
        min_column_by_range = self.wrapper.min_value_by_range(request.GET['min_column_by_range'],
            int(request.GET['start_min']), int(request.GET['end_min']))

        context = {
            'data' : data,
            'data_by_id' : data_by_id,
            'columns' : self.wrapper.get_columns_name(),
            'data_by_range' : data_by_range,
            'data_by_column_value' : data_by_column_value,
            'max_column' : max_column,
            'max_column_by_range' : max_column_by_range,
            'min_column' : min_column,
            'min_column_by_range' : min_column_by_range
        }

        html_template = loader.get_template('index.html')
        return HttpResponse(html_template.render(context, request))

    def fill_request(self, request):
        request.GET._mutable=True
        if not request.GET.get('limit'):
            request.GET['limit'] = 10
        
        if not request.GET.get('order_by'):
            request.GET['order_by'] = "timestamp,price"
        
        if not request.GET.get('ascending'):
            request.GET['ascending'] = 'False'
        
        if not request.GET.get('filter_id'):
            request.GET['filter_id'] = '534b25a9-97ed-4493-832f-3c072eb670bf'
        
        if not request.GET.get('range_name'):
            request.GET['range_name'] = 'price'
        
        if not request.GET.get('start'):
            request.GET['start'] = 60000
        
        if not request.GET.get('end'):
            request.GET['end'] = 75000

        if not request.GET.get('filter_column'):
            request.GET['filter_column'] = 'area_provinsi'
        
        if not request.GET.get('column_value'):
            request.GET['column_value'] = 'jawa barat'
        
        if not request.GET.get('max_column'):
            request.GET['max_column'] = 'price'
        
        if not request.GET.get('min_column'):
            request.GET['min_column'] = 'price'

        if not request.GET.get('max_column_by_range'):
            request.GET['max_column_by_range'] = 'size'
        
        if not request.GET.get('start_max'):
            request.GET['start_max'] = 1653633097205
        
        if not request.GET.get('end_max'):
            request.GET['end_max'] = 1653917119976
        
        if not request.GET.get('min_column_by_range'):
            request.GET['min_column_by_range'] = 'size'
        
        if not request.GET.get('start_min'):
            request.GET['start_min'] = 1653633097205
        
        if not request.GET.get('end_min'):
            request.GET['end_min'] = 1653917119976
        

        