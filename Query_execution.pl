% Experiment 6: Implementation of Simple Clauses in Prolog

% Facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules

% 1. John likes anything that Mary likes
likes(john, X) :- likes(mary, X).

% 2. John likes anyone who likes wine
likes(john, Y) :- likes(Y, wine).

% 3. John likes anyone who likes themselves
likes(john, Z) :- likes(Z, Z).

% Sample Queries

% Query 1: ?- likes(mary, food).
% Output: true.

% Query 2: ?- likes(john, wine).
% Output: true.

% Query 3: ?- likes(john, food).
% Output: true.

% Query 4: ?- likes(john, Y).
% Output: Lists the possible values of Y.
