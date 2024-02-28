import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 10

def main():
    system_major = sys.version_info.major
    system_minor = sys.version_info.minor
    if system_major != REQUIRED_MAJOR or system_minor != REQUIRED_MINOR:
        raise TypeError(
            "This project requires Python {}.{}. Found: Python {}. Run `make create_environment` to create an enviroment of Python 3.10 with conda".format(
                REQUIRED_MAJOR, REQUIRED_MINOR, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()