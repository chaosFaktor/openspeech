

def inc(integer):
    return integer+1

def shift_together(arr):
    c=0
    new_arr=[]
    for i in arr:
        if len(i) == 0:
            pass
        else:
            c+=1
        new_arr.insert(c, i)
    return new_arr
    



if __name__=='__main__':
    array= ['A', 'B', 'C', 'D', 'E', 'F']
    array.pop(3)
    shift_together(array)
    for i in array:
        print(array.index(i))