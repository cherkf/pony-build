#! /usr/bin/env python
import sys
from pony_client import HgClone, Context, TempDirectoryContext, _run_command

context = Context()

url = 'http://bitbucket.org/ned/coveragepy/'

(ret, out, err) = _run_command(['hg', 'clone', url])
assert ret == 0, (out, err)

commands = [ HgClone(url) ]
print 'Success'