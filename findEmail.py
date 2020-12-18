from functions import binarySearch_iter, analyze, generateEmails

# add domains to list for additional email extensions
listOfDomains = ['youexample.com','meexample.com','example.com']

# generate emails
emails = generateEmails(10, listOfDomains, 1000000)

# Test email to add to list of emails, followed by appending it to the list of emails
email = 'brianaster@thisexample.com'
emails.append(email)

# Sort the list of generated emails
sortedEmails = sorted(emails)

# Run binarySearch to find test  email in sorted list of emails
index, found = binarySearch_iter(email, sortedEmails)

# Print the result from the search
print(found)

# Print the index returned by the function
if index: print(f"element at index: {index} is {sortedEmails[index]}")

# run analysis of functions
analyze(binarySearch_iter, email, sortedEmails)
analyze(generateEmails, 10, listOfDomains, 1000000)
