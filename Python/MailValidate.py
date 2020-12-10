def fun(s):
    try:
        user, url = s.split('@')
        domain, extension = url.split('.')
    except ValueError:
        return False
    
    if user.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif domain.isalnum() is False:
        return False
    elif len(extension) > 3 or extension.isalnum() is False:
        return False
    
    return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)