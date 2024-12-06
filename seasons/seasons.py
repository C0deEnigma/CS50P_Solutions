import datetime
import sys
import re
import inflect
def valid_dob(DOB):
    if re.search(r'\d{4}-\d{2}-\d{2}',DOB):
        return True
    else:
        return False
def convert_to_words(n):
    p=inflect.engine()
    w=p.number_to_words(n)
    s=''
    l=w.split(' and')
    for i in l:
        s=s+i
    return s.capitalize()+' minutes'
def main():
    DOB=input('Date of Birth: ')
    if not(valid_dob(DOB)):
        sys.exit('Invalid Date')
    dob=datetime.date.fromisoformat(DOB)
    today = datetime.date.today()
    if not(valid_dob(str(today))):
        sys.exit('Invalid Date')
    total_mins=24*60*(int(((str(today-dob)).split())[0]))
    print(convert_to_words(total_mins))
if __name__ == "__main__":
    main()
