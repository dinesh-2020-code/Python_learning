required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'python'}
}
interviewees = set()
for candidate , skills in candidates.items():
    if skills.issuperset(required_skills):
        interviewees.add(candidate)

print(interviewees)
