#! usr/bin/env python3
# coding=utf-8


import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Setup Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Teardown Class")

    def setUp(self) -> None:
        print("Setup")

    def tearDown(self) -> None:
        print("Teardown")

    def test_case01(self):
        print("test_case01")
        self.assertIn('h', 'this')
        self.assertEqual('title','title',"判断相等")
        # self.assertTitle('baidu','sina')


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case01"))
    unittest.TextTestRunner().run(suite)