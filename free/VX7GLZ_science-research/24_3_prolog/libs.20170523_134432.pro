/**
 * C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/24_3_prolog/libs.20170523_134432.pro

['C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/24_3_prolog/libs.20170523_134432.pro'].
*
 */

sum([],0).
sum([X|Xs],Sum) :-
   sum(Xs,Sum1), Sum is X + Sum1.

float_decimal(X,Y,Z) :-
   X1 is X * 10^Y,
   X2 is floor(X1),
   Z is X2 / (10^Y*1.0)
   .
