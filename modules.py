# calling function of others file

from calling_file import add_kor as adding

if __name__== '__main__':

    sums = adding(10, 5)
    print('result from modules.py', sums)