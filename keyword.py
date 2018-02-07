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
print("The keywords entered in the text are:");
for i in keyword:
	print(i);