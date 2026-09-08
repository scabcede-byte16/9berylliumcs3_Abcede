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

| displayLength(Length_of_Game) |

| displayAvailable(Availability_of_game) |

| displayPoints(Amount_of_Points) |

| displayName(Name_of_schools) |

+--------------------------------------------+
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
<img width="1181" height="391" alt="image" src="https://github.com/user-attachments/assets/39eb9928-3f74-49ce-ab43-d55d7f2a105c" />

## Object Diagram
<img width="438" height="403" alt="image" src="https://github.com/user-attachments/assets/e487bc8b-d6be-4ae3-9e55-d074dc153840" />

## Analysis
### Why did you make your chosen attribute private?

In our society today, instead of using the score to know what to improve, they use the score to ridicule the losing team.

### Which method changes the state of your object?

The method that changes the state of my object is points because it has a parameter

### How did your two objects demonstrate that instances are independent?

It demonstrated that the two instances are independent since one object with a different data field does not mean that the other object has the same data field.

### What is the difference between your class diagram and your object diagram?

The class diagram is the blue print while the object diagram shows what I can do with the blueprint.
