from sys import platform


def print_version(package_name, version):
    print("The current verion of " + str(package_name) + " is " + str(version))


def get_platform():
    return platform.system()