# Jigme Lobsang Lepcha Roll no: 2016045
# Rajat Kumar Singh Roll no: 2016182
import unittest
from a3 import *
from GetData import *
class testa3(unittest.TestCase):
	def testoffByK(self):
		self.assertEqual(offByK("Jigme","Gigme",1),True)
		self.assertEqual(offByK("Lepcha","lexcha",4),False)
		self.assertEqual(offByK("Jiggy","Jig",2),False)
		self.assertEqual(offByK("IIITD","IIITD",1),False)
		self.assertEqual(offByK("ada","ADA",3),True)
		self.assertEqual(offByK("","",0),True)
		self.assertEqual(offByK("Swareena","swareena",1),True)
	def testoffBySwaps(self):
		self.assertEqual(offBySwaps("Jigme","migJe"),True)
		self.assertEqual(offBySwaps("read","raed"),True)
		self.assertEqual(offBySwaps("wangyal","choden"),False)
		self.assertEqual(offBySwaps("AA","aa"),False)
		self.assertEqual(offBySwaps("aa","aa"),True)
		self.assertEqual(offBySwaps("Sweccha","sweccha"),False)
	def testoffByKExtra(self):
		self.assertEqual(offByKExtra("Jigme","Jimge",0),False)
		self.assertEqual(offByKExtra("Jigme","Jig",2),True)
		self.assertEqual(offByKExtra("Jigme","Jiigmeex",3),True)
		self.assertEqual(offByKExtra("Jigme","Jigme",0),True)
		self.assertEqual(offByKExtra("sonamla","sonamla",2),False)
		self.assertEqual(offByKExtra("reaxd","read",1),True)
		self.assertEqual(offByKExtra("namrata","Namrata",1),True)
		self.assertEqual(offByKExtra("JiGmE","jigme",3),True)
	def testListOfNearStrings(self):
		L=fileToStringList("EnglishWords.txt")
		self.assertEqual(ListOfNearStrings("ab",L[0:9],0),[])
		self.assertEqual(ListOfNearStrings("ckaab",L[9:20],5),["aback"])
		self.assertEqual(ListOfNearStrings("aba",L[12:20],2),["abaft"])
		self.assertEqual(ListOfNearStrings("aaxhs",L[0:9],1),["aahs"])
		self.assertEqual(ListOfNearStrings("abandon",L[12:30],2),["abandoned","abandonee","abandoner"])
		self.assertEqual(ListOfNearStrings("abandoners",L[2:40],0),[])
	def testcompare_distr(self):
		self.assertEqual(compare_distr([7,11,9,14,13,16],[101,96,96,93,97,92],4),True)
		self.assertEqual(compare_distr([0,1,0,0],[-4,-3,-4,-4],1),True)
		self.assertEqual(compare_distr([2,3,2],[5,4,5],1),False)
		self.assertEqual(compare_distr([-7,-3,-9,-8],[9,17,10,9],3),True)
		self.assertEqual(compare_distr([],[],5),False)
		
if __name__=='__main__':
	unittest.main()