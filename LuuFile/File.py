def saveFile(path):
    file = open(path, 'a', encoding='utf-8')
    file.writelines('Hello\n')
    file.writelines('Hi\n')
    file.close()

saveFile('doc.txt')