def savefile(file, text):
    # file = 'C:/Users/Kadari Sadhvika/test.txt'
    try:
        fileobj = open(file, 'w')
        joined_string = "\n".join(text)
        fileobj.write(joined_string)
        fileobj.close()
    except OSError:
        print('Failed creating the file')
    else:
        print('File created')
