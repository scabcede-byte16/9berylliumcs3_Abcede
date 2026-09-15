# Class Relationships: Association and Multiplicity
## Previous Work

[Part I - Classes and Objects](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/a4571f64b2f186d99336a5367650a008e6097f13/quarter1/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/scabcede-byte16/9berylliumcs3_Abcede/blob/a4571f64b2f186d99336a5367650a008e6097f13/quarter1/classAttributesMethods.md)

## Existing Class
Class: Filipino UAAP Women’s Volleyball

Description: This class is made for the teams that are participating in UAAP Women’s Volleyball and their games.

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
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?

