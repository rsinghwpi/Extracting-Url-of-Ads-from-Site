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
