from threading import Thread, Lock, Condition
import shelve

#TODO: make this class multi-thread safe
class Database(object):
    def __init__(self,filename):
        self.lock = Lock()
        self.database = shelve.open(filename,writeback=True)

    #saves database dict in filename
    def saveDatabase(self):
        self.database.sync()

#TODO: make multi-thread safe + write: formatText, isNegStatusChange, saveInfo
class VitalDataHandler(Thread):
    def __init__(self,patientDb,nurseDb,dataInput,handlerId):
        self.patientDb = patientDb
        self.nurseDb = nurseDb
        self.dataInput = dataInput
        self.handlerId = handlerId

    #converts status to int
    def intStatus(self,status):
        return {'stable':1,'intermediate':0,'critical':-1}[status]

    #Formats and returns the the text that will be sent out
    #inputs: String patientId, String location, String status
    def formatText(self,patientId,location,status):
        pass

    #checks database.db if there is a negative status change in the patient
    #returns false if the patient does not exist in the database
    #possible statuses: "stable","intermediate","critical"
    def isNegStatusChange(self,patientId,location,status):
        pass

    #sends text from pi to nurses
    def sendText(self,msg):
        pass

    #saves all info in a database.db
    #KEY: patientId+location; VAL: status
    def saveInfo(self,patientId,location,status):
        pass

    #thread's main function
    def run(self):
        pass

#TODO: make thread safe + addPhoneNum
class NurseHandler(Thread):
    def __init__(self,nurseDb):
        self.nurseDb = nurseDb

    #adds KEY:name, VAL:num to nurseDb and saves to nurseDb
    def addPhoneNum(self,name,num):
        pass

    #wait for external input (commandline text), then add to nurseDb
    def run(self):
        pass

#========================================================================================================
#    Main
#========================================================================================================

if __name__ == "__main__":
    patientDb = Database("patients.db")
    nurseDb = Database("nurses.db")
    dataInputStream = ["p1,bed1,stable","p2,bed5,critical","p3,bed6,intermediate","p1,bed1,critical","p2,bed5,stable","p3,bed6,intermediate","p1,bed1,critical","p2,bed5,intermediate","p3,bed6,critical"]
    NurseHandler(nurseDb).start()
    for ii in range(9):
        VitalDataHandler(patientDb,nurseDb,dataInputStream[ii],ii).start()
