import requests
import re
import json
from datetime import date

class Meetings:
    _list = []
    availableDates = []
    attendees = []

    def __init__(self):
        self.data = None      

    def __repr__(self):
           return f'<APICall: works>'
     
        
class Partnerlist:
    def __init__(self, email, name, startDate, attendee_count):
        self.email = email
        self.country= country
        self.start_date = availableDates
        self.attendee_count = partners
                       
        
class Program:  
    base_url = 'https://ct-mock-tech-assessment.herokuapp.com/'
    def run(self):
        api_call = f"{self.base_url}"
        response = requests.get(api_call)
        self.data = response.json()

united_states = []
ireland = []
spain = []
singapore = []
canada = []
japan = []
united_kingdom = []
france = []

program = Program()
program.run()
# meetings.calls
partners = program.data
# print(partners)
partner  = partners['partners']
country = partners['partners'][0]['country']  
attendees = len(partners)
email = partners['partners'][0]['email'] 
conference_dates = partners['partners'][0]['availableDates']
start_date = 'availableDates'
# attendance = {
#             'availableDates' : availableDates,
#             'attendees' : email
#         }

# list_of_partners = {
#            'name' : country,
#            'start_date' : startDate,
#            'attendee_count' : attendees,
#            'partners' : partners,
#            'email' : email,     
#                     }
# print(country) == 
for people in partner:
    if people ['country'] == 'United States':
        united_states.append(people)
    elif people ['country'] == 'France':
        france.append(people)
    elif people ['country'] == 'Ireland':
        ireland.append(people)
    elif people ['country'] == 'Spain':
        spain.append(people)
    elif people ['country'] == 'Singapore':
        singapore.append(people)
    elif people ['country'] == 'Canada':
        canada.append(people)
    elif people ['country'] == 'Japan':
        japan.append(people)
    elif people ['country'] == 'United Kindgom':
        united_kingdom.append(people)

        
start_date = ['availableDates']


# print(result)

# [date(2017-5-19),(2017-5-20),"2017-05-21",
# # "2017-05-26",
# # "2017-05-28",
# # "2017-05-29",
# # "2017-06-01",
# # "2017-06-02",
# # "2017-06-03"]

# start_date = availableDates
# for sdate in united_statees:
#     if s [start_date] == enumerate(availableDates):
#         print(s)
email = []
for emails in partner:
        email.append(partner['partners']['email'])     
# for emails in partner:
#     if emails ['email'] == 'email':
#         email.append(emails)
        
# start = ['availableDates']
# date = [datetime.strptime(date, "%Y-%m-%d") for date in start_date]
# start = set([date.toordinal() for date in date])
# if max(start) - min(start) == len(start) - 1:
#     datetime.datetime()
#     print()

# names = [{'partners'}]  


                
#     if item == firstName:
#           del names[item]]
#         print(names_removed)


                 

# for startdate in range(len(start_date)):
     
#     if start_date[startdate] == start_date[startdate]:
#         print(start_date[startdate])

print(united_states)