# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 
import streamlit as st
import requests
import difflib


df = pickle.load(open('df_new.pkl','rb'))
cosine = pickle.load(open('cosine.pkl','rb'))
list_of_all_titles = df['course_name'].tolist()
#print(list_of_all_titles)
def recommend(course_name):
    #print ('course name is '  + course_name)

    find_close_match = difflib.get_close_matches(course_name, list_of_all_titles,n = 4,cutoff = 0.3)
   

    close_match = find_close_match[0]
    #print("close match is" + close_match)

    df[df.course_name == close_match]

# finding the index of the course with title
    index_of_the_course = df[df.course_name == close_match]['index'].values[0]
    #print(index_of_the_course)
# getting a list of similar names
    similarity_score = list(enumerate(cosine[index_of_the_course]))
    #print(similarity_score) 
# sorting the names based on their similarity score
    sorted_similar_courses = sorted(similarity_score, key = lambda x:x[1], reverse = True)
# [1:] 
    #print(sorted_similar_courses)
    print('courses suggested for you : \n')

    i = 1
    title_from_index_list = []
    for course in sorted_similar_courses:
        if i<11:
            index = course[0]
            title_from_index = df[df.index==index]['course_name'].values[0]
            title_from_index_list.append(title_from_index)
            i+=1
    return  title_from_index_list

       
def main():  
    # front end elements of the web page 
    html_temp = """ 
<div style ="background-color:yellow;padding:13px"> 
<h1 style ="color:black;text-align:center;">Course Recommendation Model</h1> 
</div> 
"""
  
# display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    course_name = st.text_input("Enter course name")  
 
            
    if st.button("Recommend Courses"): 
        try:
           if len(course_name) == 0:
             st.error("please enter input")
        except IndexError:
           st.error("please enter input")
        answer = recommend(course_name) 
        st.success('Your recommended courses are')
       #row1, row2, row3, row4, row5 = st.columns(5)
    k=0
    
    try:
        while(k<5):
                st.write(answer[k])
                k=k+1
    except Exception:
        print("all the receommendations listed")

            
       #with row1:
           #st.text_area(result[0])
           #st.image(recommended_movie_posters[0])
       #with row2:
            #st.text_area(result[1])
            #st.image(recommended_movie_posters[1])

       # with row3:
       #      st.text_area(result[2])
       #      #st.image(recommended_movie_posters[2])
       # with row4:
       #  st.text_area(result[3])
       #  #st.image(recommended_movie_posters[3])
       # with row5:
       #  st.text_area(result[4])
        #st.image(recommended_movie_posters[4])
        
       
if __name__=='__main__': 
    main()       