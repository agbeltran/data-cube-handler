

def compare(fname1, fname2, verbose):
    # Based on
    # http://www.opentechguides.com/how-to/article/python/58/python-file-comparison.html
    # Open file for reading in text mode (default mode)
    f1 = open(fname1)
    f2 = open(fname2)
    output = True

    # Print confirmation
    if verbose:
        print("-----------------------------------")
        print("Comparing files ", " > " + fname1, " < " + fname2, sep='\n')
        print("-----------------------------------")

    # Read the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Initialize counter for line number
    line_no = 1

    # Loop if either file1 or file2 has not reached EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        # Compare the lines from both file
        if f1_line != f2_line:
            output = False
            # If a line does not exist on file2 then mark the output with + sign
            if f2_line == '' and f1_line != '':
                if verbose:
                    print(">+", "Line-%d" % line_no, f1_line)
            # otherwise output the line on file1 and mark it with > sign
            elif f1_line != '':
                if verbose:
                    print(">", "Line-%d" % line_no, f1_line)

            # If a line does not exist on file1 then mark the output with + sign
            if f1_line == '' and f2_line != '':
                if verbose:
                    print("<+", "Line-%d" % line_no, f2_line)
            # otherwise output the line on file2 and mark it with < sign
            elif f2_line != '':
                if verbose:
                    print("<", "Line-%d" % line_no, f2_line)

            # Print a blank line
            if verbose:
                print()

        # Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()

        # Increment line counter
        line_no += 1

    # Close the files
    f1.close()
    f2.close()
    if (verbose and output):
        print("The files have the same content.")
    elif verbose:
        print("The files have NOT the same content.")
    return output