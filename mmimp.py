#!/usr/bin/python 

# The MIT License
# 
# Copyright (c) 2011 VUnite Media LLC [http://vunite.com]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os 
import optparse
import pprint
import commands
from datetime import date 

class MMImp:
	'''MySQL Multiple SQL File Importer CLI.'''
	
	version = '1.0'
	
	def __init__(self):
		self.mysqlPath = '/usr/bin/mysql'
		self.mysqlHost = 'localhost'
		self.mysqlUser = 'root'
		self.mysqlPassword = ''
		
	def handleOptions(self):  
		"""CLI Options Handler"""
		
		self.showHeader()
		p = optparse.OptionParser("Usage: %prog [options] arg1 arg2"
				"%prog {0:s}".format(MMImp.version))
		p.add_option('--path', '-p', action="store", type="string", default="/Users/karmadude",
				help="Path to SQL Files") 
		p.add_option('--database', '-d', action="store", type="string", default="test",
				help="Database to import into")
		
		(options, args) = p.parse_args()
		
		if options.path != '':
			self.importData(options.path, options.database) 
	
	def showHeader(self):  
		"""CLI Header"""
		
		print "MMImp (cli) version {0:s}".format(MMImp.version)
		print "The MIT License | Copyright (c) {0:d} VUnite Media [http://vunite.com]".format(date.today().year)  

	def importData(self, path, db): 
		"""Importer"""
		
		if path[0] == '~':
			path = os.path.expanduser(path)
		
		files = [f for f in os.listdir(path) if f[0] != '.' and os.path.splitext(f)[1] == '.sql']
		for f in files:  
			c = "{0:s} -h{1:s} -u {2:s} --password={3:s} {4:s} < {5:s}".format(
				self.mysqlPath,
				self.mysqlHost,
				self.mysqlUser,
				self.mysqlPassword,
				db,
				os.path.join(path, f)) 
			commands.getoutput(c)  
			print "Imported: {0:s}".format(f)
		

def main():
	m = MMImp();
	m.handleOptions();
	
if __name__ == '__main__':
	main()