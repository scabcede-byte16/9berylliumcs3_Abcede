# Advanced Class Relationships

## Previous Activities
[classAttrib](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/3fc3846ab7a3019bac50d4ebd3e0debaf6a1a41d/quarter1/classAttributesMethods.md)
[classRel](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/3fc3846ab7a3019bac50d4ebd3e0debaf6a1a41d/quarter1/classRelationships.md)

## Existing System Description:
Class 1: Filipino UAAP Women’s Volleyball
Class 2: UAAP Women’s Volleyball Athletes
These two classes are closesly related to one another. They cannot be independent, therefore need each other.

## Inheritance Relationship
Parent: Filipino UAAP Womens Volleyball
Child: UAAP Womens Volleyball Athletes
Explanation: These two classes already have a parent-child relationship. That is because the parent class is more generalized while the child class is specific to the parent.

## Inheritance UML
<img width="1080" height="1920" alt="YourClass +--------------------+  class blueprint  +--------------------+  -------------------   v v object1  YourClass object2  YourClass +-------------------+ +-------------------+  attr = value (2)" src="https://github.com/user-attachments/assets/24567fc3-2b95-48ea-852d-58ba963a203c" />


## Composition/Aggregation
Relationship: Composition
Explanation: I chose composition as their relationship because my methods cannot meaningfully exist without the whole. For example, the athlete name cannot meaningfully exist without the athletes themselves.

## Advanced UML Diagram
<img width="1080" height="1920" alt="YourClass +--------------------+  class blueprint  +--------------------+  -------------------   v v object1  YourClass object2  YourClass +-------------------+ +-------------------+  attr = value (3)" src="https://github.com/user-attachments/assets/6dcf3640-e207-4119-8901-42b3e854a752" />


## Python Implementation
[Source Code](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/7009a1889859da05125c48ef3b8857fab75eb7bf/quarter1/advancedRelationships.py)

## Test Run
<img width="1381" height="684" alt="image" src="https://github.com/user-attachments/assets/6773112a-c16f-4978-a8ec-70c488a6b631" />

## Object Diagram
<img width="2000" height="2000" alt="yes" src="https://github.com/user-attachments/assets/118e4a8b-435b-49ca-b202-8933c207f985" />


## Reflection

1 Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.

These two classes already have a parent-child relationship. That is because the parent class is more generalized while the child class is specific to the parent.

2 How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

Inheritance reduces duplicate codes by letting the child class inherit methods from the parent class. All of the methods from my parent class were reused to my child class.

3 Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.

I chose composition as their relationship because my child cannot meaningfully exist without its parent. As the example earlier, the athlete names cannot meaningfully exist without the athletes themselves. UAAPWomensVolleyballAthletes HAS-A Name.

4 What is the difference between Association from Part III and the advanced relationship you
implemented?

In part 3, the second class had different methods compared to the first. In this part, the child class has attributes that come from the parent class.

5 How does your design follow the DRY principle?

The DRY principle states that "every piece of knowledge must have a single, unambiguous, authoritative representation within a system". My design follows this principle because when the parent class is updated, the child class also gets updated.

LLM used: -> Built-in Gemini feature when searching in Google Prompt/s:
"What is the DRY principle?"
"How does a has-a relationship work?"
"How does inheritance work in OOP?"
