def convert(st):
    st1=st.replace(':)','🙂')
    st2=st1.replace(':(','🙁')
    return st2
def main():
    st=input('enter input:')
    print(convert(st))
main()
