import requests


def main():
    # print the header
    print_the_header()

    # get the zipcode
    code = input('What zipcode do you want (98335)? ')

    # get html from web
    get_html_from_web(code)

    # parse the html
    # display the forcast
    print('Hello from main')

def print_the_header():
    print('----------------------------------')
    print('         WEATHER APP              ')
    print('----------------------------------')
    print()

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print(response.text[0:250])


if __name__ == '__main__':
    main()