import pandas as pd
from wrapper import Wrapper

# generate data -> ideally the data is stored into json
def generate_dumy_data():
    return pd.DataFrame([
       {
        "uuid": "803e4984-3336-402d-b9e1-555d196d3d20",
        "komoditas": "LELE",
        "area_provinsi": "JAWA BARAT",
        "area_kota": "BANDUNG",
        "size": "90",
        "price": "41000",
        "tgl_parsed": "2022-05-28T11:14:23Z",
        "timestamp": "1653736463756"
    },
    {
        "uuid": "7449225e-923b-42df-aa87-ba2b1ceffe1f",
        "komoditas": "BAWAL",
        "area_provinsi": "JAWA TIMUR",
        "area_kota": "BANYUWANGI",
        "size": "40",
        "price": "50000",
        "tgl_parsed": "2022-05-29T19:28:01Z",
        "timestamp": "1653852481368"
    },
    {
        "uuid": "534b25a9-97ed-4493-832f-3c072eb670bf",
        "komoditas": "GURAME",
        "area_provinsi": "JAWA TENGAH",
        "area_kota": " PURWOREJO",
        "size": "140",
        "price": "54000",
        "tgl_parsed": "2022-05-30T13:25:19Z",
        "timestamp": "1653917119976"
    }])

def test_wrapper_initialize():
    """
    test initialize wrapper object
    """
    end_point = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'
    wrapper = None
    try:
        wrapper = Wrapper(end_point)
    except:
        pass

    assert wrapper != None

    return wrapper 

def test_get_data(wrapper):    
    assert wrapper.get_data() == generate_dumy_data().to_dict('records')

def test_get_columns_name(wrapper):
    assert wrapper.get_columns_name() == ['uuid', 'komoditas', 
        'area_provinsi', 'area_kota', 'size', 'price', 'tgl_parsed', 'timestamp']

def test_get_by_id(wrapper):
    assert wrapper.get_by_id('534b25a9-97ed-4493-832f-3c072eb670bf') == \
        generate_dumy_data().to_dict('records')[2]

def test_filter_by_column(wrapper):
    assert wrapper.filter_by_column('komoditas', 'lele')[0] == \
        generate_dumy_data().to_dict('records')[0]
    
    assert wrapper.filter_by_column('area_provinsi', 'jawa barat')[0] == \
        generate_dumy_data().to_dict('records')[0]

    assert wrapper.filter_by_column('area_kota', 'bandung')[0] == \
        generate_dumy_data().to_dict('records')[0]

def test_filter_by_range(wrapper):
    wrapper.filter_by_range('price', '10000', '42000', is_convert=True) == \
        list(generate_dumy_data().to_dict('records')[0])

def test_max_value(wrapper):
    assert wrapper.max_value('price') == generate_dumy_data().to_dict('records')[2]

def test_min_value(wrapper):
    assert wrapper.min_value('price') == generate_dumy_data().to_dict('records')[0]

if __name__ == "__main__":
    
    print("Initialize Wrapper Object...")
    wrapper = test_wrapper_initialize()

    print("Get Data...")
    wrapper.data = generate_dumy_data()
    status = test_get_data(wrapper)
    
    print("Get Columns Name...")
    test_get_columns_name(wrapper)

    print("Get Datum by ID...")
    test_get_by_id(wrapper)

    print("Get Data by Column Value...")
    test_filter_by_column(wrapper)

    print("Get Data Filtered by Range..")
    test_filter_by_range(wrapper)

    print("Get Max Value...")
    test_max_value(wrapper)

    print("Get Min Value...")
    test_min_value(wrapper)


