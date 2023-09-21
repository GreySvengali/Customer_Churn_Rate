import pickle
import sklearn
import numpy as np
import streamlit as st
# To display images
from PIL import Image


#loading the saved model
loaded_model = pickle.load(open('churn_analyser.sav', 'rb'))

#Creating a function for prediction

def churn_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person did not churn'
    else:
        return 'The person churned'


def main():
    # display image
    img = Image.open("Churn.jpeg")
    new_image = img.resize((700, 200))
    st.image(new_image)
    # let's display
    # st.image(img, width=700)

    # giving a title
    st.title('E-Commerce Shopper Churn Rate Prediction Web App')

    # getting the input data from the user

    Tenure = st.text_input('Number of years as Customer')
    LoginDevice = st.text_input('Enter your Login Device: 0 = Mobile Phone , 1: Computer, Feature Phone: 2')
    CityTier = st.text_input('How Close to Lagos Are You? In Kilometres')
    WareHouseToHome = st.text_input('Enter Distance to PickUp Location in Kilometres')
    PreferredPaymentMode = st.text_input('Enter Your Payment Method: 0 = Debit Card, 1 = Credit Card, 2 = E-Wallet, 3 = Cash on Delivery, 4 = UPI')
    Gender = st.text_input('Enter Your Gender: 0 = Male, 1 = Female')
    HourSpendonApp = st.text_input('Enter Your Avg Browse Time in Hours')
    NumberofDevicesRegistered = st.text_input('How Many Devices Did You Register on the App')
    PreferredOrderCat = st.text_input('Enter Your Favourite Shopping Category: 0 = Laptop & Accessory, 1 = Mobile Phone, 2 = Fashion, 3 = Mobile, 4 = Grocery, 5 = Others')
    SatisfactionScore = st.text_input('Rate our Service Delivery from 0 - 20')
    MaritalStatus = st.text_input('Enter Your Marital Status: 0 = Married, 1 = Single, 2 = Divorced')
    NumberofAddress = st.text_input('Enter Total Number of Your Registered Delivery Address')
    Complain = st.text_input('Tell Us How Many Complaints You Have Raised')
    OrderAmountHikeFromlastYear = st.text_input('Enter Number of Orders Made in the Last 1 Year')
    CouponUsed = st.text_input('Enter Number of Coupon Used Since Last Month')
    OrderCount = st.text_input('Enter Number of Orders Made in the Last 1 Month')
    DaySinceLastOrder = st.text_input('How Many Days Ago Was Your Last Order?')
    CashbackAmount = st.text_input('How Much Refund Have You Received In Last Month?')




    # code for Prediction
    churn = ''

    # creating a button for Prediction

    if st.button('Churn Result'):
        churn = churn_prediction([Tenure, LoginDevice, CityTier, WareHouseToHome, PreferredPaymentMode, Gender, HourSpendonApp, NumberofDevicesRegistered,PreferredOrderCat, SatisfactionScore, MaritalStatus, NumberofAddress, Complain, OrderAmountHikeFromlastYear, CouponUsed, OrderCount, DaySinceLastOrder, CashbackAmount])

    st.success(churn)


if __name__ == '__main__':
    main()