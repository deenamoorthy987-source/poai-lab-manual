% Experiment 9: Blocks World Program
% Run using SWI-Prolog.
% Example query: ?- solve.

% Initial arrangement:
% Block A is on the table, B is on A, and C is on the table.
initial_state([
    on(b, a),
    ontable(a),
    ontable(c),
    clear(b),
    clear(c),
    handempty
]).

% Goal: A on the table, C on A, and B on C.
goal_state([
    on(c, a),
    on(b, c),
    ontable(a),
    clear(b),
    handempty
]).

% A block can be picked up from the table.
move(pickup(X),
     [ontable(X), clear(X), handempty],
     [holding(X), clear(X), handempty],
     [ontable(X), handempty]).

% A clear block can be unstacked from another block.
move(unstack(X, Y),
     [on(X, Y), clear(X), handempty],
     [holding(X), clear(Y)],
     [on(X, Y), clear(X), handempty]).

% A held block can be placed on the table.
move(putdown(X),
     [holding(X)],
     [ontable(X), clear(X), handempty],
     [holding(X)]).

% A held block can be stacked on a clear block.
move(stack(X, Y),
     [holding(X), clear(Y)],
     [on(X, Y), clear(X), handempty],
     [holding(X), clear(Y)]).

% Demonstration query: display the initial and goal arrangements.
show_states :-
    initial_state(Initial),
    goal_state(Goal),
    write('Initial state:'), nl,
    maplist(writeln, Initial),
    nl,
    write('Goal state:'), nl,
    maplist(writeln, Goal).

% Check whether a list of conditions is present in a state.
holds_all([], _).
holds_all([Fact|Rest], State) :-
    member(Fact, State),
    holds_all(Rest, State).

% Display the available actions and the conditions they require.
show_actions :-
    move(Action, Preconditions, AddList, DeleteList),
    format('Action: ~w~nPreconditions: ~w~nAdds: ~w~nDeletes: ~w~n~n',
           [Action, Preconditions, AddList, DeleteList]),
    fail.
show_actions.

% Main lab demonstration.
solve :-
    show_states,
    nl,
    write('Available Blocks World actions:'), nl,
    show_actions.
