# coding: utf8

from collections import namedtuple

from rpmUtils.miscutils import splitFilename


APackage = namedtuple('APackage', ['name', 'version', 'release', 'arch'])


class PackageParser(object):
    @staticmethod
    def parsePackage(filename):
        (n, v, r, e, a) = splitFilename(filename)
        return APackage(n, v, r, a)
    
