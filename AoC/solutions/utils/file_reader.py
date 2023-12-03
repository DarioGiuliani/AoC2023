class FileReader:
    def readfile(fileName):
        file_location = "input/{}"

        file = open(file_location.format(fileName))
        data = file.readlines()
        file.close()
        return data
        