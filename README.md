# extending-brainfuck
The purpose of this project is to try to build up many layers of abstraction, all compiling down to Brainfuck, with the ultimate intention that Brainfuck will be able to be used for more complex things.

### BF1
This is Brainfuck 1, the original Brainfuck. Here are the instructions:

<pre><code>
\+ Increment the current memory cell  
\- Decrement the current memory cell  
\> Move the pointer right one space  
\< Move the pointer left one space  
\[ Start a loop; jumps to ] if the memory cell is 0  
\] End a loop; jumps back to [ if the memory cell is not 0  
\. Output memory cell using whatever chr() returns  
\, Input to memory cell using whatever ord() returns  
</code></pre>

The tape starts as `[0]`, and it automatically expands itself as necessary. `delay`, `max`, and `min` are function parameters used to control infinite looping to prevent crashing/freezing.

### BF2
This is Brainfuck 2, the next layer of abstraction above the original Brainfuck. It allows
