# Monopoly_frequentation_tracker

## Quick info
Simulates rolling dice *n* times in a Monopoly game, tracks how different properties are frequented. Especially recommended to Monopoly enthusiasts.

![Ooops, this image isn't working](images/img1.jpg)

## Method 
Two dice are thrown *n* times, where *n* is determined by the user input. The virtual player advances on the monopoly board accordingly. Special position-changing rules of Monopoly are obeyed, such as:
- cards telling you to 
  - go to a particular square
  - advance to the nearest X
  - go back three spaces
- going to jail through...
  - throwing doubles three times
  - landing on the "Go to jail!" square
  - drawing the card

## Usage

Download all `.py` files and run `monopoly.py` to execute the program. 
Concerning the input, it is recommended that you roll the dice at least *10k* times to obtain results of any use. To get solid results, dial up to *1m* throws, or more. Finally, the program will generate a bar chart, showing the number of visits on each space.
