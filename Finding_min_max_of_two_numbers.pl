max(A, B, A) :- A >= B.
max(A, B, B) :- A < B.

min(A, B, A) :- A =< B.
min(A, B, B) :- A > B.
