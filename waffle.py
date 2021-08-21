import csv
import numpy

with open("input.csv", newline='') as file:
    array = list(csv.reader(file))
    
    # Headers sanity check.
    for x in array[0]:
        if x not in ["img", "text", "url"]:
            print("Error: header incorrect.")
        if array[0][0] == "url":
            print("Error: the first header can't be an URL.")
            
    # Make the output file.
    with open("output.md", 'w') as out:
        #out.write("lol")
    
        # Make some loopies.
        xlen = len(array[0])
        for y in range(1, len(array)):
            out.write('\n|')
            for x in range(xlen):
                # Images
                if array[0][x] == "img":
                    if (array[0][x+1]) == "url":
                        out.write('[')
                    out.write("![]("+array[y][x]+')')
                    if (array[0][x+1]) == "url":
                        out.write("]("+array[y][x+1]+')')
                # Text
                elif array[0][x] == "text":
                    if (array[0][x+1]) == "url":
                        out.write('[')
                    out.write(array[y][x])
                    if (array[0][x+1]) == "url":
                        out.write("]("+array[y][x+1]+')')
                
                # Line break within the cell.
                out.write("<br />");
            out.write('|')
            if y == 1:
                out.write("\n| ---- |")