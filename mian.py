# Import
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
# User agent of the website
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

# Access the data of restaurant
def items(response,code):
    x = []
    if response.status_code == code:
        soup = BeautifulSoup(response.text,'html.parser')

        restaurants = soup.find_all('div',class_="styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp")

        for restaurant in restaurants:
            name = restaurant.find('div',class_="sc-beySbM cwvucc").text.strip()
            delivery_time = restaurant.find('div', class_="sc-beySbM gLFbKf").text.strip()
            data = restaurant.find('div',class_="sc-beySbM iTWFZi").text.strip()

            # Save the data using DataFrame in CSV
            li = [name,delivery_time,data]
            x.append(li)
            df = pd.DataFrame(x,columns=["Restaurant Name","Rating & Delivery Time","Cuisine"])
            df.to_csv("mumbai.csv",index=False)

# Main code of environment
def maincode(url):
    response = requests.get(url, headers=header)
    code = response.status_code

    if response.status_code == code:
        soup = BeautifulSoup(response.text, 'html.parser')
    items(response, code)
# Execution of program
if __name__ == "__main__":
    url = f"https://www.swiggy.com/city/mumbai/best-restaurants"
    maincode(url)