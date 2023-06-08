# Chapter 3 Vocabulary
## 3.1 - The if Statement Vocabulary

Control structure : a logical design that controls the order in which a set of statements execute

Sequence structure : a set of statements that execute in the order that they appear

Decision structure : a control structure that can execute a set of statements only under certain circumstances (alson known as selection structures)

Diamond symbol: The diamond symbol in a flowchart indicates some condition that must be tested

Conditionally exectued: performed only when a certain condition is true

Single alternative decision structure : provides only one alternative path of execution. If the condition in the diamon symbol is true, we take the alternative path

Single alternative decision structure : use the if statement
if condition:
    statement
    statement
    etc.

if clause : begins with the word if, followed by a condition, which is an expression that will be evaluated as either true or false. A colon appeats after the condition. 

Block : a set of statements that belong together as a group, indented

Boolean expression: expressions that are tested by the if statement, named after George Boole who invented a system of mathematics in which the abstract concepts of true and false can be used in computations

Relational operator: determines whether a specific relationship exists between two values. 
Greater than : >

less than : <

greater than or equal to: >=

less than or equal to : <=

equal to: ==

not equal to: !=



## 3.2 - The if-else Statemnent vocabulary

Dual Alernative decision structure : two possible paths of execution, one path if a condition is ture, and another if its false

Guidelines: if and else clause are aligned, each followed by a block of statements that are consistently indented


## 3.3 - Comparing Strings Vocabulary

ASCII : American Standard Code for Information Interchange

ASCII Representation: uppercase A through Z is represented by numbers 65 -90

Lowercase a through z is represented by numbers 97-112

digits 0 through 9 are stored, and represented by the numbers 48-57, string 'abc123' would be stored in memory as the codes 97,98,99,49,50,51

A blank spaces is represented by the number 32

## 3.5 Logical Operators

Logical operators: a set of operators, which you can use to create complex Boolean expressions

and operator: connects two Boolean expressions into one compound expression. Both subexpressions must be true for the compound expression to be true

or operator: connects two Boolean expressions into one compound expression. One or both subexpressions must be true for the compound expression to be true. It is only necessary for one of the subexpressions to be true, and it does not matter which. 

not operator: unary operator, works with only one operand. The operand must be a Boolean expression. This operator reverses the truth of its operand. If it is applied to an expression that is true, the operator returns false. If it is applied to an expression that is false, the operator returns true. 

Short-circuit evaluation: performed by and, or operators. If the operator can check one expression, sometimes it doesn't need to check the other expression. In an and operator, if the expression on the left side is false, then the entire statement is automatically false, and it doesnt check the other. In an or operator, if the left side expression is true, the statement is automatically true and it doesn't check the other subexpression

##3.6 Boolean Variables

Bool data type: allows you to create variables that may reference one of two possible values, true or false

flag: a variavle that signals when some condition exists in teh program