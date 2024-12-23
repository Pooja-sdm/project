import streamlit as st
def suggest_crop(moisture, temperature, ph):
    if 12<= moisture <=14  and  25<= temperature <=35 and  5.5<= ph <=7.0 :
        return "Rice","C:\\Users\\user\\Downloads\\rice.jpeg"
    elif 15<=moisture<=22 and 6<=ph<=7 and 14<=temperature<=18:
        return "wheat","C:\\Users\\user\\Downloads\\wheat.jpeg"
    elif 18 <= moisture <= 24 and 6 <= ph <= 7.5 and 21 <= temperature <= 27:
        return "Maize","C:\\Users\\user\\Downloads\\corn.jpeg"
    elif 28 <= moisture <= 32 and 5.5 <= ph <= 8 and 21 <= temperature <= 27:
        return "Sugar cane","C:\\Users\\user\\Downloads\\sugarcane.jpeg"
    elif 6.5 <= moisture <= 8 and 5 <= ph <= 7.5 and 18 <= temperature <= 30:
        return "COtton","C:\\Users\\user\\Downloads\\cotton.jpeg"
    elif 38 <= moisture <= 40 and 6 <= ph <= 6.5 and 27 <= temperature <= 30:
        return "Ground nut","C:\\Users\\user\\Downloads\\groundnut.jpeg"
    elif 13 <= moisture <= 15 and 6.5<= ph <= 7.5 and 26 <= temperature <= 30:
        return "Soya bean","C:\\Users\\user\\Downloads\\soybean.jpeg"
    elif 9 <= moisture <= 10 and 6.5 <= ph <= 7.5 and 15 <= temperature <= 25:
        return "Mustard","C:\\Users\\user\\Downloads\\mustard.jpeg"
    elif 70 <= moisture <= 80 and 4.8 <= ph <= 7.4 and 20 <= temperature <= 25:
        return "Potato","C:\\Users\\user\\Downloads\\potato.jpeg"
    elif 45 <= moisture <= 60 and 6.5 <= ph <= 7.5 and 21 <= temperature <= 24:
        return "Tomato","C:\\Users\\user\\Downloads\\tomato.jpeg"
    elif 83 <= moisture <= 92 and 5.5 <= ph <= 6.5 and 13 <= temperature <= 24:
        return "Onion","C:\\Users\\user\\Downloads\\onion.jpeg"
    elif 48 <= moisture <= 60 and 6 <= ph <= 7 and 15 <= temperature <= 20:
        return "Carrot","C:\\Users\\user\\Downloads\\carrot.jpeg"
    elif 90 <= moisture <=94  and 5.5 <= ph <=6.5 and 15 <= temperature <= 20:
        return "Cabbage","C:\\Users\\user\\Downloads\\cabbage.jpeg"
    elif 8 <= moisture <= 18 and 6 <= ph <= 7.5 and 10 <= temperature <= 18:
        return "Peas","C:\\Users\\user\\Downloads\\peas.jpeg"
    elif  50<= moisture <=70  and  6<= ph <=6.8  and  21<= temperature <= 30:
        return "Ladies Finger","C:\\Users\\user\\Downloads\\ladiesfinger.jpeg"
    elif 91.5<= moisture <=92 and 6 <= ph <=6.8 and 20<= temperature <=30:
        return "Brinjal","C:\\Users\\user\\Downloads\\brinjal.jpeg"
    elif 79<= moisture <=81 and 6.5<= ph <=7.5 and 21<= temperature <=26:
        return "Cucumber","C:\\Users\\user\\Downloads\\cucumber.jpeg"
    elif  60<= moisture <= 80 and 6.5 <= ph <= 7.5 and  18<= temperature <=35 :
        return "Watermelon","C:\\Users\\user\\Downloads\\watermelon.jpeg"
    elif  65<= moisture <=70  and  5.5 <= ph <= 7.5 and  15 <= temperature <=25 :
        return "Mango","C:\\Users\\user\\Downloads\\mango.jpeg"
    elif  75<= moisture <=77  and  5.5<= ph <=7.5  and  15<= temperature <=35 :
        return "Banana","C:\\Users\\user\\Downloads\\banana.jpeg"
    elif 82<= moisture <=83 and 4.5<= ph <=8.2 and 15<= temperature <=30:
        return "Guava","C:\\Users\\user\\Downloads\\guava.jpeg"
    elif 60<= moisture <=80 and 6.5<= ph <=7.5 and 10<= temperature <=20:
        return "Grape","C:\\Users\\user\\Downloads\\grape.jpeg"
    elif 92<= moisture <=94 and 5.5<= ph <=6.5 and 15<= temperature <=25:
        return "Cauliflower","C:\\Users\\user\\Downloads\\cauliflower.jpeg"
    elif 60<= moisture <=80 and 6.5<= ph <=7.5 and 20<= temperature <=30:
        return "Chilli","C:\\Users\\user\\Downloads\\chilli.jpeg"
    elif 80<= moisture <=96 and 6.1<= ph <=7.0 and 20<= temperature <=35:
        return "Pumpkin","C:\\Users\\user\\Downloads\\pumpkin.jpeg"
    elif 40<= moisture <=50 and 6.1<= ph <=7 and 18<= temperature <=24:
        return "Mint","C:\\Users\\user\\Downloads\\mint.jpeg"
    elif 84<= moisture <=85 and 2<= ph <=3 and 20<= temperature <=35:
        return "Lemon","C:\\Users\\user\\Downloads\\lemon.jpeg"
    elif 60<= moisture <=80 and 5.5<= ph <=6.5 and 21<= temperature <=24:
        return "Apple","C:\\Users\\user\\Downloads\\apple.jpeg"
    elif 80<= moisture <=82 and 6.5<= ph <=7 and 15<= temperature <=32:
        return "Pomogranate","C:\\Users\\user\\Downloads\\pomo.jpeg"
    elif 60<= moisture <=80 and 6.5<= ph <=7.5 and 10<= temperature <=35:
        return "Orange","C:\\Users\\user\\Downloads\\orange.jpeg"
    elif 75<= moisture <=80 and 5.5<= ph <=6.5 and 20<= temperature <=35:
        return "Custard Apple","C:\\Users\\user\\Downloads\\custard apple.jpeg"
    elif 20<= moisture <=60 and 5.5<= ph <=7.5 and 20<= temperature <=40:
        return "Ragi","C:\\Users\\user\\Downloads\\ragi.jpeg"
    elif 20<= moisture <=60 and 6.5<= ph <=7.5 and 15<= temperature <=20:
        return "Barley","C:\\Users\\user\\Downloads\\barley.jpeg"
    elif 15<= moisture <=20 and 5.3<= ph <=5.5 and 24<= temperature <=35:
        return "JackFruit","C:\\Users\\user\\Downloads\\jack.jpeg"
    elif 85<= moisture <=95 and 6<= ph <=7 and 18<= temperature <=25:
        return "Dragon Fruit","C:\\Users\\user\\Downloads\\dragan.jpeg"
    elif 9.5<= moisture <=10 and 6.5<= ph <=7.8 and 25<= temperature <=30:
        return "Urad Dal","C:\\Users\\user\\Downloads\\urad.jpg"
    elif 90<= moisture <=91 and 6.5<= ph <=7 and 10<= temperature <=22:
        return "Spinach","C:\\Users\\user\\Downloads\\spanich.jpeg"
    elif 69<= moisture <=70 and 5.5<= ph <=7.5 and 26<= temperature <=37:
        return "Curry leaves","C:\\Users\\user\\Downloads\\curry.jpg"
    elif 10<= moisture <=15 and 4.5<= ph <=8 and 20<= temperature <=30:
        return "Corriender","C:\\Users\\user\\Downloads\\corriander.jpeg"
    elif 60<= moisture <=70 and 7<= ph <=7.5 and 18<= temperature <=20:
        return "Marrie Gold","C:\\Users\\user\\Downloads\\marigold.jpeg"
    elif 72<= moisture <=75 and 6.5<= ph <=7.5 and 10<= temperature <=15:
        return "Jasmine","C:\\Users\\user\\Downloads\\jasimine.jpeg"
    elif 90<= moisture <=94 and 6<= ph <=6.5 and 20<= temperature <=32:
        return "Ivy Gourd","C:\\Users\\user\\Downloads\\ivy.jpeg"
    elif 45<= moisture <=55 and 6<= ph <=6.5 and 15<= temperature <=28:
        return "Coffee Bean","C:\\Users\\user\\Downloads\\coffee.jpeg"
    elif 29<= moisture <=31 and 4.54<= ph <=5.5 and 15<= temperature <=28:
        return "Tea Leaves","C:\\Users\\user\\Downloads\\tea.jpg"
    elif 20<= moisture <=60 and 6<= ph <=7 and 15<= temperature <=19:
        return "Raddish","C:\\Users\\user\\Downloads\\radish.jpeg"
    elif 4<= moisture <=6 and 4.5<= ph <=8 and 30<= temperature <=40:
        return "Cocoa Pod","C:\\Users\\user\\Downloads\\choco.jpg"
    elif 75<= moisture <=80 and 5.5<= ph <=6.5 and 23<= temperature <=32:
        return "Black Pepper","C:\\Users\\user\\Downloads\\black.jpeg"
    elif 39<= moisture <=41 and 5.8<= ph <=6.8 and 25<= temperature <=30:
        return "Capsicum","C:\\Users\\user\\Downloads\\capsicum.jpeg"
    elif 6<= moisture <=12 and 6<= ph <=7 and 13<= temperature <=16:
        return "Hazelnut","C:\\Users\\user\\Downloads\\hazelnut.jpeg"
    elif 95<= moisture <=96 and 5.5<= ph <=6.5 and 21<= temperature <=35:
        return "Star Fruit","C:\\Users\\user\\Downloads\\star.jpeg"
    elif 64<= moisture <=65 and 5<= ph <=7 and 20<= temperature <=28:
        return "Avacado","C:\\Users\\user\\Downloads\\avacado.jpeg"
    elif 91<= moisture <=93 and 4.5<= ph <=7.5 and 20<= temperature <=35:
        return "Turmeric","C:\\Users\\user\\Downloads\\termaric.jpeg"
    elif 41<= moisture <=56 and 6.4<= ph <=7 and 22<= temperature <=32:
        return "Coconut","C:\\Users\\user\\Downloads\\coconut.jpeg"
    elif 95<= moisture <=96 and 6.5<= ph <=7.5 and 24<= temperature <=31:
        return "Ash Gourd","C:\\Users\\user\\Downloads\\ash.jpeg"
    elif 9.3<= moisture <=32.1 and 6<= ph <=7 and 24<= temperature <=27:
        return "Bitter Gourd","C:\\Users\\user\\Downloads\\bitter.jpeg"
    elif 60<= moisture <=63 and 6<= ph <=7 and 12<= temperature <=18:
        return "Garlic","C:\\Users\\user\\Downloads\\garlic.jpeg"
    elif 10<= moisture <=14 and 5.5<= ph <=7 and 25<= temperature <=29:
        return "tapioca","C:\\Users\\user\\Downloads\\tapioca.jpeg"
    elif 80<= moisture <=85 and 6.5<= ph <=7 and 35<= temperature <=38:
        return "Papaya","C:\\Users\\user\\Downloads\\papaya.jpeg"
    elif 74.5<= moisture <=75 and 6<= ph <=7.5 and 25<= temperature <=35:
        return "Drumstick","C:\\Users\\user\\Downloads\\drum.jpeg"
    elif 89<= moisture <=90 and 6.5<= ph <=7.5 and 22<= temperature <=32:
        return "Muskmelon","C:\\Users\\user\\Downloads\\muskmelon.jpeg"
    elif 77<= moisture <=83 and 6<= ph <=8 and 10<= temperature <=38:
        return "Chikku","C:\\Users\\user\\Downloads\\chiku.jpeg"
    elif 0.0<= moisture <=1 and 5.5<= ph <=7 and 25<= temperature <=50:
        return "Rubber","C:\\Users\\user\\Downloads\\rubber.jpeg"
    elif 22<= moisture <=24 and 5.5<= ph <=6.8 and 15<= temperature <=40:
        return "Tamrind","C:\\Users\\user\\Downloads\\tamrind.jpeg"
    elif 5.82<= moisture <=10 and 5.5<= ph <=7 and 20<= temperature <=30:
        return "Cinnamon","C:\\Users\\user\\Downloads\\cinnamon.jpeg"
    elif 85<= moisture <=87 and 5.5<= ph <=6.5 and 20<= temperature <=30:
        return "Elaichi","C:\\Users\\user\\Downloads\\elaichi.jpeg"
    elif 8<= moisture <=13 and 5.5<= ph <=6.5 and 20<= temperature <=30:
        return "Clove","C:\\Users\\user\\Downloads\\clove.jpeg"
    elif 8.9<= moisture <=9.2 and 4.5<= ph <=5 and 24<= temperature <=28:
        return "Cashew","C:\\Users\\user\\Downloads\\cashew.jpeg"
        return "No suitable crop found for the given conditions", None
def home_page():
    st.title("Welcome to Crop Suggestion App")
    st.header("Expert Guidance for Optimal Crop Selection")
    st.write("Get personalized crop recommendations based on your local climate conditions.")
    st.write("\n")
    st.write("# How it Works")
    st.write("1. *Enter Your Soil Data*: Input your soil's moisture, temperature, and pH levels.")
    st.write("2. *Get Expert Advice*: Our algorithm suggests the most suitable crop for your soil conditions.")
    st.write("\n")
    st.write("# Benefits")
    st.write("- *Maximize Yields*: Optimize crop selection for your soil conditions.")
    st.write("- *Reduce Waste*: Minimize crop failures due to unfavorable soil conditions.")
    st.write("- *Increase Efficiency*: Make data-driven decisions for your farming needs.")
    st.write("\n")
    st.write("# Get Started")
    st.write("Enter your soil data below to receive your personalized crop suggestion.")
st.title ("Soil Symphony")
st.write("Enter the values for moisture, temperature, and pH to find the most suitable crop.")

moisture = st.number_input("Enter moisture level (%)", min_value=0.0, step=0.1)
temperature = st.number_input("Enter temperature (°C)", min_value=0.0, step=0.1)
ph = st.number_input("Enter soil pH level", min_value=0.0, max_value=14.0, step=0.1)

if st.button("Show Result"):
    crop, image_path = suggest_crop(moisture, temperature, ph)
    if image_path:
        st.success(f"The most suitable crop is: {crop}")
        st.image(image_path, caption=crop)
    else:
        st.error(crop)
page = st.sidebar.selectbox("Choose a page", ["Home Page", "Result Page"])

if page == "Home Page":
    home_page()
elif page == "Result Page":
    suggest_crop(moisture,temperature,ph)