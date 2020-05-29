# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:17:46 2020

@author: akinmade
"""


import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Kinshade/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data science', 15, False, path, 60)

JavascriptExecutor executor = (JavascriptExecutor) driver;
executor.executeScript("arguments[0].click();", element);

def click_link(element):
    executeScript("arguments[0].click();", element);
    
click_link(job_button)