import pycurl

def download():
    c = pycurl.Curl()
    with open("file.txt", "r") as ins:
        for line in ins:
        c.setopt(c.URL, line)
        with open( os.path.basename(line), 'w') as f:
            c.setopt(c.WRITEFUNCTION, f.write)
            c.perform()