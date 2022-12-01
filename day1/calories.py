def main():
    input = open("input.txt","r")
    elfs = []
    sum = 0;
    
    for line in input:
        line = line.strip()
        if(line.isnumeric()):
            sum = sum + int(line)
        else:
            elfs.append(sum)
            sum = 0;
        
    elfs.sort();
    print("the elfs with the most calories in decending order have {}, {}, and {} calories respectivly."
    .format(elfs[-1],elfs[-2],elfs[-3]))
    
    print("in total they have {} calories".format(elfs[-1]+elfs[-2]+elfs[-3]))
        
    


if __name__== "__main__":
    main()