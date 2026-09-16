# Class Relationships: Association and Multiplicity
## Previous Work

[Part I - Classes and Objects](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/a4571f64b2f186d99336a5367650a008e6097f13/quarter1/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/a4571f64b2f186d99336a5367650a008e6097f13/quarter1/classAttributesMethods.md)

## Existing Class
Class: Filipino UAAP Women’s Volleyball

Description: This class is made for the specific teams that are participating in UAAP Women’s Volleyball and their games.

## New Related Class
Class: UAAP Women’s Volleyball Athletes

Description: This new class is made for the athletes that are in the teams.

## Association
Relationship: The athletes are in the team.

Explanation: A team is defined by a group of people working together. The athletes are the groups that make up the teams.

## Multiplicity
Multiplicity: one to many: Team ───────── Athletes

Explanation: There are multiple athletes inside a team. That's why I chose one to many because one team can have multiple athletes.

## UML Class Relationship Diagram
(<img width="1080" height="1920" alt="YourClass +--------------------+  class blueprint  +--------------------+  -------------------   v v object1  YourClass object2  YourClass +-------------------+ +-------------------+  attr = value (1)" src="https://github.com/user-attachments/assets/f58a769e-794d-430d-81a5-ef3decc9e3b3" />
)

## Python Implementation
[View Python Source](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/8fd860d3a5c9cad985cc2733c79f1194bd682e81/quarter1/classRelationships.py)

## Test Run
(<img width="1058" height="894" alt="image" src="https://github.com/user-attachments/assets/50d9f52f-8af0-453f-8657-09ebdc281f91" />
)

## Object Relationship Diagram
(<img width="2000" height="2000" alt="1" src="https://github.com/user-attachments/assets/1999af26-c5d1-40c8-9cbc-ae905aa59db0" />
)

## Analysis
### What is the association between your two classes?

- The athletes are the ones that make the effort to make a team. The team unites the athletes by giving them a shared goal. The team is acts as a support system to each athlete.

### What multiplicity did you choose and why?

- I chose the multiplicity one to many. This is because one team can be connected to multiple athletes. A team cannot be a team without having multiple people.

### How did you implement the relationship in Python?

- I implemented it by putting it in a list.

### Why did you store an object reference instead of copying its data?

- Because if I simply copy the data, the performance won't be as good.

### If your relationship uses many, why is a list appropriate?

- A list is appropriate because it keeps things organized.

LLM used: -> Built-in Gemini feature when searching in Google
Prompt/s:
"How to fix a syntax error"
"Explain multiplicity in python"
"Define a team"
"Is Angel Canino currently an active player?"