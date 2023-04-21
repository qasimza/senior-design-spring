import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import multiprocessing as mp
import pandas as pd

headers = {'authority': 'translate.googleapis.com',
           'path': '/element/log?format=json&hasfast=true&authuser=0',
           'scheme': 'https',
           'accept': '*/*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7',
           'content-encoding': 'gzip',
           'origin': 'https://www.audiosparx.com',
           'referer': 'https://www.audiosparx.com/',
           'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'cross-site',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
           'x-client-data': 'CJW2yQEIprbJAQjBtskBCKmdygEIrpTLAQiUocsBCIbTzAEIm/7MAQiFoM0BCL6izQE=Decoded:message ClientVariations{repeated int32 variation_id = [3300117, 3300134, 3300161, 3313321, 3328558, 3330196, 3352966, 3358491, 3362821, 3363134];}',
           'x-goog-authuser': '0'
           }

master_list_of_links = {
    "Action": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.1/startrow.401"
    ],
    "Addiction": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.355/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.355/startrow.51"
    ],
    "Affection": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.216/startrow.451"
    ],
    "Again": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.219/startrow.401"
    ],
    "Age": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.2/startrow.301"
    ],
    "Alcohol": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.4/startrow.351"
    ],
    "Always": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.220/startrow.351"
    ],
    "America": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.196/startrow.401"
    ],
    "Angel / Angels": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.195/startrow.251"
    ],
    "Animals": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.5/startrow.301"
    ],
    "Apology": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.6/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.6/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.6/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.6/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.6/startrow.201"
    ],
    "Assurance": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.221/startrow.351"
    ],
    "Autumn / Fall": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.8/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.8/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.8/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.8/startrow.151"
    ],
    "Baby": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.291/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.291/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.291/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.291/startrow.151"
    ],
    "Bar Mitzvah": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.329/startrow.1"
    ],
    "Beach": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.10/startrow.301"
    ],
    "Beauty": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.11/startrow.401"
    ],
    "Beginning": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.264/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.264/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.264/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.264/startrow.151"
    ],
    "Believe": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.271/startrow.401"
    ],
    "Betrayal": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.12/startrow.301"
    ],
    "Birthday": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.14/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.14/startrow.51"
    ],
    "Bling": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.322/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.322/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.322/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.322/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.322/startrow.201"
    ],
    "Blue Jeans": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.337/startrow.251"
    ],
    "Body": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.15/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.15/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.15/startrow.101"
    ],
    "Boots": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.262/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.262/startrow.51"
    ],
    "Booze": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.211/startrow.251"
    ],
    "Boys": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.16/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.16/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.16/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.16/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.16/startrow.201"
    ],
    "Break Up": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.222/startrow.401"
    ],
    "Car / Cars": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.18/startrow.351"
    ],
    "Carnival": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.17/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.17/startrow.51"
    ],
    "Celebration": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.188/startrow.351"
    ],
    "Change": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.165/startrow.401"
    ],
    "Cheating": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.20/startrow.301"
    ],
    "Children": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.21/startrow.401"
    ],
    "Christian": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.333/startrow.351"
    ],
    "Christmas": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.236/startrow.301"
    ],
    "Club": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.237/startrow.351"
    ],
    "Colors": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.25/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.25/startrow.51"
    ],
    "Come Back": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.223/startrow.351"
    ],
    "Comedy": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.26/startrow.301"
    ],
    "Coming Out": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.328/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.328/startrow.51"
    ],
    "Commitment": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.224/startrow.401"
    ],
    "Compassion": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.225/startrow.401"
    ],
    "Crime": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.28/startrow.301"
    ],
    "Crying": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.29/startrow.401"
    ],
    "Dance": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.30/startrow.401"
    ],
    "Danger": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.202/startrow.351"
    ],
    "Dark / Brooding": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.31/startrow.351"
    ],
    "Death": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.33/startrow.351"
    ],
    "Demons": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.200/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.200/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.200/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.200/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.200/startrow.201"
    ],
    "Depressing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.255/startrow.401"
    ],
    "Desire": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.35/startrow.351"
    ],
    "Despair": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.257/startrow.351"
    ],
    "Destiny": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.214/startrow.451"
    ],
    "Devotion": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.37/startrow.401"
    ],
    "Disgust": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.38/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.38/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.38/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.38/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.38/startrow.201"
    ],
    "Distance": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.39/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.39/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.39/startrow.101"
    ],
    "Divorce": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.40/startrow.251"
    ],
    "Dreams": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.41/startrow.401"
    ],
    "Drinking": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.354/startrow.251"
    ],
    "Drugs": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.42/startrow.251"
    ],
    "Earth": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.43/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.43/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.43/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.43/startrow.151"
    ],
    "Easy": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.226/startrow.401"
    ],
    "Ending": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.265/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.265/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.265/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.265/startrow.151"
    ],
    "Environment": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.45/startrow.301"
    ],
    "Evening": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.185/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.185/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.185/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.185/startrow.151"
    ],
    "Eyes": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.46/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.46/startrow.51"
    ],
    "Falling": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.166/startrow.251"
    ],
    "Fame": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.300/startrow.251"
    ],
    "Family": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.47/startrow.401"
    ],
    "Fashion": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.48/startrow.451"
    ],
    "Fate": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.215/startrow.401"
    ],
    "Father": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.294/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.294/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.294/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.294/startrow.151"
    ],
    "Fear / Fears": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.175/startrow.351"
    ],
    "Feeling Good": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.242/startrow.401"
    ],
    "Festival": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.184/startrow.401"
    ],
    "Fight": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.49/startrow.351"
    ],
    "Fire": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.50/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.50/startrow.51"
    ],
    "Flowers": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.51/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.51/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.51/startrow.101"
    ],
    "Flying": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.164/startrow.251"
    ],
    "Food / Drink": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.52/startrow.251"
    ],
    "Forest": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.53/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.53/startrow.51"
    ],
    "Forgiveness": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.54/startrow.401"
    ],
    "Freedom": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.55/startrow.351"
    ],
    "Friendship": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.56/startrow.351"
    ],
    "Fun": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.57/startrow.401"
    ],
    "Funeral / Wake": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.218/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.218/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.218/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.218/startrow.151"
    ],
    "Future": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.58/startrow.301"
    ],
    "Gambling": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.59/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.59/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.59/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.59/startrow.151"
    ],
    "Girls": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.60/startrow.351"
    ],
    "God": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.191/startrow.401"
    ],
    "Good Life": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.243/startrow.351"
    ],
    "Goodbye": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.61/startrow.351"
    ],
    "Gospel": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.273/startrow.301"
    ],
    "Graduation": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.189/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.189/startrow.51"
    ],
    "Guilty Pleasures": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.244/startrow.351"
    ],
    "Gun": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.62/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.62/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.62/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.62/startrow.151"
    ],
    "Hair": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.245/startrow.1"
    ],
    "Halloween": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.276/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.276/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.276/startrow.101"
    ],
    "Hanukkah": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.330/startrow.1"
    ],
    "Happy": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.246/startrow.351"
    ],
    "Harvest": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.182/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.182/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.182/startrow.101"
    ],
    "Health": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.63/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.63/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.63/startrow.101"
    ],
    "Heart": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.64/startrow.401"
    ],
    "Heartache": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.65/startrow.351"
    ],
    "Heat": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.168/startrow.1"
    ],
    "Hello": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.68/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.68/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.68/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.68/startrow.151"
    ],
    "Helping": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.69/startrow.401"
    ],
    "Hiding": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.178/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.178/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.178/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.178/startrow.151"
    ],
    "High": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.70/startrow.351"
    ],
    "History": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.71/startrow.301"
    ],
    "Holiday / Holidays": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.72/startrow.351"
    ],
    "Home": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.73/startrow.351"
    ],
    "Homosexual": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.351/startrow.1"
    ],
    "Hope": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.74/startrow.401"
    ],
    "Hurt": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.259/startrow.351"
    ],
    "In Requiem": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.274/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.274/startrow.51"
    ],
    "Infidelity": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.198/startrow.301"
    ],
    "Inspirational": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.275/startrow.351"
    ],
    "Jealousy": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.197/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.197/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.197/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.197/startrow.151"
    ],
    "Joy": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.77/startrow.401"
    ],
    "Kiss": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.78/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.78/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.78/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.78/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.78/startrow.201"
    ],
    "Late": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.267/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.267/startrow.51"
    ],
    "Leaving": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.80/startrow.351"
    ],
    "Life": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.81/startrow.451"
    ],
    "Light": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.82/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.82/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.82/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.82/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.82/startrow.201"
    ],
    "Living large": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.209/startrow.251"
    ],
    "Loneliness": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.83/startrow.401"
    ],
    "Lonely": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.84/startrow.301"
    ],
    "Longing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.162/startrow.351"
    ],
    "Loss / Losing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.85/startrow.351"
    ],
    "Love": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.86/startrow.351"
    ],
    "Low": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.87/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.87/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.87/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.87/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.87/startrow.201"
    ],
    "Luck": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.88/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.88/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.88/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.88/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.88/startrow.201"
    ],
    "Lust": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.176/startrow.351"
    ],
    "Lying": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.228/startrow.251"
    ],
    "Mad": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.290/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.290/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.290/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.290/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.290/startrow.201"
    ],
    "Magic": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.89/startrow.351"
    ],
    "Marriage": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.90/startrow.301"
    ],
    "Media": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.347/startrow.451"
    ],
    "Meditation": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.91/startrow.401"
    ],
    "Memories": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.92/startrow.401"
    ],
    "Men / Man": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.93/startrow.401"
    ],
    "Missed / Missing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.229/startrow.351"
    ],
    "Money": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.94/startrow.351"
    ],
    "Morning": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.95/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.95/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.95/startrow.101"
    ],
    "Mother": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.293/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.293/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.293/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.293/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.293/startrow.201"
    ],
    "Mothers Day": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.326/startrow.1"
    ],
    "Mountains": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.97/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.97/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.97/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.97/startrow.151"
    ],
    "Move": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.279/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.279/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.279/startrow.101"
    ],
    "Music": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.98/startrow.401"
    ],
    "Nature": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.100/startrow.401"
    ],
    "New": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.101/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.101/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.101/startrow.101"
    ],
    "New Romance": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.230/startrow.401"
    ],
    "New Years": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.295/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.295/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.295/startrow.101"
    ],
    "Night": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.96/startrow.401"
    ],
    "Nostalgia": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.102/startrow.401"
    ],
    "Ocean": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.104/startrow.251"
    ],
    "Old": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.105/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.105/startrow.51"
    ],
    "Oppressing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.107/startrow.301"
    ],
    "Pain": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.108/startrow.351"
    ],
    "Paranormal": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.109/startrow.301"
    ],
    "Party": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.110/startrow.301"
    ],
    "Peace": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.111/startrow.351"
    ],
    "People": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.112/startrow.401"
    ],
    "Philosophical": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.260/startrow.401"
    ],
    "Places": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.113/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.113/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.113/startrow.101"
    ],
    "Pleasure": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.114/startrow.401"
    ],
    "Politics": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.115/startrow.401"
    ],
    "Poverty": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.116/startrow.251"
    ],
    "Praying": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.183/startrow.401"
    ],
    "Prison / Jail": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.174/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.174/startrow.51"
    ],
    "Racism": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.298/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.298/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.298/startrow.101"
    ],
    "Radio": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.171/startrow.451"
    ],
    "Rain": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.118/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.118/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.118/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.118/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.118/startrow.201"
    ],
    "Reality": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.119/startrow.401"
    ],
    "Relationships": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.120/startrow.401"
    ],
    "Religion": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.121/startrow.401"
    ],
    "Revolution": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.122/startrow.351"
    ],
    "Right": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.123/startrow.351"
    ],
    "River": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.124/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.124/startrow.51"
    ],
    "Road / Road Trip": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.280/startrow.351"
    ],
    "Rolling": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.210/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.210/startrow.51"
    ],
    "Romance": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.125/startrow.301"
    ],
    "Ruby": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.346/startrow.1"
    ],
    "Running": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.177/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.177/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.177/startrow.101"
    ],
    "Runway": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.349/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.349/startrow.51"
    ],
    "Sad": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.261/startrow.401"
    ],
    "Sea / Ships": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.281/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.281/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.281/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.281/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.281/startrow.201"
    ],
    "Searching": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.126/startrow.351"
    ],
    "Seasons": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.213/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.213/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.213/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.213/startrow.151"
    ],
    "Self Discovery": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.350/startrow.351"
    ],
    "Sensual": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.127/startrow.351"
    ],
    "Sexy / Hot": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.247/startrow.251"
    ],
    "Singing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.292/startrow.351"
    ],
    "Sky": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.129/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.129/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.129/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.129/startrow.151"
    ],
    "Sleeping": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.130/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.130/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.130/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.130/startrow.151"
    ],
    "Smiling": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.131/startrow.401"
    ],
    "Smoking": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.132/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.132/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.132/startrow.101"
    ],
    "Snow": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.301/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.301/startrow.51"
    ],
    "Society": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.133/startrow.351"
    ],
    "Sorry": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.231/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.231/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.231/startrow.101"
    ],
    "Soul": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.190/startrow.401"
    ],
    "Space": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.134/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.134/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.134/startrow.101"
    ],
    "Spirit / Ghost": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.135/startrow.351"
    ],
    "Sports": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.136/startrow.401"
    ],
    "Spring": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.137/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.137/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.137/startrow.101"
    ],
    "St Patricks Day": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.289/startrow.1"
    ],
    "Star": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.138/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.138/startrow.51"
    ],
    "Stars": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.139/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.139/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.139/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.139/startrow.151"
    ],
    "Start": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.270/startrow.1"
    ],
    "Stay / Staying": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.170/startrow.351"
    ],
    "Stopping": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.140/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.140/startrow.51"
    ],
    "Street": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.141/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.141/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.141/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.141/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.141/startrow.201"
    ],
    "Streets / Roads": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.282/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.282/startrow.51"
    ],
    "Strip": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.248/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.248/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.248/startrow.101"
    ],
    "Suffering": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.169/startrow.351"
    ],
    "Suicide": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.142/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.142/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.142/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.142/startrow.151"
    ],
    "Summer": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.143/startrow.351"
    ],
    "Sun / Moon / Sky": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.144/startrow.251"
    ],
    "Suspense": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.145/startrow.401"
    ],
    "Taste": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.201/startrow.1"
    ],
    "Tears / Cry": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.146/startrow.401"
    ],
    "Television": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.401",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.325/startrow.451"
    ],
    "Time": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.147/startrow.301"
    ],
    "Today": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.207/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.207/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.207/startrow.101"
    ],
    "Together": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.232/startrow.351"
    ],
    "Tomorrow": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.172/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.172/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.172/startrow.101"
    ],
    "Tonight": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.208/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.208/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.208/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.208/startrow.151"
    ],
    "Transportation": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.283/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.283/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.283/startrow.101"
    ],
    "Travel": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.148/startrow.301"
    ],
    "Vacation": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.284/startrow.251"
    ],
    "Valentines Day": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.327/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.327/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.327/startrow.101"
    ],
    "Vibe": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.233/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.233/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.233/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.233/startrow.151"
    ],
    "Victory": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.149/startrow.301"
    ],
    "Waiting": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.163/startrow.401"
    ],
    "Waking": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.167/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.167/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.167/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.167/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.167/startrow.201"
    ],
    "Walking": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.150/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.150/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.150/startrow.101"
    ],
    "Wanting": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.180/startrow.351"
    ],
    "War": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.151/startrow.351"
    ],
    "Watching": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.179/startrow.351"
    ],
    "Water": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.152/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.152/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.152/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.152/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.152/startrow.201"
    ],
    "Wealth": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.153/startrow.301"
    ],
    "Weather": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.154/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.154/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.154/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.154/startrow.151"
    ],
    "Wedding": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.234/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.234/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.234/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.234/startrow.151"
    ],
    "Wild": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.250/startrow.301"
    ],
    "Wind": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.155/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.155/startrow.51"
    ],
    "Winning": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.156/startrow.301"
    ],
    "Winter": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.157/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.157/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.157/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.157/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.157/startrow.201"
    ],
    "Wishing": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.351",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.212/startrow.401"
    ],
    "Witches": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.204/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.204/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.204/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.204/startrow.151"
    ],
    "Women / Woman": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.158/startrow.351"
    ],
    "Working": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.159/startrow.351"
    ],
    "World": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.251",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.301",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.285/startrow.351"
    ],
    "Wrong": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.160/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.160/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.160/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.160/startrow.151"
    ],
    "Yes": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.173/startrow.1"
    ],
    "You": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.101",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.151",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.201",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.235/startrow.251"
    ],
    "Young": [
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.161/startrow.1",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.161/startrow.51",
        "https://www.audiosparx.com/sa/display/search.cfm/subject_iid.161/startrow.101"
    ]
}

out_file = open(r'C:\Users\Zaina\OneDrive - University of Cincinnati\Spring 2023\Senior Design\ml_code\data\themes.csv',
                'a')


def get_songs(items):
    theme = items[0]
    print(theme)
    list_of_links = items[1]
    songs = {
        'track_name': list(),
        'artist': list(),
        'theme': list()
    }
    for link in list_of_links:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        tables_of_songs = soup.find('table', {'id': 'mainTable'}).find_all('table', {'class': 'tableBorderless'})
        for table in tables_of_songs:
            a_s = table.find_all('a', {'class': 'alink tfont13'})
            if len(a_s) > 1:
                songs['track_name'].append(a_s[0].text)
                songs['artist'].append(a_s[1].text)
                songs['theme'].append(theme)
    songs_df = pd.DataFrame(songs)
    print(songs_df)
    songs_df.to_csv(out_file, index=False)


'''
    for theme in master_list_of_links.items():
        print(theme[0])
        get_songs(theme).to_csv(out_file, index=False)
'''
if __name__ == '__main__':
    pool = mp.Pool(8)
    pool.map(get_songs, master_list_of_links.items())
