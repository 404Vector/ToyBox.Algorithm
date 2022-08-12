import os
import shutil
from turtle import delay

# Define Const
RESULT_PATH = "result/"
SOURCE_PATH = "source/"
COMPILE_DYLIB_COMMAND = 'g++ -arch arm64 --std=c++20 -dynamiclib -o {0} {1}'
COMPILE_TEST_COMMAND = 'g++ -arch arm64 --std=c++20 -o {0} {1} {2}'
#COMPILE_TEST_COMMAND = 'g++ -arch arm64 --std=c++20 source/PermutationT.TEST.cpp result/PermutationT.dylib'

KEYWORD_TEST_FILE = 'TEST'

# Define Function
def IsTestFile(fileName : str):
   fs = fileName.split('.')
   if(len(fs) < 3):
      return False
   else:
      return fs[-2] == KEYWORD_TEST_FILE
   
def FilterSourceFile(fileName : str):
   fs = fileName.split('.')
   if(len(fs) == 2):
      return fs[-1] == 'cpp'
   else:
      return (fs[-1] == 'cpp') and (not IsTestFile(fileName))

def SwapExtension(fileName : str, extension : str):
   return os.path.splitext(os.path.basename(fileName))[0] + extension

# Clear console and result directory
os.system('clear')
os.system("printf '\033[3J'")
print("Clear target directory")
os.system('rm -rf {0}'.format(RESULT_PATH))
delay(2000)

# Start Compile
print("Main Compile start......")
os.makedirs(RESULT_PATH, exist_ok = True)
sources = [f for f in os.listdir(SOURCE_PATH) if (FilterSourceFile(f)) ]
subCompiles = []
for file in sources:
   sourceFilePath = SOURCE_PATH + file
   headerFilePath = SOURCE_PATH + SwapExtension(file, ".h")
   resultFilePath = RESULT_PATH + SwapExtension(file, ".dylib")
   headerFileCopyPath = RESULT_PATH + SwapExtension(file, ".h")
   testSourceFilePath = SOURCE_PATH + SwapExtension(file, "."+KEYWORD_TEST_FILE + ".cpp")
   testResultFilePath = RESULT_PATH + SwapExtension(file, ".out")
   command = COMPILE_DYLIB_COMMAND.format(resultFilePath, sourceFilePath)
   print(" - comfile>> " + command)
   os.system(command)
   shutil.copyfile(headerFilePath, headerFileCopyPath)
   print(" - copy file>> {0} to {1}".format(headerFilePath, headerFileCopyPath))
   if(not os.path.exists(testSourceFilePath)): 
      continue
   subCompiles.append(COMPILE_TEST_COMMAND.format(testResultFilePath, testSourceFilePath, resultFilePath))
print("Main Compile end......")
print("Sub Compile start......")
for command in subCompiles:
   print(" - comfile>> " + command)
   os.system(command)
print("Sub Compile end......")

