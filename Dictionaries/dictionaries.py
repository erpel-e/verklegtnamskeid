post = {"user_id": 209, "message": "Hello darkness", "language": "english"}

post2 = dict(message="bop bop", language="English")

print(post["user_id"])
loc = post2.get("location", None)
print(loc)

for key in post.keys():
	value = post[key]
	print(key, "=", value)

for key, value in post.items():
	print(key, "=", value)

student = {"name": "John", "age": 25, "course": ["math", "compsci"]}
student["phone"] = "555-5555"
student["name"] = "jae"
print(student)
print(student.get("phone", "Not Found"))
student.update({"name":"jennifer", "age": 20, "phone":123456})
print(student)
#del student["age"]
age = student.pop("age")
print(len(student))



