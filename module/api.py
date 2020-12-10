
class UTReporter(object):
    '''
    The UT Report class keeps track of tests cases
    that have been executed.
    '''
    def __init__(self):
        self.testcases = []
        print ("init called")

    def add_testcase(self, testcase):
        self.testcases.append(testcase)

    def display_report(self):
        for tc in self.testcases:
            msg = "=============================" + "\n" + \
                "Sheet: " + tc['sheet'] + "\n" + \
                "Name: " + tc['name'] + "\n" + \
                "Description: " + str(tc['description']) + "\n" + \
                "Status: " + tc['status'] + "\n"
            print (msg)

reporter = UTReporter()

def assert_capture(*args, **kwargs):
    '''
    The Decorator defines the override behavior.
    unit test functions decorated with this decorator, will ignore
    the Unittest AssertionError. Instead they will log the test case
    to the UTReporter.
    '''
    def assert_decorator(func):
        def inner(*args, **kwargs):
            tc = {}
            tc['sheet'] = str(func.__qualname__).split('.')[0]
            tc['name'] = func.__name__
            tc['description'] = func.__doc__
            try:
                func(*args, **kwargs)
                tc['status'] = 'pass'
            except:
                tc['status'] = 'fail'
            reporter.add_testcase(tc)
        return inner
    return assert_decorator
