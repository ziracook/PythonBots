# div id="ember603"
# div id="ember663"

import urllib
import urllib.request
import random
import time
import sys

url = "https://squareup.com/market/tacocat4u/"
secondsBetweenChecks = 60

def getHtmlFromUrl(webpageUrl):
    randomAgent = random.randint(0,7)

    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
    ]

    urlOpener = urllib.request.build_opener()
    urlOpener.addheaders = [('User-agent', user_agents[randomAgent])]
    html = urlOpener.open(url).read()
    return html

def htmlLengthEqual(htmlOld, htmlNew):
    print("Old length: " + str(len(htmlOld)) + " New length: " + str(len(htmlNew)))
    return len(htmlOld) == len(htmlNew)

def htmlBytesLengthEqual(htmlOld, htmlNew):
    print("Old bytes: " + str(sys.getsizeof(htmlOld)) + " New bytes: " + str(sys.getsizeof(htmlNew)))
    return sys.getsizeof(htmlOld) == sys.getsizeof(htmlNew)

def htmlAreEqual(htmlOld, htmlNew):
    return htmlLengthEqual(htmlOld, htmlNew)


def main():
    #html = urllib.request.urlopen(url).read()
    html = getHtmlFromUrl(url)
    
    while 1:
        tempHtml = getHtmlFromUrl(url)
        if htmlAreEqual(html, tempHtml):
            print("No change")
        else:
            print ("**** THE WEBPAGE CHANGED ****")
            html = tempHtml
        time.sleep(secondsBetweenChecks)


main()