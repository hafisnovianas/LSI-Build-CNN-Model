import os
import shutil

sourceFolderPath = 'data\DATA PROTOTIPE\OPLOSAN\CC2'
sourceFolderName = os.path.basename(sourceFolderPath)
dataLatihFolderPath = os.path.join(sourceFolderPath, sourceFolderName + '(data latih)')
dataUjiFolderPath = os.path.join(sourceFolderPath, sourceFolderName + '(data uji)')

os.makedirs(dataLatihFolderPath, exist_ok=True)
os.makedirs(dataUjiFolderPath, exist_ok=True)

for fileName in os.listdir(sourceFolderPath):
    if fileName.endswith('.jpg'):
        filePath = os.path.join(sourceFolderPath,fileName)
        fileNumber = fileName.split('(')[1].split(')')[0]
        if 0 < int(fileNumber) % 10 <= 8:
            shutil.move(filePath, dataLatihFolderPath)
        else:
            shutil.move(filePath, dataUjiFolderPath)
