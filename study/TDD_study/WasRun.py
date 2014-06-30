# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)


    def setUp(self):
        self.log = "setUp "


    def testMethod(self):
        self.wasRun = 1
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        self.test.run()
        assert ("setUp testMethod tearDown " == self.test.log)


if __name__ == '__main__':
    TestCaseTest('setUp').run()
    TestCaseTest('testTemplateMethod').run()

