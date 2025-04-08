#tasks=[]
#def add_task(task):
 #   return tasks.append(task)

#def main():
 #   print('1-lisada ülesande \n 2-kustuda ülesande \n 3-ülevaadata ülesanded')
  #  userInput=input("Mida sa tahad?")
   # if userInput=='1':
    #    tasks=add_task(input("sisesta ülesande:"))
    #elif userInput =='2':
     #   pass 
    #elif userInput =='3':
     #   pass 
    #else:
     #   print("sa sisestasid midagi vale")
#main()


import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks=[]

st.title("Todo list")