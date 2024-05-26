# Challenge: Building a Banking System

## Overview
Create a banking system with the operations: withdraw, deposit, and view statement. We have been hired by a major bank to develop its new system. This bank aims to modernize its operations and has chosen the Python language for this purpose. For the first version of the system, we should implement only 3 operations: deposit, withdraw, and view statement.

## Rules
It should be possible to deposit positive values into my bank account. Version 1 of the project works only with 1 user, so we don't need to worry about identifying the account number and branch. All deposits must be stored in a variable and displayed in the statement operation.

The system should allow 3 withdrawals per day with a maximum limit of $500.00 per withdrawal. If the user does not have enough balance in the account, the system should display a message indicating that it is not possible to withdraw the money due to insufficient balance. All withdrawals must be stored in a variable and displayed in the statement operation.

This operation should list all deposits and withdrawals made in the account. At the end of the listing, the current account balance should be displayed. If the statement is blank, display the message: No transactions have been made. Values ​​should be displayed using the format $ xxx.xx, for example: 1500.45 = $1500.45.
