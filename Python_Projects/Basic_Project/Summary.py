# So in order to keep the techniques learned fresh, I think that it's best to create a seperate project that has all of them in it
# This will NOT have copied code, but will have the topics and commands learned in it

# A place to import things
import sys
# Going to start with the version of python 
print("Hello, welcome to the Learning Summary Project! \nWe're currently Running on version: "+str(sys.version))
# String Manipulation
FullName = input("Please enter your first and last name: ")
FirstName, LastName = FullName.split()
print("Ah yes of course, " + str(LastName)+ ", " + str(FirstName) + "!\n")
Mood = input("How are you doing today?: ")
print("Hmmm.... \n")
# Pick Object from list
# Pick Object from comma seperate values
FriendsInput = input("So tell me about your friends, who would you say are your top 3? (separate with commas): ")
FriendsList = FriendsInput.split(",")
# Specific Format of Output Text
BlackmailInput = input("\nOk so here's a fun question, why is "+FriendsList[2]+
                       " at the bottom of the list? Why are the other two, "+FriendsList[0]+" and "+FriendsList[1]+", higher on your list?: ")
print("Good to know...\n\nSend to: "+FriendsList[0]+"@gmail.com; "+FriendsList[1]+"@gmail.com; "+FriendsList[2]+"@gmail.com;\n\nDear "+
      FriendsList[0]+" "+FriendsList[1]+" "+FriendsList[2]+"\n\nThis is an automated email to let everyone know what's going on!\nSo it would appear"+ 
      "that this is what "+FirstName+" thinks of you:\n\t"+BlackmailInput+"\n\nwhich I just thought was fascinating, don't you?\n\n"+
      "Kind Regards,\n\nPythonAutomationService")
YesNo = input("\nReady to send?: ")
print("I'm just messing with you lol\n\nSo I can also do other things you know\n\n")
# File Identification
File = input("For example I can take file names and tell you what the file type is!\nFor example if you say CV.pdf, I can tell you that that's a pdf"
             "\nType in a file, making sure to include the extension: ")
FileSplit = File.split(".")
FileType = FileSplit[1]
print("So that's a "+str(FileType)+" File\nCool right?!")