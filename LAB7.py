def first(): 
    try:
        print("Opening file...")
        file_exmpl=open("TF12_1.txt","w")
        buff=input('please enter how more line you want to write in file\n')
        for i in range(int(buff)):
            buff_str=input('please enter line\n') + '\n'
            file_exmpl.write(buff_str)
        file_exmpl.close()
    except:
        print("File not found!")

def second():
    try:
        file_example=open("TF12_1.txt","r")
        file_example1=open("TF12_2.txt","w")
        i=1
        for line in file_example :
            for j in range(i):
                file_example1.write(line[j])
            file_example1.write('\n')
            i=i+1
            if i>10:
                i=1
        file_example.close()
        file_example1.close()
    except:
        print("File not found!")

def third():
    try:
        file_example=open("TF12_2.txt","r")
        for line in file_example:
            print(line.strip())
        file_example.close()
    except:
        print("file not found!")


first()
second()
print('text in TF12_2 file')
third()