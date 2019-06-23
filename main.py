# Python code to illustrate Sending mail from  
# your Gmail account 
import csv 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
  
fromaddr = "email@gmail.org"
password = "password"
name = "Neeraj"
title = "FrontierHacks Sponsorship Director"
phonenumber = "(111) 111-1111"
website = "https://frontierhacks.com/"
hackathonName = "FrontierHacks"
data = {}

with open('test.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data[row[0]] = [row[1], row[2]]
        
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
      
# Authentication 
s.login(fromaddr, password) 
        
for key, values in data.items():
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr
      
    # storing the receivers email address  
    msg['To'] = values[0]
      
    # storing the subject  
    msg['Subject'] = key + " Sponsorship Inquiry"
      
    # string to store the body of the mail 
    body = "Dear " + values[1] + ",\n\nHello! I am " + name +  ", " + title + ".\n\n" 
    body += "On the weekend of September 14, 2019, my team and I will be hosting " + hackathonName + ", a high school hackathon with a projected 250 person attendance.  At " + hackathonName + ", students from all over the Bay Area, many of which whom are first-time coders, will come together to solve various issues or problems in their communities with the hopes of making a global impact. " + hackathonName+ " is also a friendly and welcoming environment where teams of new and experienced coders can build a project, learn new skills, and have a great time! Within this period, the hackathon team will serve lunch, dinner, midnight snacks, and drinks. Then judges will evaluate these projects and select a winner for specific criteria such as best AI, best Python program, best educational program, etc."
    body += "\n\n" + "With the tech era being as prominent as ever here in the Silicon Valley, it is increasingly essential to cultivate the passion for computer science amongst the students in my generation. We have noticed the impact of " + key + "'s sponsorship in other similar events, and we hope that you would be interested in monetarily sponsoring " + hackathonName + ". As a sponsor of our hackathon, your company will be able to form long-lasting impressions of many student developers, and " + key +" will be publicized on our website and our merchandise. However, if you are unable to provide us with monetary help at this time, we would be happy to receive any form of sponsorship " + key + " can offer."
    body += "\n\nIf you are interested, I can email you a copy of our Sponsorship Prospectus. I look forward to following up with you in the next few days and answering any further questions. We would be grateful to arrange a sponsorship deal with you!"
    body += "\n\nSincerely," + "\n" + name + "\n" + title + "\n"+ phonenumber + "\n" + website + "\n\n"
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # open the file to be sent  
    filename = "FrontierHacks_Sponsorship_Prospectus"
    attachment = open("/Users/neerajmac/Downloads/FrontierHacks_Sponsorship_Prospectus.pdf", "rb") 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, values[0], text) 
      
  
# terminating the session 
s.quit() 
