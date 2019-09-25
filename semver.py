class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def patch_version_up(self):
        return SemanticVersion(self.major, self.minor, self.patch + 1)


def main():
    # kadaiD-1
    py370 = SemanticVersion(major=3, minor=7, patch=0)
    print(SemanticVersion(3, 7, 0) == py370)
    print(SemanticVersion(3, 7, 1) == py370)

    # kadaiD-2
    print('3.7.0' == str(py370))

    # kadaiD-3
    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)


if __name__ == '__main__':
    main()
