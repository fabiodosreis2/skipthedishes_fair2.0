from subprocess import call


if __name__ == '__main__':
    call(["docker", "build", "-t", "vanhackaton", "."])
