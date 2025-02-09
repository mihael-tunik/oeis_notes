<img src="A052852_21.svg" alt="drawing" width="50%"/>

Suppose you have n positions and n towers of heights from 1 up to n. You can place each tower on every position, possibly many in one place. If two or more towers are on the same place, the highest one is standing before all so they can't be seen. How many combinations are possible?

If you run the code, you'll get [the sequence](https://oeis.org/A052852), which refers to infinite continued fractions (what?).

### Bonus
This interpretation with towers gives nice recurrence:
$$T_n = n \sum_{k=0}^n C_{n-1}^k T_{n-(k+1)} $$

Place tallest tower n ways and for each, place n-k-1 towers into n-1 place. 
Each combination repeats for every T_{n-(k+1)} combinations.

Example:
$$T_3 = 3(T_2 + 2 T_1 + 1) = 3 (4 + 2 + 1) = 21$$.


