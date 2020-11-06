def main():
    #write your code below this line
f= open("data.text"  ,  "r")
if f.mode == "r": 
    contents = f.read()
    print (contents)





if __name__ == '__main__':
    main()
