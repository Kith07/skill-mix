import openai
import os
import random
from dotenv import load_dotenv
load_dotenv()

TOPICS = [
"Sorting Algorithms",
"Searching Algorithms",
"Data Structures",
"Object-Oriented Programming",
"File Handling",
"Basic SQL and Databases",
"Networking Basics",
"Time Complexity",
"Recursion",
"Dynamic Programming",
"Concurrency",
"Parallelism",
"Memory Management",
"Debugging",
"Profiling",
"Code Optimization",
"Performance Tuning",
"Compiler Construction",
"Code Parsing",
"Task Automation"
]

SKILLS = ["Recursion & Base Case Identification",
"Backtracking & Constraint Propagation",
"Greedy Algorithm Heuristics",
"Divide and Conquer Strategy",
"Memoization & Tabulation",
"Bitwise Operations & Manipulation",
"Event-Driven Programming",
"Lazy Evaluation & Short-Circuiting",
"Concurrency Control using Locks, Semaphores, CAS",
"Parallel Processing & Thread Synchronization",
"Heap & Priority Queue Usage",
"Graph Traversal using BFS, DFS, Topological Sorting",
"Cycle Detection in Graphs",
"Tree Transformations & Rotations",
"Dynamic Memory Allocation & Garbage Collection Awareness",
"Hashing Strategies like Collision Resolution, Cuckoo Hashing, etc.",
"Bloom Filters & Probabilistic Data Structures",
"Trees & Prefix Tree Optimization",
"Efficient String Manipulation with Z-algorithm, KMP, Rabin-Karp, etc.",
"Regular Expression Parsing & Tokenization",
"Error Handling & Exception Propagation",
"Cache Optimization & Data Locality",
"Database Indexing & Query Optimization Techniques",
"Immutability & Functional Programming Constructs",
]

selected_topic = random.sample(TOPICS, 1)[0]
sample_topic = f"{selected_topic}"
print(f"TOPIC: {sample_topic}\n")

k = 6
skills_subset = random.sample(SKILLS, k)
sample_skills = ""
for i in range(k - 1):
    sample_skills += f"{skills_subset[i]}, "
sample_skills += f"and {skills_subset[k - 1]}"

print(f"SKILLS: {sample_skills}\n")

prompt1 = f'''Greetings! I am interested in programming and I was wondering 
if you could help me generate an example of text that illustrates multiple skills in 
coding structure and syntax. The example should be a block of code with the primary goal of 
demonstrating the {sample_topic} while also illustrating all of the following skills: {sample_skills}. 
Please keep the code as concise as possible, and make sure the implementation can be found 
fully from the produced code. \n\nPlease ensure that you don't simply repeat the given example 
and start the block of code with 'Solution:' and start the explanation with 'Explanation:'.
\n\nThanks very much!'''

# prompt2 = f"Thanks very much. Could you please look over your code and improve it? Please make sure that the new answer better implement all skills and accomplishes the task in the topic. On top of that, please also make sure the new answer {IMPOSE_RESTRICTIONS}. \nAgain, please start the improved block of code with 'Solution:' and start the explanation with 'Explanation:'.\n\nThanks very much!"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = [
        {"role": "user", "content": prompt1}
    ]
)

print(response["choices"][0]["message"]["content"])