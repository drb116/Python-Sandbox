import json
import urllib.request
import textwrap

def parks_call(url):
    webURL = urllib.request.urlopen(url)
    data = json.loads(webURL.read())
    #encoding = webURL.info().get_content_charset('utf-8')
    return data["data"] #Returns just the data array


def main():
    base_url="https://developer.nps.gov/api/v1/parks?api_key="
    option = input("Do you want to search on (S)tate or (K)eyword? ")
    if option.lower() == "s":
        search_term = input("Please enter a state to search in: ")
        parks = parks_call(base_url + "&stateCode=" + search_term)
    else:
        search_term = input("Please enter a term to search on: ")
        parks = parks_call(base_url + "&q=" + search_term)


    i=0
    if len(parks) > 0:
        for park in parks:
            print(str(i+1) + ": " + park["fullName"])
            i +=1

        selection = int(input("Select a number to get more information --> "))
        wrapper = textwrap.TextWrapper(width=100)
        print(wrapper.fill(parks[selection-1]["description"]))
    else:
        print("** No Results Found **")

if __name__ == "__main__":
    while True:
        main()
        again = input("Would you like to search again? (Y or N)")
        if again.lower() != "y":
            break
