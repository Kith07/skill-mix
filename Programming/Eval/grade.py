import os
import openai
from dotenv import load_dotenv

load_dotenv()

k = 6
j = 3
topic = "Compiler Construction"
skills_str = "Bloom Filters & Probabilistic Data Structures, Hashing Strategies like Collision Resolution, Cuckoo Hashing, etc., Parallel Processing & Thread Synchronization, Memoization & Tabulation, Efficient String Manipulation with Z-algorithm, KMP, Rabin-Karp, etc., and Tree Transformations & Rotations"
skills_list = ["Bloom Filters & Probabilistic Data Structures", "Hashing Strategies like Collision Resolution, Cuckoo Hashing, etc.", "Parallel Processing & Thread Synchronization", "Memoization & Tabulation", "Efficient String Manipulation with Z-algorithm, KMP, Rabin-Karp, etc.", "Tree Transformations & Rotations"]

with open(f"Output/k_{k}/new_output{j}.txt", 'r') as file:
    student_answer = file.read()

rubric_items = ''
rubric_start = "Correctly illustrates"
skills_rubric_items = [f"{rubric_start} {skill}" for skill in skills_list]
rubric_items = skills_rubric_items + [f"Pertains to {topic}", "Text makes sense"]
rubric_items = ', '.join(rubric_items)

prompt = f'''
Greetings! I was wondering if you could help me grade the following answer given by a student.\n
I’ll first describe the question that was given to the student, and then give you the student’s answer, and the grading rubric.\n
The question given to the student was as follows: \"Generate a code snippet in the context of {topic}. This code should illustrate all of the following skills: {skills_str}.\"\n
The student's answer was:\n
\"{student_answer}\"\n
Using a rubric table format, please grade the student's answer with positive scoring. Each criterion is worth 1 point.\n
The criteria are: {rubric_items}.\n
The table should only have the following columns: 'Criteria', 'Points Earned'. In the 'Points Earned' column, please provide only numerical values with no additional formatting. Please introduce the table with 'Here's the grading table:' and please include a row for 'Total Points Earned' at the end of the table. Finally, please start your grading explanation with 'Explanation':
'''
print(prompt)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = [
        {"role": "user", "content": prompt}
    ]
)

print(response["choices"][0]["message"]["content"])