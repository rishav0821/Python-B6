import pickle

list1= [1,2,3,4,5,6]

fileName= "data.pickle"
#fileHandle= open(fileName,"wb")
#pickle.dump(list1,fileHandle)
#fileHandle.close()
with open(fileName,"wb") as fileHandle:
    pickle.dump(list1,fileHandle)
   
