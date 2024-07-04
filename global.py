result=0
def add(k,l):
    global result
    result=k+l
def sub(k,l):
    global result
    result=k-l
def display_result():
    global result
    print(f" the result is:{result}")
add(17,5)
display_result()
sub(5,17)
display_result()
