#!/usr/bin/env python 
 
from subprocess import Popen, PIPE
import os



def searchdirectory(stdout,root,count,filename):
	for i in stdout:
		#print "1->%s"%count
		
		count=count+1
		if (os.path.isdir(root+i+'/')):
			
			path=root+i+'/'
			#print "Changing directory form %s to %s"%(root,path)
			os.chdir(path)
			process=Popen(['ls'],stdout=PIPE,stderr=PIPE)
			stdoutput,stderror=process.communicate()
			stdoutput=stdoutput.split()
			searchdirectory(stdoutput,path,count,filename)
		#print "File name=%s"%i
		else :
		  if filename in i:
			print "File found at path :",root+i+'/'
			#process=Popen(['gedit',root+"/"+i],stdout=PIPE,stderr=PIPE)
			#process.communicate()
			break
		

		
	return count


 
process = Popen(['ls'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
#print stdout

stdout=stdout.split()

#print stdout

path="/home/sandeep/SPCC/"

os.chdir(path)

process=Popen(['ls'],stdout=PIPE,stderr=PIPE)
stdout, stderr = process.communicate()
#print stdout

stdout=stdout.split()
#print stdout
count=0

filename=raw_input("Enter the name of the file you are searching for")

count=searchdirectory(stdout,path,count,filename)

print "The no of files is %s"%count


		













