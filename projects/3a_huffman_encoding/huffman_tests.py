"""
Luis Gomez
Data Structures
"""
import unittest
import filecmp
import subprocess
from huffman import *

usediff = False  # When comparing files: True to use Linux diff, False to use Python filecmp

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        create_huff_tree(freqlist)
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self):
        huffman_encode("file3.txt", "file3_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb file3_out.txt file3_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("file3_out.txt", "file3_soln.txt"))

    def test_04_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline_soln.txt"))

    def test_05_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("declaration_out.txt", "declaration_soln.txt"))

    def test_06_textfile_empty(self):
        huffman_encode("empty_thing.txt", "empty_thing_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        if usediff:
            err = subprocess.call("diff -wb empty_thing_out.txt empty_thing.txt", shell = True)
            self.assertEqual(err, 0)
        else:
            self.assertTrue(filecmp.cmp("empty_thing_out.txt", "empty_thing.txt"))

    def test_07_exception(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("DNE.txt", "DNE_out.txt")

if __name__ == '__main__': 
   unittest.main()
