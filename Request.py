# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 10:59:44 2019

@author: Suresh Mylam
"""

import requests

url = 'http://localhost:5000/predict'
r=requests.post(url,json={'YearsExperience':2})

print(r.json())