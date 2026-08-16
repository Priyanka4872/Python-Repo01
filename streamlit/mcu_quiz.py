import streamlit as st
st.title("my codeee...")
questions=[
    {
        "question":"How Many Infinity stones are there?",
        "options":["Five","Ten","Six","Four"],
        "answer":"Six"
    },
    {
        "question":"What type of doctor is Doctor Strange?",
        "options":["Psychologist","Dentist","Cardiologist","Neurosurgeon"],
        "answer":"Neurosurgeon",
    },
         
    {
        "question":"What is the name of the organization Nick Fury works for?",
        "options":["HYDRA","S.W.O.R.D.","S.H.I.E.L.D.","A.I.M."],
        "answer":"S.H.I.E.L.D.",
    },
    {
        "question":"What fake name does Natasha Romanoff use when she first meets Tony Stark in Iron Man 2?",
        "options":["Natalie Porter","Natasha Rush","Natalie Rushman","Natalie Rogers"],
        "answer":"Natalie Rushman",
    },
    {
        "question":"What is the name of the mysterious planet where the Soul Stone is located?",
        "options":["knowhere","Sakaar","Vormir","Xandar"],
        "answer":"Vormir",
    },
    {
        "question":"What species is Groot?",
        "options":["Sentient Shrub","Flora Colossus","Plant Titan","Wood Elf"],
        "answer":"Flora Colossus",
    },
]

if "question_number" not in st.session_state:
    st.session_state.question_number=0
if "score" not in st.session_state:
    st.session_state.score=0
if "answered" not in st.session_state:
    st.session_state.answered=False

st.title("MCU Quiz!")

if st.session_state.question_number<len(questions):
   current=questions[st.session_state.question_number]

st.subheader(current["question"])
select=st.radio(

    "Options:",
    (current["options"]))

col1, col2 = st.columns(2)

with col1:
 if st.button("Confim"):
   if select==current["answer"]:
      st.session_state.score+=1
    #st.success("Correct!...")
   #else:
      #st.warning("Incoorect Answer...")

if st.button("Check Answer"):
    st.session_state.answered= True
    if select!=current["answer"]:
     st.write("Correct Answer:",current["answer"])
    
with col2: 
 if st.session_state.question_number<len(questions)-1:
  if st.button("Next"):
        #if select==current["answer"]:
           #st.session_state.score+=1
    st.session_state.question_number+=1
    st.session_state.answered=False
    st.rerun()

 else:
    st.success("Quiz Completed!")
st.write("Your Score:",st.session_state.score)