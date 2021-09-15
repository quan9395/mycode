from automata.fa.dfa import DFA

print("Enter a string from a language:")
x = input()

#ending with ‘ab’
dfa1 = DFA(
    states = {'q0', 'q1', 'q2'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':'q1', 'b':'q0'},
        'q1':{'a':'q1', 'b':'q2'},
        'q2':{'a':'q1', 'b':'q0'},
    },
    initial_state = 'q0',
    final_states = {'q2'}
)

#starting and ending with ‘b’
dfa2 = DFA(
    states = {'q0', 'q1', 'q2', 'd'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':'d', 'b':'q1'},
        'q1':{'a':'q1', 'b':'q2'},
        'q2':{'a':'q1', 'b':'q2'},
        'd':{'a':'d', 'b': 'd'}
    },
    initial_state = 'q0',
    final_states = {'q2'}
)

# the number of both a’s and of b’s is odd
dfa3 = DFA(
    states = {'q0', 'q1', 'q2', 'd'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':'q1', 'b':'d'},
        'q1':{'a':'q0', 'b':'q2'},
        'q2':{'a':'d', 'b':'q1'},
        'd':{'a':'q2', 'b': 'q0'}
    },
    initial_state = 'q0',
    final_states = {'q2'}
)
if(dfa1.accepts_input(x) or
    dfa2.accepts_input(x) or
    dfa3.accepts_input(x)):
    print("Accepted")
else:
    print("Rejected")