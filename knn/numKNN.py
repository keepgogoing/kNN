from numpy import *
from os import listdir
import operator
# /home/zzh/下载/machinelearninginaction/Ch02/testDigits
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('/home/zzh/下载/machinelearninginaction/Ch02/trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('/home/zzh/下载/machinelearninginaction/Ch02/trainingDigits/%s' % fileNameStr)
    testFileList = listdir('/home/zzh/下载/machinelearninginaction/Ch02/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in arange(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest =img2vector('/home/zzh/下载/machinelearninginaction/Ch02/testDigits/%s'%fileNameStr)
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print('the classifier came back with:%d,the real answer is:%d'%(classifierResult,classNumStr))
        if(classifierResult!=classNumStr):errorCount+=1.0
    print('the total number of errors is:%d'%errorCount)
    print('the total error rate is:%f'%(errorCount/float(mTest)))
handwritingClassTest()
