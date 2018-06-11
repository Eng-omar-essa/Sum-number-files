import unittest
from app import *
class TestAppMethods(unittest.TestCase):

    """
    Test the reading files data app.py
    """
    def test_sum_total_number_of_3_files(self):
        readData = ReadingFileData()
        list_of_files = ['A.txt', 'b.txt', 'c.txt']
        for file in list_of_files:
            lines = readData.readFile(file)
            for value in lines:
                if value.isdigit():
                    readData.sumTotalNumber.append(int(value))
                else:
                    readData.readFile(value)

        total = sum(readData.sumTotalNumber)
        print(total)
        self.assertEqual(total ,111)


    def test_sum_total_number_of_all_files(self):
        readData = ReadingFileData()
        readData.sumTotalNumber = []
        total = readData.getTotalNumber()
        print(total)
        self.assertEqual(total,120)


if __name__ == '__main__':
    unittest.main()
