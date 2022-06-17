import pandas as pd
import numpy as np
uni_dict = pd.read_csv('./uni_dict.csv')
admission_score = pd.read_csv('./admission_score.csv')
pd.merge(admission_score,uni_dict,left_on='university_code',right_on='code').to_csv('./admission_score_with_province.csv',index=False)