from PIL import Image
import streamlit as st


st.title("Quick Update App")
st.header("The Grocery Checker App")
st.subheader("Make grocery shopping a delight")
img = Image.open("groceries.jpg")
st.image(img, width=500)

# select groceries
selected_grocery = st.selectbox(
    "Select Grocery Item", ["Milk", "Eggs", "Vegetables", "Fruits", "Meat"])
st.write("You have selected: ", selected_grocery)

# getting user inputs


def users_response():
    response = st.number_input(
        f"How long have you been using {selected_grocery} ?")

    submission = st.button("Submit")
    if submission == True:

        def output():
            if response < 14:
                st.success("Not yet due for purchase")

            elif response >= 14:
                st.warning("Due for restocking")

        output()


users_response()


# while len(Milk) = 7 days:
#     Milk = input("Choose number of days: [0-7 days]")

#     if less than 14 days
#     print("Not yet due for purchase")

#     else:
#         print("Due for restocking")


# while len(Eggs) = 14 days:
#     Milk = input("choose number of days: [0-14 days]")
#     if < 14:
#         print("Not yet due for restocking")
#     else:
#         print("Due for restocking")
