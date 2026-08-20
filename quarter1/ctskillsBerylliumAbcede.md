# Computational Thinking Exercise
## [Smart School Canteen Queue]
Name: Sofiya C. Abcede
Section: Beryllium
Last Name: Abcede
Date: 08/20/2026
---

## Step 1: Identify the Big Problem
### Main Problem
The canteen gets too crowded during lunch breaks because of the absence of a proper system that will help the canteen staff. 
---
## Step 2: Identify the Sub-Problems
1. Buyers take too long when taking their order.
2. Cashiers have to manually calculate the total cost and change for the buyer.
3. During rush hours, there is no system that will notify the staff if a food is running out.

---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Buyers take too long when taking their order. | Abstraction | There should be menus so that the buyer can think of what they want to order before reaching the cashier. |
| Cashiers have to manually calculate the total cost and change for the buyer. | Algorithm Design | There should be devices that have a set inventory. Once the cashier inputs the name of the item, it will automatically show its price. When there are several items, the device will automatically sum all of them and minus the sum from the payment that will be given for change. |
| During rush hours, there is no system that will notify the staff if a food is running out. | Pattern Recognition | There will be a device that monitors the items, that device will have a low stock limit and notify the staff if the item is getting too low on stock. |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
During rush hours, there is no system that will notify the staff if a food is running out.
### Pseudocode
START
Set warning for low stock
Check the current stock level of an item
Check if the current level is below limit
IF yes THEN
    Notify the staff
Else
    Continue monitoring
END IF
---