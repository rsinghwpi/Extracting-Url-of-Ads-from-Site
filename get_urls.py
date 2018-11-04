import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_urls():
    new_list=[]
    urls_list = []
	# define the root url from where advertisement needs to be captured
    basic_url = "https://www.commonfloor.com/bangalore-property/for-sale/apartment-ht/budget-below-60-lakhs&o="
	# loop over the paginated urls
    for i in range(1):
		# get the page url
        url = basic_url+str(i)
		# get the request response
        r  = requests.get(url)
        data = r.text
		# transform it to bs object
        soup = BeautifulSoup(data, "lxml")
		# loop over page links
        for div in soup.findAll('div', {'class': 'snb-tile-info'}):
            a = div.findAll('a')[0]
            urls_list.append(a.get('href'))
            for b in urls_list:
                oldurl="https://www.commonfloor.com"
                newurl = oldurl+str(b)
                new_list.append(newurl)
    df = pd.DataFrame(data={"url": new_list})
    df.to_csv("D:/Python_CSV/url.csv", sep=',',index=False)

# get the ads urls and save them in a file
get_urls()
