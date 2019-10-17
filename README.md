# Assn3-Hash-Function
# Name: BSAF-5

## Functions:

    F(B,C) = (B⋃¬C)⋃(B⋂¬C)
    G(B,C) = (¬C⋃(B⋂C))⨁(B⋃C)
    H(B,C) = (B⋃¬C)⨁C
    I(B,C) = B⨁C

## Definitions
•	Deterministic
Ours is deterministic because we are not using any random generators in our code. And not depending on specific memory addresses to run such code thus making it repeatable every time and satisfying the definition of determinism. 

•	One Way
Shifts and multi rounds and different functions each round.

•	Pre-image resistant
Shifts and multi-function

•	Collision resistant
Shifts aid, however it is less collision resistant than md5 due to less rounds.

•	Computationally efficient
O(n) which is ideal. 
 
## Structure

input: 512 bit chunks

chunks: 16, 32 bit chunks

Output: 96 bit numbers

rounds:48

