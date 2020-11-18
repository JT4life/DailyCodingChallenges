class WordCount:
    @staticmethod
    def same_counts(string):
        countJ = 0
        countM = 0
        john = "John"
        mary = "Mary"
        if john in string.lower():
            countJ +=1
        if mary in string:
            countM +=1
        if countJ == countM:
            return True
        else:
            return False

print(WordCount.same_counts("John&Mary"))

string = "John Mary John"

a = WordCount()
a.same_counts(string)