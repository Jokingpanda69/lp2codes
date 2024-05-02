% Define predicates to handle greetings
greet :-
    write('Hello! I\'m your friendly chatbot. How can I assist you today?'),
    nl.

% Define predicates to handle responses
response(hello) :-
    write('Hi there! How can I help you?'),
    nl.
response(hi) :-
    write('Hello! How can I assist you today?'),
    nl.
response(how_are_you) :-
    write('I\'m just a Prolog program, so I don\'t have feelings, but thanks for asking!'),
    nl.
response(goodbye) :-
    write('Goodbye! Have a great day!'),
    nl,
    halt. % Halt the program when user says goodbye.

% Define predicate to handle unrecognized inputs
response(_) :-
    write('I\'m not sure I understand. Can you please rephrase or ask something else?'),
    nl.

% Main predicate to initiate conversation
chat :-
    greet,
    repeat,
    write('You: '),
    read(UserInput), % Read user input
    response(UserInput), % Respond based on user input
    fail. % Fail to loop back and repeat

% Start the conversation
:- initialization(chat).
