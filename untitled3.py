# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:31:06 2020

@author: akinmade
"""


import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Kinshade/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data science', 15, False, path, 60)