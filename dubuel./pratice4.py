#클래스 연습문제
import math

class Compelx_num:
	def __init__(self, real = 0, imag = 0):
		self.real = real
		self.imag = imag

	def __add__(self ,Compelx_num2):
		
		return new_complex(self.real + Compelx_num2.real, self.imag +Compelx_num2.imag)

	def __str__(self):
		if self.imag > 0:
			return f'{self.real} + {self.imag}j'
		else:
			return f'{self.real} - {abs(self.imag)}j'

	def lenth(self):
		return math.sqrt(self.real**2 + self.imag**2),2

	def __eq__(self,Compelx_num2):
		if self.lenth() == Compelx_num2.lenth():
			return True
		else:
			return False

	def __lt__(self,Compelx_num2):
		if self.lenth() <  Compelx_num2.lenth():
			return True
		else:
			return False
	def __le__(self,Compelx_num2):
		if self.lenth() <= Compelx_num2.lenth():
			return True
		else:
			return False
	def __ne__(self,Compelx_num2):
		if self.lenth() != Compelx_num2.lenth():
			return True
		else:
			return False

	def __gt__(self,Compelx_num2):
		if self.lenth() >  Compelx_num2.lenth():
			return True
		else:
			return False

	def __ge__(self,Compelx_num2):
		if self.lenth() >= Compelx_num2.lenth():
			return True
		else:
			return False

a = Compelx_num(2,-1)
b = Compelx_num(2,2)
print(a,b)
print(a>=b)

