def scrap_ad_data(ad_url):
    r = requests.get(ad_url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    target_component = soup.findAll("h1")
    # create a list that will hold our component data
    results = []
    for i in target_component:
        results.append(''.join(i.find(text=True)).replace('\n',''))
    return results


def write_data_to_csv(data):
    with open("D:/Python_CSV/phones_output1.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
# read the saved urls file as a dataframe 
urls_data = pd.read_csv("D:/Python_CSV/urls.csv")
# create  a list that will hold the final data
final_result = []
i = 1
# loop over the dataframe
for index, row in urls_data.iterrows():
    final_result.append(scrap_ad_data(row['url']))
    # to count how many page we have processed since qe have 35 links per page
    #i += 1
    #if i%100 == 0:
    #    print("page ",i, "done")
print('Scrapping data finished')
# now that we have all the data we can write it in a csv file
write_data_to_csv(final_result)
