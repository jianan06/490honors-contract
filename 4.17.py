# Jianan Hao
# April 17th 2020
# COMP490 Honors Contract
import json
import requests
from operator import itemgetter
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# get data and a source of house price
def get_data(location:str):
    url = f"https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict = r.json()

    submission_price = r.json()
    submission_dicts = []
    submission_location = r.json()

# build a dictionary for price
    submission_dicts = {
    'price': response_dict['price'],
    'link': f"https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt"
    'location': response_dict['location']
    }
    submission_dicts.append(submission_dicts)

    submission_dicts = sorted(submission_dicts, key=itemgetter('location'), reverse=True)
def print_data(submission_dicts=None):
    for submission_dict in submission_dicts:
        print(f"\nPrice: {submission_dict['price']}")
        print(f"location: {submission_dict['location']}")
    pass
    #Jianan to fill in here- step through the data and print it
    # this is temporary but useful to make sure get_data worked

# building a map
def lons(args):
    pass

def lats(args):
    pass

data = [Scattergeo(lon = lons, lat = lats)]
my_layout = Layout(title = 'house price')

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename = 'https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt')
def main():
    api_location = ""#Jianan replace the "" with the actual address
    returned_data = get_data()
    print_data(returned_data)

if __name__ == '__main__':
    main()
