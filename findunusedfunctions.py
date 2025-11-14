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
			content += "\n".join(tmp) + "\n"
		except Exception as e: print(e); exit()
	content = content.splitlines()
	return [line for line in content if '#' not in line]

def giveContent(filename):
	try:
		content = open(filename, "r").read().splitlines()
		return [line for line in content if '#' not in line]
	except Exception as e:
		print(e);

def giveDefs(content):
	if content == None: return []
	defs = [line.split()[1] for line in content if 'def ' in line]
	return [part[:part.index('(')] for part in defs]

def giveFuncCalls(content):
	if content == None: return []
	return [line[:line.index('(')] for line in content if '(' in line and 'def' not in line]

def giveUnusedFuncs(defs, func_calls):
	return [func for func in defs if func not in func_calls]

def findunusedfunctions(filename):
	content = giveContent(filename)
	#content = get_all_files_content()
	unused_funcs = giveUnusedFuncs(giveDefs(content), giveFuncCalls(content))
	print("Unused Functions:", unused_funcs)

if __name__ == "__main__":
	ac = len(sys.argv)
	if ac > 1:
		for i in range(1, ac): findunusedfunctions(sys.argv[i])
	else: print('Give files in args'); exit()