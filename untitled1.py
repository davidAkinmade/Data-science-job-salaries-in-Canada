# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:17:46 2020

@author: akinmade
"""


import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Kinshade/Documents/ds_salary_proj"

df = gs.get_jobs('data scientist', 15, False, path, 60)