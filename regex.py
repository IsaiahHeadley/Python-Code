import re
import pyperclip
#regex for phone numbers

phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000, 555-0000 ext12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d)))?    # area code (optional)
(\s|-)   #first seperator
\d\d\d   #first 3 digits
-      #seperator
\d\d\   # last 4 digits
(((ext(\.)?\s |x)         #extension wrd (optional)
(\d{2,5}))?                #extension number (optional)
)
''', re.VERBOSE)
#regex for email addresses

emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

 [a-zA-Z0-9_.+]+    # name part
@                   # @symbol
[a-zA-Z0-9_.+]+     # domain part

''', re.VERBOSE)

#get text from clipboard
text = pyperclip.paste()

#get email/phone from text on clipboard
extractedPhone = phoneRegex.findall(text) 
extractedEmail = emailRegex.findall(text) 

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.apped(phoneNumber[0])

#copy email/phonenumber to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' +'\n'.join(extractedEmail)
pyperclip.copy(results)