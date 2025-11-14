# the idea is to check whether every line which has a
	# def bla also has a line where only
	# bla()

import sys
from pathlib import Path

def get_all_files_content():
	filenames = Path('.' + '/').rglob('*.py')
	content = ''
	for filename in filenames:
		try:
			tmp = open(filename, 'r').read().splitlines()
			content += "\n".join(tmp)
		except Exception as e: print(e); exit()
	print(content)
	for name in filenames:
		print(name.resolve())
	#print(filenames)

def giveContent(filename):
	content = open(filename, "r").read().splitlines()
	return [line for line in content if '#' not in line]

def giveDefs(content):
	defs = [line.split()[1] for line in content if 'def ' in line]
	return [part[:part.index('(')] for part in defs]

def giveFuncCalls(content):
	return [line[:line.index('(')] for line in content if '(' in line and 'def' not in line]

def giveUnusedFuncs(defs, func_calls):
	return [func for func in defs if func not in func_calls]

def findunusedfunctions(filename):
	content = giveContent(filename)
	unused_funcs = giveUnusedFuncs(giveDefs(content), giveFuncCalls(content))
	print("Unused Functions:", unused_funcs)

if __name__ == "__main__":
	get_all_files_content()
	#findunusedfunctions('testprogram.py')

"""
import sys
from pathlib import Path

def find_line_after_imports(txt):
	imports = False
	for i, line in enumerate(txt):
		if "import" in line: imports = True
		if "import" not in line and len(line) and imports: return i;

def loopfiles():
	content = []
	if len(sys.argv) < 2: print("Give Folder in Args"); exit()
	elif len(sys.argv) == 2: filenames = Path(sys.argv[1] + '/').rglob('*.py')
	else: filenames = set(sys.argv[1:])
	for filename in filenames:
		try:
			tmp = open(filename, 'r').read().splitlines()
			content += tmp[:find_line_after_imports(tmp)]
		except Exception as e: print(e); exit()
	content = [line for line in content if 'import' in line and line[0] != '#']
	content = [line[:line.find('as')] if 'as' in line else line for line in content]
	content = [line[:line.find('import')] if ',' in line else line for line in content]
	return " ".join(content)

def fiximports():
	imports = loopfiles()
	imports = [line.replace(',', '') for line in ''.join(imp for imp in imports).split()]
	imports = [line.strip() for line in imports if line != 'import' and line != 'from' and line != '*']
	imports = set(imports)
	savedcontent = "\n".join(imports)
	open("requirements.txt", "w").write(savedcontent)
	print("Created requirements.txt for:\n", savedcontent)

if __name__ == "__main__": fiximports();
find_line_after_imports(open("testfolder/test.py", 'r').read().splitlines())
"""