import random
import requests


def request_test(domain, location_id, wpt_url):
    params = {'f': 'json', 'url': domain, 'location': location_id}
    request = requests.get("%s/runtest.php" % (wpt_url), params=params)
    return request.json()


if __name__ == "__main__":
    input_file = "sites4.txt"
    output_file = "wptids4.txt"

    sites = open(input_file, "r")
    ids = open(output_file, "w")

    site = sites.readline()
    i = 1
    while site:
        response = request_test(site, "first_wptdriver", "http://3.93.81.121")
        ids.write(str(i+300)) #test_num
        ids.write("\n")
        ids.write(site) #site
        ids.write(response["data"]["testId"]) #wptid
        ids.write("\n")
        site = sites.readline()
        i = i+1
        
    sites.close()
    ids.close()
