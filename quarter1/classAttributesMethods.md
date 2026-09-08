# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
| Length | int | public | This attribute is public because the length of the game should be seen for those who want to watch with limited time. |
| Available | boolean | public | The availability is public because it should be seen if the game is available or not. |
| Points | int | private | Points are private to prevent comparisons. |
| Name | string | public | The name is public to check what two teams are currently in a match. |
## Updated UML Class Diagram
+--------------------------------------------+
| Filipino UAAP Women's Volleyball |

+--------------------------------------------+
| + Length : int |
| + Available : boolean |
| - Points : int |
| + Name : string |
+--------------------------------------------+
| + method() |
| + method(parameter : datatype)|
| + getSomething() |
+--------------------------------------------+
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
