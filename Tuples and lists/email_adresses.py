def get_emails():
    break_stat = False
    email = []
    while break_stat is False:
        get_string = input("Email address: ")
        if get_string.lower() == "q":
            break_stat = True
        else:
            email.append(get_string) 
    return email

def get_names_and_domains(email_list):
    mail_domain = []
    for x in email_list:
        mail_domain.append(tuple(x.split("@")))
    return mail_domain

# Main program starts here - DO NOT change it
email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)