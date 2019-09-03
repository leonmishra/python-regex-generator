
class regexPattern :
	
	pattern = "";
	
	def __init__(self):
		self.pattern = "";
	
	def _appendToPattern(self,pattern):
		self.pattern+=pattern;
		
	def getPattern(self,useGlobalMarker=False):
		return "/{}/".format(self.pattern);
		
	
	def anyWord(self,negate=False):
		if(negate==True):
			return  self._appendToPattern("\W");
		else:
			return self._appendToPattern("\w");
		
	def anyDigit(self,negate=False):
		if(negate==True):
			return  self._appendToPattern("\D");
		else:
			return self._appendToPattern("\d");
	
	def whiteSpace(self,negate=False):
		if(negate==True):
			return  self._appendToPattern("\S");
		else:
			return self._appendToPattern("\d");
		


class regexGenerator:
	baseString = "";
	regexString = "";
	reference = {"(anyword)": "\w", "(notword)": "\W", "(anydigit)": "\d", "(notdigit)": "\D", "(whitespace)": "\s",
		"(notwhitespace)": "\S", };
	
	def _evaluateSpecialCases(self, word):
		if ("group(" in word):
			return "123";
		else:
			return "";
	
	def _initializeObject(self):
		baseString = self.baseString;
		list = baseString.split(" ");
		for word in list:
			if (word in self.reference):
				evaluatedString = self.reference[word].strip();
			else:
				evaluatedString = self._evaluateSpecialCases(word);
			self.regexString += evaluatedString;
	
	def __init__(self, baseString):
		self.baseString = baseString;
		if (len(self.baseString) > 0):
			self._initializeObject();
	
	def getExpression(self):
		return "/{}/".format(self.regexString);
