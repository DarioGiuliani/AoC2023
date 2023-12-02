class FileReader:
    def readFile(fileName):
        fileLocation = "input/{}"

        file = open(fileLocation.format(fileName))
        data = file.readlines()
        file.close()
        return data
        