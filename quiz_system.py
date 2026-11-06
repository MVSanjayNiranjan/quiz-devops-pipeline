class Question:
    def __init__(self, q_id, text, options, answer):
        self.q_id = q_id
        self.text = text
        self.options = options
        self.answer = answer

    def display(self):
        print(f"Q{self.q_id}. {self.text}")
        for i, option in enumerate(self.options, start=1):
            print(f"   {i}) {option}")


class QuizManagementSystem:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        print(f"Added Q{question.q_id} to {self.quiz_name}.")

    def list_questions(self):
        print(f"\n--- {self.quiz_name} Question List ---")
        for question in self.questions:
            question.display()

    def evaluate(self, student, responses):
        score = 0
        for question in self.questions:
            if responses.get(question.q_id) == question.answer:
                score += 1
        total = len(self.questions)
        percent = score * 100 / total
        grade = "Pass" if percent >= 50 else "Fail"
        print(f"\nStudent: {student} | Score: {score}/{total} | "
              f"Percentage: {percent:.1f}% | Result: {grade}")
        return score


# Example Usage
if __name__ == "__main__":
    qms = QuizManagementSystem("Python Basics Quiz")
    qms.add_question(Question(1, "Which data type is mutable?",
                              ["List", "Tuple", "String"], "List"))
    qms.add_question(Question(2, "Which keyword defines a function?",
                              ["func", "def", "define"], "def"))
    qms.add_question(Question(3, "What is the output of 2 ** 3?",
                              ["6", "8", "9"], "8"))
    qms.list_questions()
    qms.evaluate("Alice", {1: "List", 2: "def", 3: "8"})
    qms.evaluate("Bob", {1: "Tuple", 2: "def", 3: "6"})
