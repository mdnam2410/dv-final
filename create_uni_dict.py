from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from datetime import date
import datetime

large_df = pd.read_html("./uni_data.html",header=0)

have_province = [large_df[1],large_df[3],large_df[5]]
no_province = [large_df[0],large_df[2],large_df[4]]

df_1 = pd.concat(have_province)
df_1 = df_1[['Mã trường','Tỉnh']]

no_province[0]['Tỉnh']='Hà Nội'
no_province[2]['Tỉnh']='Hồ Chí Minh'
no_province[1]['Tỉnh']=no_province[1]['Địa chỉ'].apply(lambda x: "Thừa Thiên Huế" if "Thừa Thiên Huế" in x else "Đà Nẵng")
df_2 = pd.concat(no_province)
df_2 = df_2[['Mã trường','Tỉnh']]

df = pd.concat([df_1,df_2])
#to csv
df.rename(columns={'Mã trường':'code','Tỉnh':'province'},inplace=True)
# save to csv
df.to_csv('./uni_dict.csv',index=False)