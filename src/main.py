#!/usr/bin/python
import rest as restinterface
import downloader as download
import logging

# Configure logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s"
)

def main():
    restinterface.start()
    download.download()



# start main method
if __name__ == '__main__':
    main()

