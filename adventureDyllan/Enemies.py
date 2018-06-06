import random
import operator

# def randomCalc():
#     ops = {'+':operator.add,
#            '-':operator.sub,
#            '*':operator.mul,
#            '/':operator.truediv}
#     num1 = random.randint(0,12)
#     num2 = random.randint(1,10)   # I don't sample 0's to protect against divide-by-zero
#     op = random.choice(list(ops.keys()))
#     answer = ops.get(op)(num1,num2)
#     print('What is {} {} {}?\n'.format(num1, op, num2))
#     return answer

# def askQuestion():
#     answer = randomCalc()
#     guess = float(input())
#     return guess == answer

# def quiz():
#     print('Welcome. This is a 10 question math quiz\n')
#     score = 0
#     for i in range(10):
#         correct = askQuestion()
#         if correct:
#             score += 1
#             print('Correct!\n')
#         else:
#             print('Incorrect!\n')
#     return 'Your score was {}/10'.format(score)

class Enemy:
	"""
	Base class for Enemies

	Variables:
		name <str>
		subject <str>
		question <str>
		answer <str>
		guesses <int>
		correct <bool> Defaults to false, when true enemy is dead

	Methods:
		__init__(self,name,hp,damage) Initializes base enemy class
		is_alive(self) Method to determine if enemy is alive, true or false 
		 base on hp
	"""
	def __init__(self, name, subject, question, answer, guesses, correct = False):
		"""
		Initializes the Enemy base Class

		Input: 
			name <str>
			subject <str>
			question <str>
			answer <str>

		Output: 
			None
		"""
		self.name = name
		self.subject = subject 
		self.question = question 
		self.answer = answer
		self.guesses = guesses
		self.correct = correct
	
	def is_alive(self):
		"""
		Return true if correct is false, is used to check if the enemy has been defeated 
		Output:
			<bool>
		"""
		return not self.correct

	def guess_made(self, guess):
		"""
		Is used to allow the player to make a guess
		"""
		if (guess == self.answer):
			self.correct = True
		else:
			self.guesses -= 1

	def out_of_guesses(self):
		return self.guesses <= 0


class TestQuestion(Enemy):
	"""
	Subclass of Enemy

	Variables:
		name <str>
		hp <int>
		damage <int>

	Methods:
		__init__(self) calls Enemy init method with specific information 
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			hp <int>
			damage <int>
		"""
		super().__init__(name="Test", subject = "Philosophy", question = "Who is awesome!?", answer = "Me", guesses = 2)




class FillInQuestion(Enemy):
	"""
	Subclass of Enemy

	Variables:
		name <str>
		hp <int>
		damage <int>

	Methods:
		__init__(self) calls Enemy init method with specific information 
	"""
	def __init__(self):
		"""
		Input: 
			name <str>
			hp <int>
			damage <int>
		"""
		self.choices = []
		self.choicea = "\n\ta) Dominic\n"
		self.choiceb = "\tb) Amber\n"
		self.choicec = "\tc) Ciri\n"
		self.choices.append(self.choicea)
		self.choices.append(self.choiceb)
		self.choices.append(self.choicec)
		self.question = "Who is super cute and also super young?\n"
		for choice in self.choices:
			self.question += str(choice)

		super().__init__(name="Fill in", subject = "Literacy", question = self.question, answer = "c", guesses = 2)



class RandomAdditionMathQuestion(Enemy):


	def __init__(self):
		self.x = random.randint(1,99)
		self.y = random.randint(1,99)
		self.solution = self.x + self.y
		super().__init__(name="RandomMath", subject = "Math", question = "What is {} + {}?".format(self.x, self.y), answer = str(self.solution), guesses=3)




class RandomSubtractionMathQuestion(Enemy):


	def __init__(self):
		self.x = random.randint(1,99)
		self.y = random.randint(1,99)
		self.solution = self.x - self.y
		super().__init__(name="RandomMath", subject = "Math", question = "What is {} - {}?".format(self.x, self.y), answer = str(self.solution), guesses=3)




class RandomMultiplicationMathQuestion(Enemy):


	def __init__(self):
		self.x = random.randint(0,10)
		self.y = random.randint(0,12)
		self.solution = self.x * self.y
		super().__init__(name="RandomMath", subject = "Math", question = "What is {} * {}?".format(self.x, self.y), answer = str(self.solution), guesses=3)




class RandomDivisionMathQuestion(Enemy):


	def __init__(self):
		self.x = random.randint(0,30)
		self.y = random.randint(1,5)
		self.solution = self.x / self.y
		super().__init__(name="RandomMath", subject = "Math", question = "What is {} / {} to one decimal place?".format(self.x, self.y), answer = "{0:.1f}".format(self.solution), guesses=3)


