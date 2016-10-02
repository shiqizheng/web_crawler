import unittest
import crawler as c
import json

FILENAME = "Internet/Internet_1.json"
with open(FILENAME) as f:
        test_data = json.load(f)
f.close()


class Test(unittest.TestCase):


    def test_getAllAddrs(self):
        all_addrs = {"http://foo.bar.com/p1":["http://foo.bar.com/p2","http://foo.bar.com/p3","http://foo.bar.com/p4"],
        "http://foo.bar.com/p2":["http://foo.bar.com/p2","http://foo.bar.com/p4"],
        "http://foo.bar.com/p4":["http://foo.bar.com/p5","http://foo.bar.com/p6"],
        "http://foo.bar.com/p5":[],
        "http://foo.bar.com/p6":["http://foo.bar.com/p7","http://foo.bar.com/p4","http://foo.bar.com/p5"]}

        self.assertEqual(sorted(all_addrs.keys()), sorted(c.getAllAddrs(test_data).keys()))

    def test_allLinks(self):
        all_addrs = {"http://foo.bar.com/p1":["http://foo.bar.com/p2","http://foo.bar.com/p3","http://foo.bar.com/p4"],
        "http://foo.bar.com/p2":["http://foo.bar.com/p2","http://foo.bar.com/p4"],
        "http://foo.bar.com/p4":["http://foo.bar.com/p5","http://foo.bar.com/p1","http://foo.bar.com/p6"],
        "http://foo.bar.com/p5":[],
        "http://foo.bar.com/p6":["http://foo.bar.com/p7","http://foo.bar.com/p4","http://foo.bar.com/p5"]}

        test = c.getAllAddrs(test_data)

        for k in all_addrs.keys():
            self.assertEqual(all_addrs[k], test[k])


    def test_crawl(self):
        expected_success = ["http://foo.bar.com/p1", "http://foo.bar.com/p2",
    "http://foo.bar.com/p4", "http://foo.bar.com/p5",
    "http://foo.bar.com/p6"]
        expected_skipped = ["http://foo.bar.com/p2",
    "http://foo.bar.com/p4","http://foo.bar.com/p1",
    "http://foo.bar.com/p5"]
        expected_error = ["http://foo.bar.com/p3", "http://foo.bar.com/p7"]

        ret_success, ret_skipped, ret_error = c.crawl(test_data)

        self.assertEqual(expected_success, ret_success)
        self.assertEqual(expected_skipped, ret_skipped)
        self.assertEqual(expected_error, ret_error)

if __name__ == '__main__':
    unittest.main()
