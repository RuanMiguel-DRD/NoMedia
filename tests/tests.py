import unittest

from os import getcwd, mkdir, rmdir, path

from nomedia.__main__ import check_directory, media_control


class TestMain(unittest.TestCase):

#    def setUp(self):
#        return super().setUp()

    def test_valid_directory(self):

        self.assertTrue(check_directory("."))
        self.assertTrue(check_directory(".."))

        self.assertTrue(check_directory("/"))
        self.assertTrue(check_directory("/storage"))

        self.assertTrue(check_directory(getcwd()))
        self.assertTrue(check_directory(f"{getcwd()}/../"))


    def test_invalid_directory(self):

        self.assertFalse(check_directory("*"))
        self.assertFalse(check_directory("\""))

        self.assertFalse(check_directory("non-existent-directory"))


    def test_media_control(self):

        self.assertIsNone(media_control("."))
        if not path.exists(".nomedia"):
            self.fail(".nomedia file not created")

        self.assertIsNone(media_control(".", True))
        if path.exists(".nomedia"):
            self.fail("the .nomedia file was not deleted")


    def test_errors_media_control(self):

        with self.assertRaises(FileNotFoundError):
            media_control("non-existent-directory")

        # Error: You do not have sufficient permissions to work on directory "directory"
        self.assertIsNotNone(media_control("/"))

        # Error: There is a directory named ".nomedia" inside "directory"
        mkdir(".nomedia")
        self.assertIsNotNone(media_control("."))
        rmdir(".nomedia")


if __name__ == "__main__":
    unittest.main()
