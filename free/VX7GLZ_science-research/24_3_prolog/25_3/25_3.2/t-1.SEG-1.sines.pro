sines(Start,Tick) :-
    Start >= 0,
    X is sin(Start),
%!    format("Start = ~5f / X = ~5f / ", [Start,X]),
    format('sin(~5f) is ~5f~n', [Start, X]),
    Y is Start - Tick,
    sines(Y,Tick)
    .

