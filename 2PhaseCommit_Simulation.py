import time


no = 0


def delay(s):
    for i in range(s):
        print(".")
        print(".")
        time.sleep(1)
class CSite:
    def __init__(self,sites):
        self.sites = sites
        self.status = "idle"
    def check(self):
        print("_______________________________________________________________________________________")
        doneCount = 0
        for i in range(5):
            if self.sites[i].status  == "DONE":
                doneCount += 1
                print("Site No: {} has send DONE Message".format(self.sites[i].siteNo))
                delay(2)
            elif self.sites[i].status == "Not Ready":
                print("Site No: {} has send Not Ready Message".format(self.sites[i].siteNo))
                break
        if doneCount == 5:
            print("Every Site has sent DONE Message")
            print("Sending 'Commit' Message to all sites")
            delay(2)
            self.status = "COMMIT"
            print("Commit Message sent by Controlling Site")
        else:
            print("Sending ABORT message to all site")
            delay(2)
            self.status = "ABORT"
            print("ABORT Message sent by Controlling Site")

class Slave:
    def __init__(self,no):
        self.siteNo = no
        self.status = "idle"

    def sendAck(self):
        print("_______________________________________________________________________________________")
        if cSite.status == "COMMIT":
            print("Site No {} has Committed Transaction".format(self.siteNo))
            print("Site No {} sending Commit ACK to Controlling Site".format(self.siteNo))
            delay(2)
            print("Controlling site has Considered Transaction as Commited")
        elif cSite.status == "ABORT":
            print("Site No {} has aborted Transaction".format(self.siteNo))
            print("Site No {} sending Abort ACK to Controlling Site".format(self.siteNo))
            delay(2)
            print("Controlling site has Considered Transaction as Aborted")
        self.status = "idle"
    def ready(self):
        print("Site No {} is excuting transaction .....".format(self.siteNo))
        delay(2)
        print("Execution Completed")
        self.status = "DONE"
        print("Sending 'DONE' Message to Controlling Site")
        delay(2)
        print("DONE Message Sent by Site: {}".format(self.siteNo))
        print("_______________________________________________________________________________________")
    def notReady(self):
        print("Site {} is Not ready".format(self.siteNo))
        print("Sending 'Not Ready' Message to Controlling Site")
        self.status = "Not Ready"
        delay(2)
        print("Not Ready Message Sent by Site: {}".format(self.siteNo))
        print("_______________________________________________________________________________________")


def ack():
    for i in range(5):
        _sites[i].sendAck()
    cSite.status = "idle"
def abort():
    print("***********************_| Phase 1: Prepare Phase |_************************************")
    print("Operation at Salve side")
    for i in range(4):
        _sites[i].ready()
    _sites[4].notReady()
    print("***********************_| Phase 2: Commit / Abort Phase |_*****************************")
    print("Operation at Controlling Site")
    cSite.check()
    ack()
def commit():
    print("***********************_| Phase 1: Prepare Phase |_************************************")
    print("Operation at Salve side")
    for i in range(5):
        _sites[i].ready()
    print("***********************_| Phase 2: Commit / Abort Phase |_*****************************")
    print("Operation at Controlling Site")
    cSite.check()
    ack()



_sites = []
for i in range(5):
    _sites.append(Slave(i+1))
cSite = CSite(_sites)



while True:
    print("----Perform Operation----")
    print("\n 1. Simulate Commit\n 2. Simulate Abort\n 3. Exit")
    q = int(input("Enter option: \n"))
    if q == 3:
        break
    if q == 1:
        commit()
    elif q == 2:
        abort()
    else:
        print("Invalid Input")