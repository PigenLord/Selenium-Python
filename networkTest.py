import pychrome
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def output_on_start(**kwargs): 
    print("STARTED ", kwargs) 
def output_on_end(**kwargs): 
    print("Finished ", kwargs) 

 
#defining the chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#setting the remote bug port so we can connect devs tool to our pc 
options.add_argument("--remote-debugging-port=8920")
#installs the latets version of chrome drivers
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
#create a devtools object using the pychrome library and defining the url connects to the local host which is where devtools will be running from
#basically we are telling pychrome (the devtools protocol) to bind the remote debuging port to the same port as the local host. 
dev_tools = pychrome.Browser(url="http://localhost:8920")
#here we are binding it a tab. In this case we binding to the first tab. 
tab = dev_tools.list_tab()[0]
tab.start()

start = time.time()
driver.get("https://fox.com")
print (int(time.time() - start)) 

#this is what is keeping the browser from closing 
while(True): 
    pass
#ChromeDevTools Docs 
tab.call_method("Network.emulateNetworkCondition", 
                offline=False, 
                latency=100, downloadThroughput=93750,  #this is how we simulate network conditions
                uploadThroughput=31250, 
                connectionType="cellular3g")


tab.set_listener("Network.enable", _timeout)
tab.set_listener("Network.requestWillBeSent", output_on_start)
tab.set_listener("Network.responseReceived", output_on_end)

start = time.time()
driver.get("https://fox.com")
print (int(time.time() - start)) 