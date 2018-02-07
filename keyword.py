"""
Program to input a text and store the keywords in a list and print the keywords.
"""

text=input("Enter the text:");

#Splits the text about spaces
T=text.split(" ");

#This list contains the words to ignore
ignore=[',','.','?',';','!','(',')','-','are','is','then','those','than','for','so','the','if','a','an','there','thus','because'];

#This list contains the keywords
keyword=[];

#Adding the keywords
for i in T:
	if i in ignore:
		pass;
	else:
		keyword.append(i);

#Printing the keywords
print("\nThe keywords entered in the text are:");
for i in keyword:
	print(i);

#Adding more keywords
check=input("\nWant to add more keywords(y/n)?");
if check=='n':
	pass;
else:
	print("\nEnter the keywords(input *stop* to stop entering):");
	temp="initial";
	while temp!= '*stop*' :
		temp=input("-->");
		keyword.append(temp);
    #Removing the last element-->*stop*
	keyword.pop();


#Removing the keywords
rmv=[];
check=input("\nWant to delete any keywords shown?(y/n)?");
if check=='n':
	pass;
else:
	print("\nEnter the keywords to remove(input *stop* to stop entering):");
	temp="initial";
	while temp!= '*stop*' :
		temp=input("-->");
		rmv.append(temp);
    #Removing the last element-->*stop*
	rmv.pop();

#for i in rmv:
	#print(i);

#keywordfinal=keyword;
keywordfinal=[];
for i in keyword:
	if i not in rmv:
			keywordfinal.append(i);


    

#Final list of keywords
print("\nFinal list of keywords are:");
for i in keywordfinal:
	print(i);