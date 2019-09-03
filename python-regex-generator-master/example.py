"""Created By PrakashLeonMishra | PrakashLeonMishra.com"""
from main import regexGenerator;

pattern = "(anyword) (notdigit) ";
generator = regexGenerator.regexGenerator(pattern);

print (generator.getExpression());
