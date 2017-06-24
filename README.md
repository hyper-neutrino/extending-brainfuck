# extending-brainfuck
The purpose of this project is to try to build up many layers of abstraction, all compiling down to Brainfuck, with the ultimate intention that Brainfuck will be able to be used for more complex things.

### Preprocessor
The preprocessor modifies code before anything can run it, except BF1, because BF1 literally does not care what you throw at it as long as your square brackets are balanced. Otherwise, the code is modified by the preprocessor first.

### BF1
This is Brainfuck 1, the original Brainfuck. Here are the instructions:

<pre><code>+ Increment the current memory cell
- Decrement the current memory cell
> Move the pointer right one space
< Move the pointer left one space
[ Start a loop; jumps to ] if the memory cell is 0
] End a loop; jumps back to [ if the memory cell is not 0
. Output memory cell using whatever chr() returns
, Input to memory cell using whatever ord() returns</code></pre>

The tape starts as `[0]`, and it automatically expands itself as necessary. `delay`, `max`, and `min` are function parameters used to control infinite looping to prevent crashing/freezing.

### BF2
This is Brainfuck 2, the next layer of abstraction above the original Brainfuck. It allows the entry of numbers to perform `+`, `-`, `<`, or `>` multiple times. For example, `+3` will become `+++`. `BF2.downgrade` turns BF2 code into BF1 code. `BF2.run` downgrades and then calls BF1 to interpret it.

### BF3
This is Brainfuck 3, the next layer of abstraction over BF2. Actually, BF3 doesn't compile into BF2; it compiles directly into BF1. I could make it compile into BF2 but that wouldn't help with readability or anything. BF3 has its own instruction set:

<pre><code>!+ Add the cell directly to the right of the current cell to the current cell, removing the contents of the right cell, and leaving the pointer in the same location.
!- Subtract the cell directly to the right of the current cell from the current cell, removing the contents of the right cell, and leaving the pointer in the same location
!* Multiply the cell directly to the right of the current cell with the current cell, removing the contents of the next three cells to the right, and leaving the pointer in the same location
!! Zero the current cell, leaving the pointer in the same location
!> Shift the content of the current cell 1 cell to the right, overwriting the right cell and zeroing the original cell, and moving the pointer to the right 1 cell
!< Shift the content of the current cell 1 cell to the left, overwriting the left cell and zeroing the original cell, and moving the pointer to the left 1 cell
!@ Swap the current cell with the cell 1 cell to the right, overwriting the second cell to the right, and moving the pointer to the right 1
?+ Add the current cell into the cell directly to the right of the current cell, removing the contents of the original cell, and moving the pointer to the right 1 cell
?- Subtract the current cell from the cell directly to the right of the current cell, removing the contents of the original cell, and moving the pointer to the right 1 cell
?* Multiply the current cell with the cell directly to the right of the current cell, removing the contents of the original cell and the cell two and three cells to the right of it, and moving the pointer to the right 1 cells
?? Zero the cell to the right, leaving the pointer in the same location
?> Copy the content of the current cell 1 cell to the right, overwriting the right cell but not zeroing the original cell, and moving the pointer to the right 1 cell
?< Copy the content of the current cell 1 cell to the left, overwriting the left cell but not zeroing the original cell, and moving the pointer to the left 1 cell
?@ Swap the current cell with the cell 1 cell to the left, overwriting the second cell to the left, and moving the pointer to the left 1</pre></code>

### BF4
This is Brainfuck 4, the next layer of abstraction over BF3. It adds custom functions.

Each line that matches the regular expression `^\w+:.+$` is treated as a function, in the form `function_name:commands`. Thus, take the following code as an example:

<pre><code>a:++++++++++
b:aaa
bb.</code></pre>

`a` evaluates to `++++++++++` which makes `b = aaa = ++++++++++++++++++++++++++++++`. Then, calling `bb` will do that twice, resulting in `60`, and the `.` prints it as `'<'`.
