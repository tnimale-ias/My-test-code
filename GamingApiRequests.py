import requests
import random
import threading
import multiprocessing
import time
import platform

gaming_url = "http://gaming-viewability.k8s.dev.303net.net/gaming/ias/v1/viewability"
sentIDs = {}

n = 0


req = requests.session()

def getLoadData(adID):
    params = {}
    params['event'] = 'Load'
    params['aid'] = adID
    params['et'] = int(time.time())
    params['etz'] = time.timezone
    params['model'] = platform.platform()
    params['os'] = platform.system()
    params['osv'] = platform.version()
    params['sdk'] = 'ias'
    params['sdkv'] = '1.0.0'
    params['bid'] = '1920adx'
    params['ad_dom'] = 'sports'
    params['adu_type'] = 'banner'
    params['app_name'] = 'sfg3'
    params['appid'] = 'ab23egw'
    params['placement_id'] = 'ssx'+adID
    params['ad_h'] = 1000
    params['ad_w'] = 1250
    params['sc_w'] = 1750
    params['sc_h'] = 1040
    params['media_type'] = 'image'

    return params






def getImpressionData(adID):
    params = {}
    params['event'] = 'Impression'
    params['aid'] = adID
    params['et'] = int(time.time())
    params['etz'] = time.timezone
    params['chd'] = random.uniform(0, 100)
    params['mchd'] = params['chd']+10
    params['cid'] = random.uniform(0, 100)
    params['mcid'] = params['cid']+10
    params['dd'] = random.random()*10 + 5
    params['asws'] = random.uniform(1.5, 100)
    params['msws'] = random.uniform(15, 100)
    params['asr'] = params['chd']
    params['msr'] = params['mchd']
    params['aaws'] = params['asws']
    params['mxa'] = params['msws']
    params['mna'] = random.uniform(0,55)

    return params





def getUnloadData(adID):
    params = {}
    params['event'] = 'Impression'
    params['aid'] = adID
    params['et'] = int(time.time())
    params['etz'] = time.timezone
    params['chd'] = random.uniform(0, 100)
    params['mchd'] = params['chd']+10
    params['cid'] = random.uniform(0, 100)
    params['mcid'] = params['cid']+10
    params['dd'] = random.random()*10 + 5
    params['asws'] = random.uniform(1.5, 100)
    params['msws'] = random.uniform(15, 100)
    params['asr'] = params['chd']
    params['msr'] = params['mchd']
    params['aaws'] = params['asws']
    params['mxa'] = params['msws']
    params['mna'] = random.uniform(0,55)

    return params



def createImpressionRequest(n, i):

    adID = "ad"+str(random.randint(0, 100000000))

    if adID in sentIDs:
        return

    sentIDs[adID] = 1

    print(adID+ " " + str(n) + " "+str(i))

    #Load event....
    parameters = getLoadData(adID)
    try:
        req.get(gaming_url, params=parameters)
    except:
        pass

    #impression event....
    parameters = getImpressionData(adID)
    try:
        req.get(gaming_url, params=parameters)
    except:
        pass

    #Unload event....
    parameters = getUnloadData(adID)
    try:
        req.get(gaming_url, params=parameters)
    except:
        pass

    return




def runGetThreads(n, ind):
    threadN = 100
    iterations = 100
    while (iterations)>0:

        iterations-=1
        threads = []
        for i in range(threadN):
            n+=1
            tempThread = threading.Thread(target=createImpressionRequest, args=(n,ind, ))
            threads.append(tempThread)
            tempThread.start()


        for thread in threads:
            thread.join()
    return


start_time = time.time()

if __name__ == "__main__":
    processN = 6

    processes = []

    for i in range(processN):
        tempProcess = multiprocessing.Process(target=runGetThreads, args=(n, i, ))
        processes.append(tempProcess)
        tempProcess.start()

    for process in processes:
        process.join()

print("Completion Time: "+str(time.time()-start_time))