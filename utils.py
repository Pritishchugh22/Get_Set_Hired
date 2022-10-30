def tryExcept(req, a, b, c):
    try:
        a.__dict__[b] = c
    except:
        from django.contrib import messages
        messages.error(req, "Error in ", b)

def check(req, field, fieldName):
    from django.contrib import messages
    if field != "" and field != None:
        return True
    print(field)
    messages.error(req, "Please complete " + fieldName)
    return False

def sendNotification(jobposting, user, text):
    from home.models import Notification
    Notification(sender = jobposting.company, reviever = user, message = text + ' ' + jobposting.title).save()

def profileCompleted(req):
    user = req.user
    isCompleted = check(req, user.username, "username")
    isCompleted = isCompleted and check(req, user.email, "email")
    if user.userprofile.isUser:
        isCompleted = isCompleted and check(req, user.first_name, "first_name")
        isCompleted = isCompleted and check(req, user.last_name, "last_name")
        isCompleted = isCompleted and check(req, user.userprofile.contact_num, "contact_num")
        isCompleted = isCompleted and check(req, user.userprofile.education, "education")
        isCompleted = isCompleted and check(req, user.userprofile.experience_yrs, "experience_yrs")
        isCompleted = isCompleted and check(req, user.userprofile.age, "age")
        isCompleted = isCompleted and check(req, user.userprofile.willing_to_work_at, "willing_to_work_at")
    else:
        isCompleted = isCompleted and check(req, user.companyprofile.name, "name")
        isCompleted = isCompleted and check(req, user.companyprofile.contact_num, "contact_num")
        isCompleted = isCompleted and check(req, user.companyprofile.number_of_employees, "number_of_employees")
    return isCompleted

def sendFormErrorMessages(req, form):
    import json
    from django.contrib import messages
    for errorLabel in form.errors:
        message = errorLabel + " - "
        errorMessages = json.loads(form.errors[errorLabel].as_json())
        for errorMessage in errorMessages:
            message += errorMessage['message'] + " "
        messages.error(req, message)