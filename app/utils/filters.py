# format the date
def format_date(date):
    return date.strftime('%m/%d/%y')

# format the url
def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# format plural words
def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    
    return word

