from django.shortcuts import render
from pandas import pandas as pd


def index(request):
  zillow = pd.read_csv('zillow_states.csv')

  # California = zillow.iloc[0, 5::12]
  date_group = []
  state_group = []
  price_group = []

  numStates = 0

  for state in zillow['RegionName']:
    state_group.append(state)
    numStates = numStates + 1

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

  for numb in range(numStates):
    for col in zillow.columns:
      if col == '1/31/2000':
        price_group.append(zillow[col][numb])
      if col == '1/31/2006':
        price_group.append(zillow[col][numb])
      if col == '1/31/2012':
        price_group.append(zillow[col][numb])
      if col == '1/31/2018':
        price_group.append(zillow[col][numb])
      if col == '1/31/2024':
        price_group.append(zillow[col][numb])

  data = {"States": state_group, "Dates": date_group, "Prices": price_group}

  return render(request, 'index.html', context=data)

