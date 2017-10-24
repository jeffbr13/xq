import sys
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.html import XmlLexer


print(highlight(sys.stdin.read(), XmlLexer(), Terminal256Formatter()))
