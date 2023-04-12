
import sys
import getopt

# Example usage
# python given_args.py -f=test.json -k=django -l=tre

def get_dates():
    filename = None
    keyword = None
    location = None

    argv = sys.argv[1:]
    # print(argv)

    try:
        opts, args = getopt.getopt(argv, "f:k:l:", ["filename=", "keyword=", "location="])
    except getopt.GetoptError as err:
        print(err)
        opts = []

    for opt, arg in opts:
        if opt in ['-f', '--filenamne']:
            filenamne = arg
        elif opt in ['-k', '--keyword']:
            keyword = arg
        elif opt in ['-l', '--location']:
            location = arg

    print(f'filenamne: {filenamne}')
    print(f'keyword: {keyword}')
    print(f'location: {location}')

		    
get_dates()

