Quiz Score Tracker
This project is a simple tool to help teachers or students track quiz results. It calculates the total points, the highest and lowest scores, and the average marks.

How it Works
The project is split into two parts to keep the math separate from the testing.

exm.py: This is the main program. It contains the logic for updating scores and asks the user to type in the results.

test.py: This is the inspector. It uses the unittest module to make sure the math in the main program is 100% correct.

How to Use
Run exm.py to enter student scores one by one.

Type 'done' when you are finished to see the final summary.

Run test.py at any time to verify that the scoring logic is working perfectly.

Key Features
Whole Number Logic: Uses int for clean, easy-to-read scores.

Automated Testing: Uses unittest to prevent math errors.

Memory Efficient: Does not store a long list of scores; it updates totals instantly.

Created By
Aritraw Ghosal Arko
