#----Import self made modules
import txtopp as to # find txtopp module code as a github repository on my account
import list_module as lm


#main convert function
def convert(value, inunit, outunit, quantity):
    #define 2 directories as variables
    udir = f'database/{quantity}/{quantity}_units.txt'
    cdir = f'database/{quantity}/{quantity}_convo.txt'


    # use txtopp module to convert the data in the files into a list
    units = to.read_list(file=udir, separator='\n')
    convo = to.read_list(file=cdir, separator='\n')


    #main dictionary
    unitsdict = {}


    #funtion to insert data into dictionary
    def dict():
        unitsdict.clear()
        for i in range(len(units)):
            unitsdict[units[i]] = float(convo[i])
    dict()


    #modifing the data to match output unit
    for item in convo:
        y = float(item)/unitsdict[outunit]
        lm.replace(x=item, y=y, list=convo)
    dict()
    

    #calculating the answer and returning it
    ans = str(float(value)*float(unitsdict[inunit])) + ' '+outunit
    return ans