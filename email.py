import csv
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('sponsorships@frontierhacks.org', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("sender_email_id", "receiver_email_id", message) 
  
# terminating the session 
s.quit() 

data = {}

with open('CompanyNames.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data[row[0]] = [row[1], row[2]]

name = "Neeraj"
title = "FrontierHacks Sponsorship Director"
phonenumber = "(111) 111-1111"
website = "https://frontierhacks.com/"
hackathonName = "FrontierHacks"
        
emails = []

for key, values in data.items():
    template = "Dear " + values[1] + ",\n\nHello! I am " + name +  ", " + title + ".\n" 
    template += "On the weekend of September 14, 2019, my team and I will be hosting FrontierHacks, a high school hackathon with a projected 250 person attendance.  At FrontierHacks, students from all over the Bay Area, many of which whom are first-time coders, will come together to solve various issues or problems in their communities with the hopes of making a global impact. FrontierHacks is also a friendly and welcoming environment where teams of new and experienced coders can build a project, learn new skills, and have a great time! Within this period, the hackathon team will serve lunch, dinner, midnight snacks, and drinks. Then judges will evaluate these projects and select a winner for specific criteria such as best AI, best Python program, best educational program, etc."
    template += "\n\n" + "With the tech era being as prominent as ever here in the Silicon Valley, it is increasingly essential to cultivate the passion for computer science amongst the students in my generation. We have noticed the impact of " + key + "'s sponsorship in other similar events, and we hope that you would be interested in monetarily sponsoring FrontierHacks. As a sponsor of our hackathon, your company will be able to form long-lasting impressions of many student developers, and " + key +" will be publicized on our website and our merchandise. However, if you are unable to provide us with monetary help at this time, we would be happy to receive any form of sponsorship " + key + " can offer."
    template += "\n\nIf you are interested, I can email you a copy of our Sponsorship Prospectus. I look forward to following up with you in the next few days and answering any further questions. We would be grateful to arrange a sponsorship deal with you!"
    template += "\n\nSincerely," + "\n" + name + "\n" + title + "\n"+ phonenumber + "\n" + website
    emails.append(template)
