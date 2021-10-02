''' add commandline interface work here'''

import booksdatasource, sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ptATRh?",["sort=","search=","help"])
    except getopt.GetoptError:
        print('Invalid syntax. \nEnter \'python3 books.py --help\' for help.')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '-?' or opt == 'help':
            # give useful info
            sys.exit()
        # elif opt in ("-i", "--ifile"):
        #     inputfile = arg
        # elif opt in ("-o", "--ofile"):
        #     outputfile = arg

if __name__ == '__main__':
    main(sys.argv[1:])
