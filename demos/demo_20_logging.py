import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s"
)

logging.warning("Program is for demo purposes only")


def main():
    logging.info("Starting the program")
    retrieve_data()


def retrieve_data():
    logging.info("Downloading")
    data = [1, 2, 3]
    logging.debug(data)


if __name__ == "__main__":
    main()
