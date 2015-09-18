#
# Test Runner
# https://github.com/davide-ceretti/googleappengine-python-flask-skeleton/blob/master/application/test.py
#
# USAGE
# python tests/test.py ~/google-cloud-sdk/platform/google_appengine/
#
import optparse
import sys
import unittest
import site
import os

USAGE = """python test.py SDK_PATH
Run unit tests for App Engine apps.

SDK_PATH    Path to the SDK installation"""

TEST_PATH = './tests'


def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    site.addsitedir(os.path.join(os.getcwd(), 'lib'))
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(test_path, top_level_dir='.')
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 1:
        print 'Require Google App Engine SDK path.'
        parser.print_help()
        sys.exit(1)
    SDK_PATH = args[0]
    main(SDK_PATH, TEST_PATH)
