class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        cmp1 = self.major - other.major
        cmp2 = self.minor - other.minor
        cmp3 = self.patch - other.patch

        return cmp1 == 0 and cmp2 == 0 and cmp3 == 0

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def patch_version_up(self):
        return SemanticVersion(self.major, self.minor, self.patch + 1)

    def minor_version_up(self):
        return SemanticVersion(self.major, self.minor + 1, 0)

    def major_version_up(self):
        return SemanticVersion(self.major + 1, 0, 0)


def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    # 等価である場合
    print(SemanticVersion(3, 7, 0) == py370)  # True

    # 等価でない場合
    print(SemanticVersion(3, 7, 1) == py370)  # False

    # 文字列を取得
    print('3.7.0' == str(py370))  # True

    # パッチバージョンアップ
    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True

    # マイナーバージョンアップ
    py380 = py370.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)  # True

    # メジャーバージョンアップ
    py400 = py370.major_version_up()
    print(SemanticVersion(4, 0, 0) == py400)  # True


if __name__ == '__main__':
    main()
