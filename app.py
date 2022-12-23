
import pickle
import streamlit as st

pickle_in = open('classifier', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# Define the function which will make the prediction using data
# inputs from users
def prediction(industrial_land, river_side,
               mean_rooms, pupil_teacher_ratio, large_lots):
    
    # Make predictions
    prediction = classifier.predict(
        [[large_lots, industrial_land, river_side, mean_rooms, pupil_teacher_ratio]])
    
    if prediction == 0:
        pred = 'This township is likely to possess a lot of high valued properties. Research further!'
    else:
        pred = 'This township will probably not have a lot of high valued properties. Avoid for residential, but can consider for Industrial projects.'
    return pred

# This is the main function in which we define our webpage
def main():
    
    # Create input fields
    
    large_lots = st.number_input("Residentials lots that are large (%)",
                                  min_value=0,
                                  max_value=100,
                                  value=5,
                                  step=1,
                                 )
    industrial_land = st.number_input("Township land zoned for industrial purposes (%)",
                              min_value=0,
                              max_value=100,
                              value=5,
                              step=1,
                             )

    river_side = st.number_input("Riverside - Yes(1) or No(0)",
                              min_value=0,
                              max_value=1,
                              value=0,
                              step=1
                             )
    mean_rooms = st.number_input("Mean Number of Rooms",
                          min_value=1,
                          max_value=10,
                          value=2,
                          step=1
                         )
    pupil_teacher_ratio = st.number_input("pupil_teacher_ratio",
                          min_value=1,
                          max_value=25,
                          value=10,
                          step=1
                         )

    result = ""
    
    # When 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(large_lots, industrial_land, river_side, mean_rooms, pupil_teacher_ratio)
        st.success(result)
        
if __name__=='__main__':
    main()
