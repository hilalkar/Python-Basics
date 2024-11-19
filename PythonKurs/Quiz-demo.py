# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer


    def checkAnswer(self,answer):
         return self.answer==answer


q1=Question("En iyi programlama dili hangisidir ? ",["C#","Python","JavaScript", "Java"], "Python")
q2=Question("En popüler programlama dili hangisidir ? ",["Python","JavaScript","C#", "Java"], "Python")
q3=Question("En çok kazandıran programlama dili hangisidir ? ",["C#","JavaScript", "Java","C#"], "Python")

liste=[q1,q2,q3]

print(q1.checkAnswer("Python"))
print(q1.checkAnswer("C#"))

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0



