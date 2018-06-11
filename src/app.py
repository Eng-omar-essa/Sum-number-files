import glob

class ReadingFileData():
    '''
    This ReadingFiles class , it used to read sets of file and sum number of all files.
    '''
    sumTotalNumber = []
    path = "*.txt"
    textFiles = []
    lines = []
    refFiles = []

    def getTotalNumber(self):
        files = self.getListOfFiles()
        for file in files:
            lines = self.readFile(file)
            for value in lines:
                if value.isdigit():
                    self.sumTotalNumber.append(int(value))
                else:
                    self.readFile(value)

        total = sum(self.sumTotalNumber)
        return total

    def getListOfFiles(self):
        '''
        This function get list of files, it is return list of files.
        '''
        textFiles = glob.glob(self.path)
        return textFiles

    def readFile(self , filenName):
        '''
        This method responsable read file and return list of value.
        '''
        try:
            f = open(filenName,'r')
            lines = f.readlines()
            lines= list(map(lambda x:x.strip(),lines))
            return lines
        except IOError as e:
            print ("I/O error")
        finally:
            f.close()


if __name__ == "__main__":
    readData = ReadingFileData()
    readData.getTotalNumber()
