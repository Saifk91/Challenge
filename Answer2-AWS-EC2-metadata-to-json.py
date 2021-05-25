import requests
import json

def loadjson():
    metaurl = 'http://169.254.169.254/latest'
    # There are three types of data and those 3 subdirectories are not exposed with a '/'
    newUrl = {'dynamic': {}, 'meta-data': {}, 'user-data': {}}
    #Now we need append the metaurl with dynamic, meta-data and user-data one by one to metaUrl and fetch the output
    for SubUrl in newUrl.keys():
        datacrawl('{0}/{1}/'.format(metaurl, SubUrl), newUrl[SubUrl])

    return newUrl


def datacrawl(url, d):
    r = requests.get(url)   #in case the Url is not accessible then fail and take new from above
    if r.status_code == 404:
        return
		#The new url is splitted
    for l in r.text.split('\n'):
        if not l: # "instance-identity/\n" case
            continue
        nesubwurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/', as there are chances the metadata have more files within
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            datacrawl(newsuburl, d[newkey])

        else:
            r = requests.get(newsuburl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None



if __name__ == '__main__':
    print(json.dumps(loadjson()))
@Saifk91
 


