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
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Composition
Explanation: I chose composition as their relationship because my child cannot meaningfully exist without its parent. The athletes cannot meaningfully exist without the team they're in.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection

1 Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.

These two classes already have a parent-child relationship. That is because the parent class is more generalized while the child class is specific to the parent.

2 How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

Inheritance reduces duplicate codes by letting the child class inherit methods from the parent class. All of the methods from my parent class were reused to my child class.

3 Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.

I chose composition as their relationship because my child cannot meaningfully exist without its parent. The athletes cannot meaningfully exist without the team they're in and vice versa. FilipinoUAAPWomensVolleyball HAS-A UAAPWomensVolleyballAthletes


4 What is the difference between Association from Part III and the advanced relationship you
implemented?

In part 3, the second class had different methods compared to the first. In this part, the child class has attributes that come from the parent class.

5 How does your design follow the DRY principle?

The DRY principle states that "every piece of knowledge must have a single, unambiguous, authoritative representation within a system". My design follows this principle because when the parent class is updated, the child class also gets updated.

LLM used: -> Built-in Gemini feature when searching in Google Prompt/s:
"What is the DRY principle?"
"How does a has-a relationship work?"
"How does inheritance work in OOP?"