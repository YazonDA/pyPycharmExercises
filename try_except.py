class WrongAnswer(Exception):
	pass
def sm():
	print('into DEF')
	try:
		print('into TRY')
		raise WrongAnswer
	finally:
		print('into FINALLY')
	print('after TRY into DEF')
		

print('programm started')

try:
	print('into TRY')
except WrongAnswer as e:
	print('into EXCEPT')

print('then starting DEF')
sm()
print('after all')