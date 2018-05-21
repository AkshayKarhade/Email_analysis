# Email_analysis
This is a very basic analysis of hypothetical data of Email logs. 

INTRODUCTION:

The given data is taken from one of the online courses I have just completed. This was one of the assignments. 

DATA:

The dataset Emails.csv contains the following columns:

0) Id 
1) RawText
2) DocNumber 
3) ExtractedTo
4) MetadataSubject 
5) ExtractedFrom
6) MetadataTo 
7) ExtractedCc
8) MetadataFrom 
9) ExtractedDateSent
10) SenderPersonId 
11) ExtractedCaseNumber
12) MetadataDateSent 
13) ExtractedDocNumber
14) MetadataDateReleased 
15) ExtractedDateReleased
16) MetadataPdfLink 
17) ExtractedReleaseInPartOrFull
18) MetadataCaseNumber 
19) ExtractedBodyText
20) MetadataDocumentClass 
21) ExtractedSubject

QUESTION:

Find out who are the top 3 people emailing Hillary Clinton.

PROCESS:

Step 1: Clean the data and filter people who mailed Hillary.
Step 2: Use reducer to count the number of times a particular person have mailed Hillary.
Step 3: Finally display the top 3 people who mailed Hillary.

FINAL OUTPUT:

('"Abedin', 1255)	
('"Mills', 1081)	
('"Sullivan', 765)
