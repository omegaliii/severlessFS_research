class File:
    def __init__(self):
        self.isOpen = False
        self.isFile = False
        self.isReadable = False
        self.isWriteable = False
        self.content = ''

class Directory():
    def __init__(self):
        self.files = {}

root = Directory()

def mkdir(path):
    t = root
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            t.files[d[i]] = Directory()
        t = t.files[d[i]]

def rmdir(path):
    t = root
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    if(path != "/"): 
        d = path.split("/")
        for i in range(1,len(d)-1):
            if (d[i] not in t.files):
                raise Exception("path incorrect: no", d[i])
            t = t.files.get(d[i])
        
        if(isinstance(t.files[d[-1]], Directory)):
            del t.files[d[-1]]
            return
        else:
            print("It is not a directory.")

    print("root can't be removed")
        

def ls(path):
    t = root

    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    if(path != "/"): 
        d = path.split("/")
        for i in range(1,len(d)):
            if (d[i] not in t.files):
                raise Exception("path incorrect: no", d[i])
            t = t.files.get(d[i])

    for i in t.files.keys():
        print(i)

def create(path):
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    t = root
    d = path.split("/")
    for i in range(1,len(d)-1):
        if (d[i] not in t.files):
            raise Exception("path incorrect: no", d[i])
        t = t.files[d[i]]

    if (d[-1] in t.files):
        print("File already exist.")
        return
    
    t.files[d[-1]] = File()
    t = t.files[d[-1]]

def openFile(path, flag='rw'):
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            raise PathIncorrectException("path incorrect: no", d[i])
        t = t.files[d[i]]
    
    flagList = list(flag)
    if(isinstance(t,File)):
        if('r' in flagList):
            t.isOpen = True
            t.isReadable = True
        if('w' in flagList):
            t.isOpen = True
            t.isWriteable = True
    else:
        raise Exception("Not a file. Can't be opened")
    
    return t

def close(path):
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            raise Exception("path incorrect: no", d[i])
        t = t.files[d[i]]
    
    if(isinstance(t,File)):
        t.isOpen = False
        t.isReadable = False
        t.isWriteable = False

def read(path):
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            raise Exception("path incorrect: no", d[i])
        t = t.files[d[i]]
    
    if(isinstance(t,File)):
        if(t.isOpen and t.isReadable):
            if(not t.content):
                return
            else:
                print(t.content)
        else:
            if(not t.isOpen):
                raise Exception("File is not open")
            else:
                raise Exception("File is not readable")
    else:
        raise Exception("Not a file. Can't be read")

def readline(path):
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            raise Exception("path incorrect: no", d[i])
        t = t.files[d[i]]
    
    if(isinstance(t,File)):
        if(t.isOpen and t.isReadable):
            if(not t.content):
                return
            else:
                print(t.content.split('\n')[0])
        else:
            if(not t.isOpen):
                raise Exception("File is not open")
            else:
                raise Exception("File is not readable")
    else:
        raise Exception("Not a file. Can't be read")

def write(path, content):
    if (path[0] != "/"):
        raise Exception("path mush start with '/'")

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            raise Exception("path incorrect: no", d[i])
        t = t.files[d[i]]
    
    if(isinstance(t,File)):
        if(t.isOpen and t.isWriteable):
            t.content = t.content + content
        else:
            if(not t.isOpen):
                raise Exception("File is not open")
            else:
                raise Exception("File is not writeable")
    else:
        raise Exception("Not a file. Can't be write")

def getRoot():
    return root

class PathIncorrectException(Exception):
    pass