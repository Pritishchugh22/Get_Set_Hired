def tryExcept(a, b, c):
    try:
        a.__dict__[b] = c
    except:
        print("Error in ", b)

def check(field):
    if field != "" and field != None:
        return True
    return False

def profileCompleted(user):
    isCompleted = check(user.username)
    if user.userprofile.isUser:
        isCompleted = isCompleted and check(user.first_name)
        isCompleted = isCompleted and check(user.last_name)
        isCompleted = isCompleted and check(user.email)
        isCompleted = isCompleted and check(user.userprofile.contact_num)
        isCompleted = isCompleted and check(user.userprofile.education)
        isCompleted = isCompleted and check(user.userprofile.experience_yrs)
        isCompleted = isCompleted and check(user.userprofile.age)
        isCompleted = isCompleted and check(user.userprofile.willing_to_work_at)
    else:
        isCompleted = isCompleted and check(user.email)
        isCompleted = isCompleted and check(user.companyprofile.name)
        isCompleted = isCompleted and check(user.companyprofile.contact_num)
        isCompleted = isCompleted and check(user.companyprofile.number_of_employees)
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