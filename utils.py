def tryExcept(a, b, c):
    try:
        a.__dict__[c] = b[c]
    except:
        print("Error in ", c)

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
    else:
        isCompleted = isCompleted and check(user.email)

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