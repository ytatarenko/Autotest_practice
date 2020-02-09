import requests
import json
from functools import reduce
import time
import calendar


#def get_from_dict(dataDict, mapList):
#    """Iterate nested dictionary"""
#    return reduce(dict.get, mapList, dataDict)


start_time = str(calendar.timegm(time.gmtime()))+'000' #start time in epoch format - current time stamp
end_time = str(calendar.timegm(time.gmtime())+2592000)+'000' #end time in epoch format - start time + 1 month
domain1 = 'https://democlubready.netpulse.com/np/exerciser/login?username=autotest@mailinator.com&password=Netpulse1'
domain2 = 'https://democlubready.netpulse.com/np/company/1b86d272-ca43-400c-b8bb-4e3c7c0cb788/classes?endDateTime=' + str(end_time) + '&exerciserUuid=89ca182b-7af9-4e2e-8059-54e73fa9602e&startDateTime=' + str(start_time)
with requests.Session() as call:
    login = call.post(domain1)
    login_response = json.loads(login.text)
    for cookie in call.cookies:
        print(cookie.name, cookie.value)
    cookies=call.cookies
    print (login_response)
    classes = call.get(domain2, cookies=cookies)
    classes_response = json.loads(classes.text)
    print (classes_response)
    i=0
    for i in range (0,len(classes_response)):
                                 class_data = classes_response[i]
                                 if reduce(dict.get, ("brief", "name"), class_data) == "Class for Auto Tests": #searching test class from response
                                        if reduce(dict.get, ("brief", "totalBooked"), class_data) == 0: #checking if the class isn't full
                                            schedule_id = reduce(dict.get, ("brief", "id"), class_data) #getting schedule id of the class
                                            print(schedule_id)
                                            break




    #class details "https://democlubready.netpulse.com/np/company/1b86d272-ca43-400c-b8bb-4e3c7c0cb788/class/22600718?exerciserUuid=89ca182b-7af9-4e2e-8059-54e73fa9602e"
    domain3 = 'https://democlubready.netpulse.com/np/company/1b86d272-ca43-400c-b8bb-4e3c7c0cb788/class/'+ str(schedule_id) + '/addExerciser?exerciserUuid=89ca182b-7af9-4e2e-8059-54e73fa9602e'
    book = call.post(domain3, cookies=cookies)
    book_response = json.loads(book.text)
    print (book_response)

    domain4 = 'https://democlubready.netpulse.com/np/company/1b86d272-ca43-400c-b8bb-4e3c7c0cb788/class/'+ str(22600720) + '/removeExerciser?exerciserUuid=89ca182b-7af9-4e2e-8059-54e73fa9602e'
    remove = call.post(domain4, cookies=cookies)
    remove_response = json.loads(remove.text)
    print(remove_response)

