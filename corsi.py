
#Importing Dependencies
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle
#print('Dependencies Imported')



data = pd.read_csv("/home/juana/Downloads/Coursera.csv")
#print(data)

#Required Columns for System


data = data[['Course Name','Difficulty Level','Course Description','Skills','Course URL']]


data['Course Name'] = data['Course Name'].str.replace(' ',',')
data['Course Name'] = data['Course Name'].str.replace(',,',',')
data['Course Name'] = data['Course Name'].str.replace(':','')
data['Course Description'] = data['Course Description'].str.replace(' ',',')
data['Course Description'] = data['Course Description'].str.replace(',,',',')
data['Course Description'] = data['Course Description'].str.replace('_','')
data['Course Description'] = data['Course Description'].str.replace(':','')
data['Course Description'] = data['Course Description'].str.replace('(','')
data['Course Description'] = data['Course Description'].str.replace(')','')

#removing paranthesis from skills columns
data['Skills'] = data['Skills'].str.replace('(','')
data['Skills'] = data['Skills'].str.replace(')','')

data['tags'] = data['Course Name'] + data['Difficulty Level'] + data['Course Description'] + data['Skills']



#Dataframe to be used



new_df = data[['Course Name','tags','Course URL']]
#print(new_df.head(5))



new_df['tags'] = data['tags'].str.replace(',',' ')

new_df['Course Name'] = data['Course Name'].str.replace(',',' ')

new_df.rename(columns = {'Course Name':'course_name'}, inplace = True)


new_df['tags'] = new_df['tags'].apply(lambda x:x.lower()) #lower casing the tags column
print(new_df.head(5))



cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()





ps = PorterStemmer()


# defining the stemming function
def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)
new_df['tags'] = new_df['tags'].apply(stem) #applying stemming on the tags column



from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)


def recommend(course):
    course_index = new_df[new_df['course_name'] == course].index[0]
    distances = similarity[course_index]
    course_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    for i in course_list:
        print(new_df.iloc[i[0]].course_name)

#pickle.dump(similarity,open('similarity.pkl','wb'))
#pickle.dump(new_df.to_dict(),open('course_list.pkl','wb')) #contains the dataframe in dict
#pickle.dump(new_df,open('courses.pkl','wb'))
