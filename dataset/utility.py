import os
import shutil

def copyAllFile(sourceFolderPath,targetFolderPath):
    print(sourceFolderPath)
    for fileName in os.listdir(sourceFolderPath):
        sourceFilePath = os.path.join(sourceFolderPath, fileName)
        shutil.copy2(sourceFilePath, targetFolderPath)
