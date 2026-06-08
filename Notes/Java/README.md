# JAVAFullNOTES

Source: [JAVAFullNOTES.pdf](./JAVAFullNOTES.pdf)

> Text extracted via OCR from the PDF. Minor recognition errors may exist.

## Page 1

“FULL NOTES |

SS

=~ ae
_—..

¥ |

at a Time,
COMPLETE e ORGANIZED e EASY TO UNDERSTAND One Concept
at a Time,
= ee You'll Master
etree ee | g Them All!
| 4) Teeny / a static void main( i, \
! ao EXAMPLES iy String{] args) {

4 keepLearning();
! [J IMPORTANT QUESTIONS | y beConsistent();

| [&f INTERVIEW QUESTIONS ! j neverGiveUp();
| Fel PRACTICE QUESTIONS |
| | AND MORE...

‘

wae owe oe ae eS

. The Best Way To Predict
Your Future Is To
Create It. 9?

ALL THE BEST! © &

---

## Page 2

=
—

+ =
ur

= ~

(4) Introduction to Java

@)
®
@
6
@
@
@
©

Wm,
lg
74
Zz

Java Basics

Operators — in ae oS et Cee

Control Siabletels

OOPs in Java

Classes and Ob pjects ;

Inheritance

Polymorphism

Abstraction

Encapsulation

Constructors

This Keyword

Static Keyword

Exception Handling |

String Handling

Collections Framework ,

Multithreading Pe Se eee 2 ee ie fe

File Handling

Java 8+ Features

Important hidden Chasis ae

Frequently Asked Questions (FAQ)

Practice Questions

Programs,

Tips & Best Practices:

Conclusion

CODE
LEARN
REPEAT

---

## Page 3

"

1. INTRODUCTION To |

Java isa sai

Simple, object- oriented,

Supports inheritance, polymorphism,
_ encapsulation, abstraction.

= » SZ
mee <=

ae Oe a 5 ee -

— platform independent,
Secure, robust and
=— high performance
Programmi
* ee
aT. ss ' Cae Ss ee. ee, se en a ae >
= a Seiad is a ay ulated. object-oriented ! : ae PC Ry ee ;
a 1 . ! ike Sheridan starte ava projec |
— ‘i ae ogee eee WS Sn | (Green Project) at Sun Microsystems. |
Fig (now owned ig Oracle). 1 ! e 1995 : Tava officially released. |
| It was officially released in 1995. : | © 2009 : Oracle acquired Sun Microsystems.
F 2 ‘ | @ Today : Java is widely used for building |
— | web, mobile, enterprise applications
- and more. |
a | | eee ee ee ee ee ee ee ee ee ee af
—— Java programs can run on any system
| that has Java installed.
= ' | ra 7S“
a = ie LE
a [ savac | — | me : Easy to learn, clean syntax,
— ; java. — | aed =e Eoup } no pointer, no operator overloading.
| = ( iler) Platform) ‘
ae -\(Seorck Cala) Oigiaslnde) wees Object-Oriented : Based on class and objects.
1
|
|
)

Platform Independent : Write Once, Run Anywhere (WORA)
using JVM.

-——-— ------- oS - - -—*71

=
. ¢, PE
r

~ JVM (Java Virtual Machine) is an abstract machine.

Secure : No explicit pointer, bytecode verifier,

@ security manager.

|
|
= It enables Java bytecode to run on any platform.
l z | Robust : Strong memory management,
+ [ JVM Architecture | Cy , exception handling, garbage collection.
| :
——® | Class | High Performance : JIT compiler makes Java
_ | Loader faster and efficient.
a \ |
! @) Multithreaded : Can perform multiple tasks
= |
]
1

concurrently.

; ee ee ee ee eee ee ee ee oe = — a

tee ee ee eee ee ee

= public class Hello {
public static void main(String[] args) { | E
— System.out.println("Hello, Java!"); | program. } |
aed i —— | Web Mobile Enterprise Desktop Games

roe — ihe so etc.

~ ee ee a a a He ee ee Re eee eee ee coe

---

## Page 4

// This is a simple Java program
public class Hello { k

public static void main(String[] args) {

“=o
-_

Primitive Data Types
=e

Non-Primitive Data Types

* String
© Array
* Class
* Interface

° Enum

(We will learn in detail later)

Widening (Implicit)
smaller —> larger

Narrowing (Explicit)
larger —> smaller
Example:
int a = 100;
byte b = (byte)a; // type casting

— float —> double
char —> int — long — float

Java is Case Sensitive!
class and Class are different.

_-? Main Method

3 i). Ls Statement
System.out.println( Hello, Java!"); r (prints output)

@ Keywords

@ Identifiers : name given by user

e.g., Hello, main, age
@ Literals : 10, 3.14, ‘a’, “Hello”

6) G€7C): « -

© Operators

@ Separators :

A variable is a container that stores data.

int age = 20; // integer variable

double salary = 55000.75; // double variable

char grade = ‘A’; // character variable

// boolean variable

boolean isJavaFun = true;

String name = “Alice”;

// String variable

= ee age wml,
é Rules for Variables -
MM Must start with a letter, $ or _

MM Can contain letters, digits, $ or _

MM Case sensitive

M Cannot be a keyword

7. COMMENTS IN JAVA

// This is a single line comment
/*

This is a

multi-line comment.

It can span multiple lines.
*/

OUTPUT EXAMPLE

: class, public, static, void, int...

---

## Page 5

‘Ye (2. vartaBLes | xy

A variable is a container
that stores data.

Widening (Implicit)
smaller — larger

byte + short — int + long
— float — double

— flag = aha

char + int — long — float

o
>
5
se
"
“A

J Must start with a letter, $ or _
@ Cannot be a keyword

J Case sensitive

(@ No spaces or special characters

if, if-else
¢ Iteration
for, while, do-while, for-each

, else-if ladder, switch

Scanner sc =
new ner (System.in) | Shorets

» Jump : System.
break, continue, return | String s = sc.nextLine();

int x = sc.nextInt();

true

7. STRING BASICS —

* Strings are immutable.

| 1. Single line
| + Common methods:

|=

|

i

|

|

// This is a single line comment
2. Multi-line

!
|
|
| length() = returns length /*
| charAt(i) - returns char at index This is a
| substring(a,b) - returns substring multi-line comment.
| equals() - compares content } It can span
' toUpperCase(), tolowerCase() - convert case 1 i
‘ | | 3. Documentation | class public — static ~— void int
| Example: /* | if else for while return
String s = "Hello"; int len = s.length(); * This is documentation comment new this super final abstract
is i gel * used for generating docs. | try catch throw throws finally
«/ ! ‘ P
break continue switch case default
et aT SS ar ai
true false null instanceocf

© Java is Case Sensitive (class and Class are different). Finté = (ae Te Tagg ag a.
© main() is the entry point of any Java program. (Ran A , )
@ Every statement must end with a semicolon (;)

© Code is compiled and then executed by JVM. @&~ Ce baxz ee Loe | |

------------------- w Master the basics, and the rest becomes easier. Happy Coding! © - -----—--------

System.

———
3. TYPE CONVERSION

Narrowing (Explicit)
larger — smaller
int a = 100;
byte b = (byte)a;
// type casting

out.print("Hello”);
out.println("Java");

out.printf("Age: Yd
age);

go

KEEP PRACTICING
&
KEEP CODING!

---

## Page 6

int a = 10, b = 3;
ren? atb = 13
a minus b | a-b 7
Multiplication | a times b a*b 30
Division a/b a divide by b 3

(integer division)
Modulus a%b Remainder of i
a/b

Increment a++ or ++a| Increase by 1

Decrement or Decrease by 1

Relational operators return boolean value
(true or false).

(a>0 && b<5) Used in
decision

| True if any one >0 Il b>5 . and
condition is true — (a ” making

conditions. ,,
Reverses the '(a>b) YU
boolean value ,

| conditions are true

__5. BITWISE OPERATORS }

Operator Name Description
10; 2 i ; 0011
& Bitwise AND | 1 if both bits ore 1
; Ma=15 0001

| Bitwise OR | 1 if any one bit is 1 011
Ma=t2 A Bitwise XOR | 1 if bits are different 0110

11 a= 24 ~ Bitwise Complement | Inverts all bits (inverts bits) !
Ha=6 << Left Shift | Shifts bits left a<<1=10 // 1010
>> | Right Shift | 0010

Unsigned Right Shift | Shifts right with

zero fill }

Shifts bits right
a>>>1=2

6. UNARY OPERATORS ©

(oe Name Eaell ipti
+ Unary Plus +a Indicates positive value
- Unary Minus | -a | Negates the value
++ Pre / Post Increment ++a /at+ | Increase by 1
-- Pre / Post Decrement --a / a-- | Decrease by 1

Pe | | Logical NOT la Reverses boolean value
~ Bitwise Complement ~a | Inverts bits

Unary operators
work with only

—> 6 (pre-increment) one operand.
-> 6 (post-increment)

—> 4 (pre-decrement)

—> 4 (post-decrement)

cc eee eee

Understanding ach well
makes your code clean,

efficient and powerful! iy)
int max = (a >b) ?.a:b; // if arb then a else b

---

## Page 7

Make decisions

Control the flow

PP Oe FE Pl ee at your code
of a program based on conditions. :

based on a condition. 2. if-else Statement
1. if Statement

int n = -5;

pe ae
| int marks = 76;

pa ee if (n >= 0) { li
|i = 18; |  System.out .printin(”" Positive”); ream Sy
int age = 18; y -out. prin ositive’ ); | System.out.printin ("A Grade”);
if (age >= 18) { } else {  } else if (marks >= 75) {
System.out.println("Eligible to vote”); System. out. println (" Negative”); Hf Nglhicl: Grade” );
| } else
t } } System. out. println("C Grade” );
~ Lia a.
| int marks = 85; he f9 e e e ee a
ry eRe Ay ; - Selection Statements are used when
if (marks >= 80) { ! we need to make decisions.
System.out.println (” Distinction” ); , of - one condition
} else { e if-else - two possibilities i
System.out.println ("First Class”); : ;
} i$ if-else if-else - multiple conditions |
|} else { | @ nested if —- if inside another if y |
| System. out. println ( Fail") Ce a Pe eae ee ee /
}
2. ITERATION STATEMENTS (LOOPS en’ ea oa ee OF . ae, Fee Ae sk '
(2. ITERATION STATEMENTS (LOOPS) } Fe See di
Used to repeat a block of code multiple times. 3. for Loop
e while : when number of
1. while Loop 2. do-while Loop _ | iterations is not known !
in advance.
1 |
| | © do-while : executes at least
re for : when number of
| iterations is known
in advance.
: )

| inti= 4; 7} —--

| while (i <= 5) { | | for (int i = 1; i <= 5; i++) { 5 .

System. out. println (i); System.out.printin (i); | System.out. printin (i); Fe Print 1 to 5
i++; ive; | } while

L? y |} while (i <= 5);

— ——$————— —

default: System.out.println (“Other”);

|
| // used inside methods
“1 opt: 12 Hosp 1245 1245 I | }
-— a 2 Se |_ 4 aK Fe euggerts String & orem to enti

—— = — = 3 Ss —
Terminates the loop or | Skips the current iteration ” Exits a fren the method ' Selects one option from
switch immediately. and continues with next. and returns a value. Li many etornakines.
| for (int i= 4; i <5; ive) { Ser (int i= 1; 1 <2 5; ioe) { || | int eddint a, int b) { int day = 2; |
| if Gi =s 3) break; | if (i == 3) continue; return a + b; // returns value ha eS en veoh:
System. out. println (i ); i System. out.println (i); } case 2: System.out.println(“Tue”); break |
i i |
i
|

YX { Choose the right control statement to write efficient eT ee @

---

## Page 8

00Ps (Object Oriented P| & Cote Reuabiity
* Programming) isa AAAS — SOE MH Easy Maintenance

Programming paradigm Better Security
based on objects. M Real-world Modeling
& “ e Data (Variables) H Flexibility & Scalability
e Behavior (Methods)

[ 4. ENCAPSULATION } [ 2. ABSTRACTION ] "3, INHERITANCE ANCE _ | f 4, POLYMORPHISM - |

into a single unit. details and showing and methods of another class. differently in different
only functionality.  . situations.

—_—__
ah Ha , { abstract class Vehicle { , a vy Zz ; class Animal {
] ; i 7 abstract void start(); = t. printin(“Eating..."); void sound() {
public int getBalance() { } , pean en aa + 7 System. out. printla(“Animal sound”);
}

, = class Car extends Vehicle { } }
— , void start() { class Dog extends Animal { class Dog extends Animal {
“ wy een hf System.out.printin("Car sterts”); void bark() { void sound() {
" } System. out. println("Barking...”); , System.out.println("Dog barks”);

=> Reduces Complexity => Code Reusability => Flexibility

~ ae or or blueprint oe of a class.
to create objects. Example:

Example:

a
——_— Student si = new Student(); class Animal {
a Py { si.id = 101; int add(int a, int b) { yp stew LEN imal sound”);

Stri ; ‘ si.name = “Alice”; return a + b;

phere { oe. play); } he Dog extends Animal {

System.out..printin(id + * "+ name); int add(int a, int b, int c) { @Override
return a + b + ¢; void sound() {
Output: : ) . System.out. println("Dog barks");

101 Alice

Refers to current

class Student {

ro Student {

int id; : °
Student() { i, 8
id = 101; Student(int id) {
}
}

< TYPES OF INHERITANCE ;

1. Single Inheritance

2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Hybrid Inheritance

ooo xX

(J Reusable Code
J Easy Debugging

MM Modular Structure  [&% Real-world Mapping

class Animal {
Animal() {

Dog() {
super();

=> Resolved at compile time => Resolved at run time

SUPER KEYWORD

System. out. println(“Animal”);

class Dog extends Animal {

"3 super ()

; System. out. printin ("Dog");

ae eee
ABSTRACTION vs ENCAPSULATION

J Better Productivity
© Secure Programs

—Q4 INTERFACE |-. Xx
‘in
Contains abstract I
methods

Interface Animal {
void sound();

}
class Dog implements Animal {

public void sound() {
System.out.println("Dog barks”);

_REAL LIFE EXAMPLE _

= Ge» *)

Objects + BMW, Audi
Sl —» Engine details hidden
Abstraction — Start button
Inheritance > ElectricCar extends Car
—~ Different cars start

1. OOPs makes programs easy to understand.
3. Follow OOPs principles for better & clean code. vy)

---

## Page 9

~CLASSES & OBJECTS =
— INJWA— *

A class is a blueprint or template that
behaviors (methods) that the objects
of that type will have.

Syntax:

An object is a real world entity that is
an instance of a class. It is created
from a class.

Syntax:

class ClassName {
data members;
methods ;

ClassName objectName
new ClassName();

public class Main {
public static void main(String[] args) {
Student si = new Student(); // object 1
Student s2 = new Student(); // object 2

1. Class Declaration

class Student {
int id; // data. members
String name;

si.id = 101; si.name = “Alice”;
s2.id = 102; s2.name = “Bob”;

void display() { // method
System.out.println(id +" "+ name);

s1.display();
s2.display();

|

| FX Objects are created from a class and
consume memory.
FX Multiple objects can be created from

Real world entity

Physical entity

P Created using ‘new’
~ One blueprint (class) keyword
can create many cars (objects).  -

---

## Page 10

‘

}

// additional fields and methods
}

public class Main ; {
Dog d = new Dog();

d.eat(); // inherited method ;
Asleep); // inherited method eg | Sleeping...

d.bark(); // own method

f IMPORTANT POINTS ~~ ¢
Fe Java does not support multiple inheritance
with classes.
Yr Jova supports multiple inheritance
through interfaces.
$e Child class can access all non-private |

INNERITANCE IN JAVA

class Parent { 2——~_ Parent
// fields and methods (Base Class)

class Child extends Parent { <—~ Child
/ inherits fields and methods (Derived Class)

void eat() {
System.out.println(“Eating. ..");

}

eal ste

Eating..,

Barking...

KEYWORDS USED

@ extends : used to inherit a class.
@ super : used to access parent class

@ A class can have only one parent
class.

@ A child class can have any number
of child classes.

Y Use ‘extends’ keyword to inherit
a class.

Y constructor and static methods

---

## Page 11

}

3. Example Program

interface Printer {
void print();
}
interface Scanner {
void scan();
1,
| class AllInOneDevice implements Printer, Scanner {
public void print(){
System.out.println("Printing. ..");

}
public void scan(){
oe ee si

can static void main(String(] args) {
AllInOneDevice d = new AllInOneDevice();
d.print();
d.scan();

making code more flexible and reusable.

Y MULT TIPLE INHERITANCE
IN JAVA =— a

“,,Why Multiple I Inheritance? }

Beware eee
M Increases code reusability
M Promotes better program design

1. Multiple Inheritance - Not possible with Classes |} —.-—{ 2. Multiple Inheritance - Possible with Interfaces
Java. does NOT allow a class to extend more than one class.
class A {

Why?
| class B { It creates ambiguity.
void showB(){} If both A and B
} have same method,
// % Not allowed in Java the compiler gets
class C extends A, B { confused which one

// Compilation Error to use.
io

——<—
; Note ) Multiple Inheritance in Java is achieved using interfaces,

A class can implement more than one interface.

ee

class C implements A, B {
System. out.println("Method A");

}
public void showB(){
System.out.println("Method B");

@ Interfaces have abstract methods only.

@ Class implements multiple interfaces,
so it must provide implementation for
all methods.

@ No ambiguity because interfaces don’t
contain method bodies (default).

| ae tein he Septal ths ere ths, Vega
| multiple interfaces.
w
| we

If two interfaces have same method, class must

implement it once.

Think: Interfaces define what a class should do. 1
| Class defines how to do it. |

---

## Page 12

Why Polymorphism? ~
(4 Improves Code Reusability ‘
M Easy to Extend

[M Makes Code Maintainable

___ Polymorphism means “many forms”. ae
a allows one interface (method) to behave differently )

in different situations.
et ae

1. COMPILE TIME POLYMORPHISM
Same class, same method name, but different
parameters (number, type or order).

2. RUNTIME POLYMORPHISM
Parent and child class have same method name and
same parameters. The child class provides its own

Epeelh | implemen:
dadb Mea { Example:
int add(int a, int b) { class Animal {
return a + b; void sound() {

}

int add(int a, int b, int c) {
return a + b + ¢;

}

double add(double a, double b) {

System.out.println(“Animal sound”);
}
}

}

}
Ne

| m.add(10, 20); WI calls first add() [Example Call: Example Call: }— = .
_m.add(10, 20, 30); // calls second add() | Animal a = new Dog(); // reference of parent, object of child
_madd(10.5, 20.5); // calls third add() a.sound(); “+ // calls Dog's sound() at runtime }

-

Overriding (Runtime)

ea ©

Polymorphism gives you the ability to write ; Potto ,

---

## Page 13

yaad

uu

ef a eT

SLABSTRACTION IN JAVA IN | TAVA |
= i Reston?

Real Life Example
When you drive a car, you
know how to start, stop
and change gears but you
don't know how the engine |

MM Focus on what an object does,
not how it does

| Ways to achieve Abstraction in Java [2

y

71 1. Abstract Class ear {2° Interface 7 Z
A class that is declared with ‘abstract’ keyword. An interface is a completely abstract class.
It can have abstract methods (without body) It contains only abstract methods (by default
—— _——_$$ Rules: +
abstract class Shape { ° Can have abstract | interface Vehicle {
methods. f
void color() { I concrete mathod | © Cannot create void stop();
System.out.println(“Color method”); object of abstract }
class. ae ad
} © Child class must
== f
abstract class Animal { extends -——— [oe wie) opm er gs i
abstract void sound(); “|S | class Dog extends Animal { void start(); = owt ® started"):
aidietia void sound() { void. stop(); } ——— .
System.out.println("Dog barks”); } ee
System.out.println("Animal is sleeping”); | } public void stop() {
>} } — =i System.out.println("Car stopped");
J & J }
(Ta } ! J
f a )

public class Test {
Vehicle v = new Car(); // interface reference, Car object /

static void main(Stringl] args) {
Animal a = new Dog(); // reference of parent, object of child

re

a.sound(); Cia — Kalani); 1! Cor started -
Ras 1 Keinal 'e dasping v.stop(); // Car stopped C4. \_\ 1
> }
eee. } y ul}

Takeaway | It helps in building secure, flexible and easy to maintain applications.
: bE ee ee el ae ee ee eS

---

## Page 14

Why Encapsulation?
[J Protects data from outside access
(data hiding).

@ Provide pubic getter a"

value of private
variables.

public class Main {

private int rollNo;

Sigua Student s = new Student(); T Output:

public int getRollNo() { s.setRollNo(101); Roll No: 101

ee, 0; s.setName("Alice”); —a
ic Stri Name ——

ae ey mA System. out. println("Roll No: " + s.getRollNo());

‘a _— ncienaiis System.out.println("Name: "“ + s.getName());

public void setRollNo(int rollNo) { \

if(rollNo > 0) a
this.rollNo = rollNo;
else {
=

if(name != null && name.length() > 0)
System.out.println("Name cannot be empty");

this.name = name;

s.rollNo = -5; // invalid

Student s = new Student(); |

} AO ae
—_——— ee

we Use private variables and public methods.
W Provides controlled access to data.

---

## Page 15

[% Constructor name is same as the class name.
Gf It has no return type, not even void.

M It is called automatically when object is created.
cs)

cs)

a

It is used to initialize the object.
It can be overloaded.

class Student {
er If we don't write any constructor, Java provides

String name; coe a default no-argument constructor.

// Constructor Constructor called Example:
Student() { 101 Alice class Student {
id = 101; _ int id;
name = “Alice”; String name;
System.out.println("Constructor called”); }
} public class Main {

Student s = new Student(); // constructor called
System.out.println(s.id + " " + s.name);

Student s = new Student(); // default constructor
System.out.println(s.id); 4/0
System.out.println(s.name); // null

@ Constructor is called only once, at the time of object creation.
@ Constructor name = class name.
@ It has no return type.
°
°

Ye Constructor cannot be inherited.
we If we write any constructor, default constructor

It initializes the object.
It can be overloaded.

1. Default Constructor r
=) || See
class Student { class Student {
int id; int id;
String name; Student() { id = 0; }
Student(int i, String n) { Student(int i) { id = i; }

id = i;

"

}

$7 | Constructor is the heart of object initialization in Java. iy) |

|
‘

---

## Page 16

;

w@ To distinguish between instance variables and

ly
7 method/constructor parameters.
— PJ To call the current class constructor. LP
M1 To pass the current object as an argument.

w@ To return the current object from a method.

(T1. To refer current class instance variables | (2. To call current class constructor |

When local variable (or parameter) has the same name We use this() to call another constructor of the same class.

class Student {
int id;
String name;
Student() {
this(O, “Unknown"); // calls parameterized constructor

class Student {
int id;
String name;

void setData(int id, String name) {
this.id = id; // refers to instance variable
this.name = name; // refers to instance variable

}
Student(int id, String name) {
this.id = id;

this.name = name;

}
}

}

3. To pass current object as an argument >) f 4. To return current object from a method ———

We can pass the current object to another method.

class Student {
int id;

class Student {
int id;

void show() {

System. out.println(this); // passing current object
}

System. out.println(s.id);

Student setId(int id) {
this.id = id;
return this; // returns current object

Student s = new Student();
s.setId(101).show();
}

System.out.println("ID: " + id);

si sens Sonia i Sas on oe ee '
this keyword is all about the current object. It helps avoid ambiguity, |
call constructors, pass the object, and return the object. ©

---

## Page 17

[1 To define a method that belongs to the class.
[1 To create utility methods (no object required).

MM To save memory.

It gets memory only once when the class is loaded.

Counter cl = new Counter();
Counter c2 = new Counter();
Counter <3 = new Counter();
cl.show(); // Count = 3
¢2.show(); // Count = 3
c3.show(); // Count = 3

A static block runs only once when the class is loaded.

class Demo {
static int x;

x = 100; // static block

System. out. printin( “Static block executed”);

}
}
class Test {

public static void main(Stringl] args) {
System. out.println(Demo.x); // 100

Per object

i (Automatic)

It can be called without creating an object.

static int add(int a, int b) { // static method
return a + b;
}

}

class Test {
int sum = MathUtil.add(10, 20); // call without object
System. out.printin("Sum = " + sum); // 30

Static methods/blocks can access only static members directly.
To access non-static members, we need an object.
int x = 10;
static void show() {
Example obj = new Example();
System. out. println(obj.x); // OK

class Example {
int x = 10;
static void show() {

WY 1. static keyword is used with variables, methods and blocks.

YY 2. static members are loaded in the memory when
the class is loaded.

YF 3. static methods cannot use ‘this’ or ‘super’.

VY 4. main() method is static because it is called

Ww

A} i alleadl

---

## Page 18

execution of a program and disrupts the normal

try {

// code that may throw exception
}
catch (ExceptionType e) {

// code to handle exception
}

ed .
ran
occurs in

(oe nae i
eas ®

public static void main(String[] args) {
int a = 10, b = O, result;
try {
result = a / b; // may throw exception
System.out.println(“Result: “ + result);
} catch (ArithmeticException e) {

It is used to declare that a method
void check() throws IOException {
// code

System.out.println("Arithmetic Error”);
System.out.println(“Null Pointer Error”);

The caller method must handle the
exception using try-catch or further

System.out.println(“Some Other Error”);

—-_— = SS EE SE Ee

---

## Page 19

length

String s1 = “Hello”;

heap memory)
String s2 = new String(“Hello”);

i

Any modification creates a new string object.
String s = “Java”;
s = s.concat(" Programming”);
System.out.printin(s); // Java Programming
System. out.println(s); // Java (original unchanged)

@ Using == (checks reference, not content)
String a = “Halle”;

String b © “Hello”;

System.out.println(a == b); // true (same pool)

@ Using equals() (checks content)
String ¢ = new String(“Hello”);
System.out.println(a == c); // false
System. out.println(a.equals(c)); // true

|

startsWith(String prefix) : “Java”. startsWith("Ja") // true public class Demo {
endsWith(String suffix) : “Java” endsWith("va") // true public static void main(Stringl] args) {

" "4 $2; // Hello World

String s4 = sl.concat(" ").concat(s2);
System. out.printin(s4);  // Hello World

9 ag) 18
Returns substring from begin index | “Helle”. cubstring(1) // elle
epee) 1A

1@)
1@)

|

equalsIgnoreCase

contains(CharSequence s) “Hello”. contains(“ell") // true
lar

|
i|t
tf

1

Hello” . substring(1, 4) 4/ ell

" equals("hi") // false

H
Hi" . equalsIgnoreCase("hi") // true

“hello” .replace(‘l','x') // hexxo

4! Jona is Programming
sb.delete(5, 8); M1 Java Programming

indexOF(char ch) : “Java” indexOf('a") IA String name = “Alice”; 7 Use string literals for efficiency.
lastIndexOf(char ch) : “banana”.lastIndexOf(‘a") 5 String mag = " Hello " + name ef *} Use equals() for content comparison.
System. out. printla( msg. trim(). toUpperCase());

isEmpty() 2 "" isEmpty() Mt true
toCharArray() “Hi” .toCharArray() //('H", “i’)

split(String regex) : “a,b,c. split(",") //[a","b","c") name. startsWith("Al"));
}
m4 sy
LY Master String handling to work with text data effectively in Java! ©

System.out.println("Starts with Al: " +

System. out. println(“Length: “ + name. length());

methods.

---

## Page 20

\
J It is a unified architecture for representing and
manipulating collections.

MJ It indudes interfaces, implementations ond. algorithms. | \
(J Ik reduces programming effort and increases speed |

| & It is port of java.util package.

© Maintains insertion order. : : @ Follows First-In-First-Out order.

© Allows duplicate elements. intai i © Used for processing elements in a sequence.
© Elements can be accessed by index. ; © Examples: LinkedList, PriorityQueue,
Examples: ArrayList, LinkedList, Vector i i intai ArrayDeque

an Front Rear
ist< . " . s "

public class Demo {
© Keys are unique, values can be 1 igheaba public static void main(Stringl] args) {
© Does not extend Collection interface. List<String> list = new ArrayList<>();
list. add("A ny Fe
© Examples: HashMap, LinkedHashMap, atten, Mee tT Set: [20, 10] (order may vary)
list.add("Cherry”); Map: {A=1, B=2}
System. out.println("List: " + list); <

Set<Integer> set = new HashSet<>();
set.add(10); set.add(20); set.add(10);
System. out.println("Set: “ + set); ‘

Mepes : 0 Order of elements in Set
< ing, r> = new HashMap<>();
nanpest hs th — 7 (HashSet) and Map (HashMap)
map.put("B", 2); Sipe | teh 2
System.out.println("Map: “ + map);

F ; \
Reduces programming effort
| w Tt includes interfaces (List, Set, Queue, Map) and their | * vis
| FY Callcions support generis | | ¥& Provides high-quality, reusable data structures
| [A Fail-fast behavior: If collection is modified while iterating J
\ (except through iterator), it throws ConcurrentModificationException. S| w ll inithatieninitiinihin a

---

## Page 21

Unified Architecture
Generic Support (<Type>)
Iterator for traversal
High performance & quality

List<String> list = new ArrayList<>();
list .add( Hello”);
String s = list.get(0);

Iterator<String> it = list.iterator();
while(it.hasNext()) {
String s = it.next();

If a collection is modified while it is being
is thrown.

List <Integer> nums = new ArrayLlist<>();
Collections. sort (mums); 11 Ascending
Collections. sort (nums, Collections.reverseOrder());
1 Descending

for(String s =: list) {
list.add("X");  // Exception!

© Arrays.aslist() : Converts array to List.

© Collections. singletonList(obj) : Single element list.
© Collections.emptylist()  : Immutable empty list.

© Collections.nCopies(n, obj) = n copies of an object.

“ List<String> List = new ArrayList<>();
list.add("A"); list.add("B™);
List<String> unmod =

Collections. umodifiablel ist (List);

(List String> syncList = ]
Map<String, Integer> syncMap =

// unmod.add("C"); // UnsupportedOperationException

~~ {At Collection vs Map > 122 Wen te Use What?) ——
GI Use LinkedList  -> Frequent insert/delete.
Use TreeSet -> Sorted data.
[J Use HashMap -->—-Fast key-value access.
J) \G Use TreeMap => Sorted by hey.

SLY { Collection Framework = Powerful, Flexible and Essential for Java Developers! 9 |

---

## Page 22

(b) By implementing Runnable interface
class MyTask implements Runnable {
public void run() {
task

}
}
MyThread t = new MyThread(); Thread t = new Thread(new MyTask());
t.start(); t.start();

te

class PrintNumbers extends Thread {
public void run() {
for (int i = 1; i <= 5; ive) {
System. out. printin("Thread: “ + Thread. currentThread().getName()
+" =>" i);
try { Thread. sleep(500); } catch (Exception ¢) {}
}
}
public class Demo {
public static void main(Stringl] args) {
PrintNumbers ti = new PrintNumbers();
t1. setName("A");
t2. setName("8"); 5
ti, start();

Cae en ex = Executors.newFixedThreadPool(3);
ex. shutdown();
,

eta pt (tre

: 2)

Race Condition Deadlock Starvation

cr

---

## Page 23

© The File class represents a file or directory
pathname.

@ It does not allow to read or write data.

Commonly Used Constructors:

@ File(String pathname)

ee ee ee ee

Java uses different streams to handle bytes and characters

import java.io.*;
public class ReadExample {
public static void main(Stringl] args) { public static void main(Stringl] args) {
Ee es ||| Sea | SR
fry + acai od Hi ill
a — == String line; bw.write( “Hello Javal\n");
System.out. println(Line); System.out.println(“Data written successfully!”);
} } catch (IOException e) {
} catch (IOException «) { System.out.println("Error: “ + e.getMessage());
System.out.println("Error: " + e.getMessage());
}
}
pga ns 1 RleWiriter() everuetins the file.
Ae, ie ae 11 Use FileWriter( “file”, true) to append.

E

File f = new File(“example.txt™);
f.exists(); // true or false
f-delete(); // deletes file

f -length(); 1 returns file size in bytes
f .getName(); M1 file name
f.getAbsolutePath(); // full path

File dir = new File("MyFolder™);

System. out. println(name); "Note: Directory must be
(ety to delete.

MJ Always close streams (use try-with-resources). © PlcNotfoundEmeption = fils nck found. & File class represents files and directories.

File f = new File("temp.txt”);
f.delete(); // deletes file

File dir = new File("MyFolder™);

[J Always close the stream after use.

Be File handling in Java makes your application persistent, reliable and data-driven! @ |

---

## Page 24

2

Method Reference

J More readable and easy to use!

Runnable r = ()-> System. out.println("Hello”); MH Provides target type for lambdas

Interfaces can have default method Interf. eg ee ere Old Date API was mutable and not thread-safe.
interface Mylnterface { (e) = a ae { LocalDate today = LocalDate.now(); dea
default void show() { static void display() ( a LocalTune tims © LocalTime.now(); ©
System. out.printin( "Default Method"); Sgetem.cut. printing "Stehic Method"); | | 1 ccsdessTune dabeTume = LecelDateTuns.nsw();
) } DateTimeFormatter . of Pattern( "dd-MM~yyyy ” );
hes cael _—_ Ee
Listelnteger> list = Arrays.eslist(1, 2, 3, 4,5); | | it @ better way. Used for asynchronous programming.
.filter(n -> n % 2 == 0) if (nama. isPresent()) { Cong itetare<Singh Tee =
dghinth +a *a > System. out. printin(name.get()); CompletableFuture. supplyAsync(() -> “Hello Java 8");
} else {
.sum(); . a =

}
; Filter |—> . // Non-blocking, more powerful!
easy [ra | [me > = NullPointerException! ©
_— —— —————— f ————— ee 2 ee

J

list. parallelStream() CQ String encoded = Base64.getEncoder()

-forEach( System. out: :println); -encodeToString(text. getBytes());

(f) vite et aor ti

L Base64. getDecoder().decode(encoded)); wt JS y
Annotations can be applied to any use of types. | | Allows an annotation to be repested. Some new methods added to Collection

interfaces.
© forEach() © removelf()
© spliterator() © replaceAll()

List<@NonNull String> names;

V Helps in static type checking tools

---

## Page 25

INTERVIEW
QUESTIONS |

4, What is the difference between
JRE, JDK and JVM?
== and equals()?

6. What is String Pool?

8. What is final, finally and finalize?
9. What is the difference between Ke

Array and ArrayList? BS
10. What is the difference between  <S=~

3. What is Inheritance? Types?
4. What is Polymorphism? Types?

1. What is a Thread?
2. What are the ways to create a Thread?
start() and run()?

. What is File class?

. How to read a text file?
. How to write into a file?
. What are Streams in Java?

. What are the ways to achieve
} ization?

FileInputStream and FileReader?

Ul
2. What is the difference between

== and equals()?
4. What is a static block?
6. What is the difference between
int and Integer? o

1. What is Spring Framework?
2. What is IoC and DI?

of a bean?

2. What is Functional Interface? A
3. What is Stream API?

4. What is Method Reference?

5. What is Optional class?

6. What is default method in interface?
7. What is CompletableFuture?

WHERE and HAVING?
2. What is JOIN? Types?
INNER JOIN and LEFT JOIN?

5. What is Primary Key and
Foreign Key?
( TIPS TO CRACK THE INTERVIEW }

Ne aS.

[A Keep learning and stay updated!

SHY ( CONSISTENT PRACTICE + CONCEPT CLARITY = INTERVIEW SUCCESS! ©

---

## Page 26

“FREQUENTLY ASKED »

UESTIONS ( Java FAQ)

\,
i 1. Se
(1) What is Java?
Java is a high-level, object- JVM (Java Virtual Machine)
allows Java programs to run @ JDK : Development kit
on any platform. e JRE : Runti ;
@ JVM : Executes bytecode

What is the difference (Z) wat tig Pool? What is final, finally finally —
Achy fr Mais? — é ov O= and finalize()?

Array : Fixed size literals to save memory. ote: yee vais
e Homogeneous elements If same literal exists, it »% block
returns the reference _—" anys

POOL © finalize() : called by

of objects Menerod

concurrently to make
better use of CPU.

_eo f oie he

>
What is Method Overloading What is Garbage Collector?

free up memory
\ Ww !

class Hello {
(J Practice coding public static void main(String[] args) {
(@ Write clean code System.out.println(" Java is Awesome!”);

[7 Revise collections & OOP } \'
M7 Stay calm & be confident 3 ‘a

| @ What is Polymorphism?
| @ What is Encapsulation?

---

## Page 27

1. What is Jawa? Write its key features.
JDK, JRE and JVM?
== and equals()?

6. What is String Pool?

7. Write a program to reverse a String.

. What is File class? 1. What is garbage collection?
2. What is the difference between
final, finally and finalize?

StringBuffer?

2. How do you read a text file?

3. How do you write data into a file?

»

FileInputStream and FileReader?
5. What is buffering?

6. Write a program to copy the

”

[3 Peers} —

1. Write a program to check if a number

1, What is the output? 1. Identify and fix the error: . What is the difference between

ery: oe int x = 5; public class Test { static and non-static method?
5 le ® reget 1S Pere f(xee > 5) © void. main(String{) args) { mt ts ike ana OF tes ?
System. out. printla(x); 9 System. out. println("Hi"); =
3. Write a program to count the number else 3. What is a constructor?

}

4. Write a program to find the largest }
element in an array.
5. Write a program to implement

System. out.println(++x); 4. What is the difference between
5. What is the difference between

deep copy and shallow copy?

2. What is the output?
String s = new String(“hello”);
System. out.printin(s == “hello”);
System. out. println(s.equals( “hello” ));

err(5] = 10; (‘%))

T </> |

te Consistency is the key.

ve Clean code

Ye Confident you
You Can Do It!

3

eee oe oe eae

- You are given a large log file. How will you read it
. Design a class Employee with id, name and salary.

[A Solve a little every day.

[M Focus on understanding, not just answers.
[A Write code by yourself.

(& Try variations and edge cases.

Apply OOPs concepts.

- You have a List of integers. You need to remove
- You are building a multi-threaded application where

multiple threads access a shared resource.

( fv Practice + Patience + Persistence = Success @ |

a a eh

---

## Page 28

rues

=

in

Urey

f
!
|
|

public class HelloWorld {
public static void main(String[(] args) {

import java.util. Scanner;
public class EvenOdd {
public static void main(String[{] args) {

f~
/

import java.util.Scanner;
public class Table {

Check Even or Odd

Table of a Number

Practice makes perfect! Keep coding
Hello World Program (2) Add Two Numbers

import java.util.Scanner;
public class AddNumbers {
public static void main(String{] args) {

System.out.println (“Hello, World!”);
Scanner sc = new Scanner(System.in );

f y
' !
i 1
1 i
| 1
| 1
! System.out.print ("Enter first number: “);
ie ie int a = sc.nextInt(); 1
System.out. print (“Enter second number: ");
int b = sc.nextInt();
| |
|
l 1
\ "
i
i
\ i

int sum = a + b;

System.out.println( “Sum = " + sum);

}

Scanner sc = new Scanner(System.in );

(4) Factorial of a Number
a a —— a a ‘
import java.util. Scanner;

System.out.print( "Enter a number: ”);
int n = sc.nextInt();
public class Factorial {

|
|
|
!
i
;
!
|
!
!
|
1
i

if (n % 2 = 0)
System.out. println ("Even Number”);

else
System.out.println("Odd Number”);

public static void main(String(] args) {

Scanner sc = new Scanner(System.in );
System.out.print( “Enter a number: "):
int n = sc.nextInt();

for (int i = 13 i <= nj ie) {
fact *= i; O
} °

System.out.println( “Factorial = " + fact);

|
|
|
!
|
|
|
|
\
|
| a 4:
long fact 4:
|
\
|
|
\
|
|
|
\
\

|
! ¢ ~“
public static void main(String(] args) { import java.util. Scanner; eRo

Scanner sc = new Scanner(System.in ); ! public class PrimeCheck { ° °
System.out. print ("Enter a number: “); public static void main(String[] args) {
int n = se.nextInt(); | Scanner sc = new Scanner(System.in );

! System.out.print("“Enter a number: “);

is yste P ; 7

for (int i 1; i <= 10; ite) { ; int n = sc.nextInt(); |

if (m <= 1) isPrime = false;
for (int i = 2; i * i <= nj; ive) {
if (n % i == 0) { isPrime = false; break; }

}

System.out.println (isPrime ? “Prime Number” : “Not Prime”); |

‘

!

|

\

!

|

|

|

|
.

System.out.println(n "x" eieree(n*i))s! | boolean isPrime = true;

: |
\

|

\

i

|

|

|

|

|

|

~
See

Se eS SSS SE Ee ee ee. EERE EE a aa.
Fibonacci Series
import java.util. Scanner;
public class Fibonacci { for (int i = 3; i <= mn; ive) {
public static void main(String(] args) { int c = a + b;
Scanner sc = new Scanner(System.in ); System.out.print(c + " ");
System.out.print( "Enter how many terms: “); ae = b;
int n = se.nextInt(); » = <¢;
int a= 0, b= 1; }

System.out.print(a + “ “+ b+” “); }

---

## Page 29

Understand the Basics Solve Problems Actively
Strong concepts are the foundation Start easy, then move to medium
of good coding. and hard problems.

Practice Regularly He Review & Revise
Consistency is the key to Revise important topics and code

improvement.

Write Code Daily (s: Discuss & -_
Daily coding builds confidence | Discuss solutions, ask doubts and
and problem-solving skills. learn from others.

Debug Smartly

Read error messages carefully and — Be Patient with Yourself.

understand the root cause. Every expert was once a beginner!
Le

Congratulations on completing this notes!
You have taken an important step towards | Stay curious Q

becoming a better Java programmer.

aw Keep practicing </>
(J Learn from mistakes %

never stop exploring.
o/? The best view 7 w Be consistent ea
ae we “4

Keep learning, keep practicing and

ml Enjoy the journey Y

eee ee ee ee we we a oe oe ee a a a

Believe in yourself. Stay positive. Keep going.
You've got this! ()
