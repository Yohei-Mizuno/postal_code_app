from response_2 import search_address


def main():
   zipcode = input()

   address = search_address(zipcode)

   print(address)


if __name__ == '__main__':
   main()
