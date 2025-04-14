import sys
import unittest

from python_fcc.broadband_api import *
from python_fcc.FRNConversionsAPI import *
from python_fcc.block_conversion_api import *


class TestBroadbandAPI(unittest.TestCase):
    def setUp(self):
        self.bb = BroadbandApi()
        self.frnapi = FRNConversionsAPI()

    def test_FRN(self):
        result = self.frnapi.getInfo(frn="0016095838")
        self.assertTrue(result["Results"][0]["frn"] == "0016095838")

    def test_companyName(self):
        result = self.frnapi.getInfo(frn="0016095838")
        self.assertTrue(
            result["Results"][0]["companyName"] == "Cygnus Communications Corporation"
        )

    def test_FRNapiIsDict(self):
        result1 = self.frnapi.getList(stateCode="IL")
        result2 = self.frnapi.getInfo(frn="0016095838")
        self.assertTrue(type(result1) == type({}) and type(result2) == type({}))

    def test_CygnusInIL(self):
        result = self.frnapi.getList(stateCode="IL")
        # print result['Frns']
        # Cygnus Telecommunications Corporation
        self.assertTrue(
            "Cygnus Communications Corporation"
            in [x["companyName"] for x in result["Results"]]
        )


class TestBlockConversionAPI(unittest.TestCase):
    def setUp(self):
        self.bb = BlockConversionAPI()

    # Does SF exist? (Really, more Santa Cruz)
    def test_SF(self):
        result = self.bb.get_block(latitude=37, longitude=-122)

        self.assertTrue(result["status"] == "OK")
        self.assertTrue(result["State"]["code"] == "CA")
        self.assertTrue(result["Block"]["FIPS"] == "060871001001003")

    # Does (somewhere near) Chicago exist? (Jasper, IN)
    def test_Chicago(self):
        result = self.bb.get_block(latitude=41, longitude=-87)

        self.assertTrue(result["Block"]["FIPS"] == "180731008003098")

    # Test the middle of nowhere (Disclaimer: I have no idea where
    # this is, so it may not be in the middle of nowhere)
    def test_Nowhere(self):
        result = self.bb.get_block(latitude=35, longitude=35)

        self.assertTrue(result["Block"]["FIPS"] == None)


if __name__ == "__main__":
    unittest.main()
