from bs4 import BeautifulSoup
import requests
import json

# instagram URL
URL = "https://www.instagram.com/{}/"
# parse function
def parse_data(s):
    # creating a dictionary
    data = {}
    # splitting the content
    # then taking the first part
    s = s.split("-")[0]
    # again splitting the content
    s = s.split(" ")
    # assigning the values
    data['UserName'] = username
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    # returning the dictionary
    return data

# scrape function
def scrape_data(username):
    # getting the request from url
    r = requests.get(URL.format(username))
    # converting the text
    s= BeautifulSoup(r.text, "html.parser")
    # finding meta info
    meta = s.find("meta", property="og:description")
    # calling parse method
    return parse_data(meta.attrs['content'])


def write_json(data, filename='data.json'):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)


#main function
if __name__ == "__main__":
    username="satyu.26"
    # calling scrape function
    data = scrape_data(username)
    #storing data into JSON
    fetch = write_json(data)
    # printing the info
    print(data)