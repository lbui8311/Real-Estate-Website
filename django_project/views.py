#from django.http import HttpResponse
#import requests
from django.shortcuts import render
#from ipware import get_client_ip
from pandas import pandas as pd


def index(request):
  zillow = pd.read_csv('zillow_states.csv')
  #print(df)
  #df2024 = zillow['RegionName']

  California = zillow.iloc[0, 5::12]
  date_group = []
  state_group = []
  price_group = []

  for col in zillow.columns:
    if col == '1/31/2000':
      date_group.append(col)
    if col == '1/31/2006':
      date_group.append(col)
    if col == '1/31/2012':
      date_group.append(col)
    if col == '1/31/2018':
      date_group.append(col)
    if col == '1/31/2024':
      date_group.append(col)

  for state in zillow['RegionName']:
    state_group.append(state)

  test = zillow

  print(date_group)
  data = {
      "California_1": California[0],
      "California_2": California[3],
      "California_3": California[6],
      "California_4": California[9],
      "California_5": California[12],
      "California_6": California[15],
      "States": state_group,
      "Dates": date_group
  }

  return render(request, 'index.html', context=data)
