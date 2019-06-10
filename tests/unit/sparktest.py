import pytest
from pyspark import SparkContext

from config import ENV


class SparkEnv:
    _SC = None

    @classmethod
    def getSc(cls):
        if cls._SC == None:
            cls._SC = SparkContext(appName="SparkTest")

        return cls._SC
    

class SparkTest:

    @pytest.fixture
    def sc(self):
        return SparkEnv.getSc()

    @pytest.fixture
    def env(self):
        return ENV
