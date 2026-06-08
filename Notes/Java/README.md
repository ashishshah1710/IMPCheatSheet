# JAVA Full Notes

Source: [JAVAFullNOTES.pdf](./JAVAFullNOTES.pdf)

> Study notes extracted from the PDF. Content is organized by topic with OCR cleanup applied.

## Table of Contents

- Introduction to Java
- Java Basics and Variables
- Operators
- Control Statements
- OOPs in Java
- Classes and Objects
- Inheritance
- Polymorphism
- Abstraction
- Encapsulation
- Constructors
- This Keyword
- Static Keyword
- Exception Handling
- String Handling
- Collections Framework
- Multithreading
- File Handling
- Java 8+ Features
- Interview Questions
- Frequently Asked Questions (FAQ)
- Practice Questions
- Programs and Practice
- Tips and Best Practices

## Introduction to Java

a . SS
J « i) A. INTRODUCTION Ue Java is a. >I
. J ava 5 Fy & am Cy & ma Programming
_—_x_ language.
S=@ °C WHAT IS Java? SSS
an. —=— = a, a Go 3 a Se
s—@m Java is a high-level, class-based, object-oriented 1991 +: James Gosling, Patrick Naughton, !
™ . Mike Sheridan started the Java project
= programming language developed by Sun (Green Project) at Sun Microsystems.
S—— Microsystems (now owned by Oracle). bo
- 1995 : Java officially released.
Le It was officially released in 1995. : 2009 : Oracle acquired Sun Microsystems.
WR nnn nna an----—-- Today : Java is widely used for building
7? = Sey web, mobile, enterprise applications
--34 PLATFORM INDEPENDENT we and more.
= Yo KL
a : Java programs can run on any system . =
that has Java installed. SL. FEATURES OF JAVA FZ
C LS = =) SN
f=2 '= iE learn, clean
in 7 M ! ) ie » Easy to ,¢ syntax,
) = (Compiler) = Platform) ot .
m—am (Source Code) (Byte Code) tj Object-Oriented : Based on class and objects.
_ _ encapsulation, abstraction. !
ame ae 1 Platform I Write Once, Run Anywhere (WORA)
_ JVM THE HEART OF JAVA fF 1
**, ie mf \ @) Secure : No explicit pointer, bytecode verifier, :**
= JVM (Java Virtual Machine) is an abstract machine. (6) security manager.
= It enables Java bytecode to run on any platform.
: G) Robust : Strong memory management,
e j JVM. Architecture ji , exception handling, garbage collection.
= ! apo Execution ate G) High Performance : JIT compiler makes Java
Paneer Verifier Engine Data Area "J faster and efficient.
aT "y gues Multithreaded <= Can perform multiple tasks !
rT i Compiler ; Collector _ Concurrently, !
iD [EXAMPLE _{ w {APPLICATIONS OF JAVA 2
```java
public class Hello { [a aT -_ 3 ,
public static void main(String[] args) { Tis "So a om
System.out.println("Hello, Java!"); ieeeare. IS i ais
```
1 } Ve? Web Mobile Enterprise Desktop Games
> xi, Applications Applications Applications Applications etc.
. Ww { Write Once, Run Anywhere. That's the Power of Java! yy Dy
Se oS ZZ

Sf, a N
re sh) OF F Cy is
a2 5 Strong Program!
= 1. STRUCTURE OF A JAVA PROGRAM ene
: £2. TOKENS IN JAVA}
```java
// This is a simple Java program _-7 Class Definition '
tal , 7 Keywords : class, public, static, void, int...
public class Hello { ke _-» Main Method
= public static void main(String[] args) { Identifiers : name given by user
```
s in("H Java!") Statement e.g., Hello, main, age
```java
stem.out.println("Hello, I"); -+--» 7
```
i ne (prints output) Literals : 10, 3.14, 'a', "Hello"
= ~~+--> End of Method Operators : +, -, *, /, =, >, <, &&, Il
zm ~=F--> End of Class Separators: () {3} 0];,.
### DATA TYPES
al 4. VARIABLES
Primitive Data Types Non-Primitive Data Types A variable is a container that stores data.
```java
but 1 byte 0 String int age = 20; // integer variable
short 2 bytes 0 Array double salary = 55000.75; // double variable
```
=" See 0
```java
lng P "ae OL Class char grade ='A'; // character variable
Float 4 bytes 0.0f Interface boolean isJavaFun = true; // boolean variable
double 8 bytes 0.0d e Enum
char 2 bytes "u0000" (We will learn in detail later) String name = "Alice"; // String variable
=. boolean 1 bit false
```
= gt ge \ -_
7 Rules for Variables
kd [J Must start with a letter, $ or _
Z 5. TYPE CONVERSION ECan contain letters, digits, $ or
Widening (Implicit) Narrowing (Explicit) M Case sensitive
**= smaller larger larger smaller MM Cannot be a keyword :**
=D byte short int long P Example: a
float —» double «nt a= 100:
a ; int a= 100;
har ik tng et as ype eng 7. COMMENTS IN JAVA
### OPERATORS IN JAVA // This is a single line comment
a Arithmetic + * { Marae This is a
Relational ss l= < >= < . " multi-line comment.
Logical && I! oe It can span multiple lines.
OUTPUT EXAMPLE
ernary ? 3 : 7
! ee i Hello, Java! Ly
_ Java is Case Sensitive!
class and Class are different. K¢ 3 :
Y Strong Basics Strong Logic Strong Programmer @& 7

## Java Basics and Variables

4 Ss
<==. JAVA BASICS Complete Guipe = sec ci
] OMPLETE GUIDE <
he tnorou! gy
a! . , aa
### DATA TYPES W {_2. VARIABLES 3. TYPE CONVERSION
+ = =e . oo... A variable is a container
= Primitive _(8"types) Hon Pega ieferenee) st stores data. Widening (Implicit) Narrowing (Explicit)
```java
a byte - 1 byte String es smaller larger larger smaller
_ short 2 bytes ° Array int age = 20; . .
tn int = 4 bytes Class double salary = 5500.75; "Mt Sw" BE long Example:
7 long 8 bytes « Interface char grade = 'A'; int a = 100;
st float 4 bytes o Emm boolean flag = trues char -» int long -» float byte b = (byte)a;
double 8 bytes . we wu) L _String name = "Wilkes — double // type casting
char = 2 bytes (Unicode) \
: boolean 1 bit bens Rules
```
= v7) MM Must start with a letter, $ or _ : Loss of data may i)
MH Cannot be a keyword happen in narrowing!
= M Case sensitive . z
[4 No spaces or special characters
= 4. OPERATORS
_ ; , - e 5. CONTROL STATEMENTS 6. INPUT / OUTPUT
= = Arithmetic + * to Pp , . = a
Relati ge Is = <= ° Selection Input Output
=+— Rotana ° SOS if, if-else, else-if ladder, switch a " secnondhgtabl "lis
```java
_ Logical ae Iteration as se er(Sy stem.in); System. : .
= Assignment = ¢= -= *= /= %= for, while, do-while, for-each ont seal) System.out.println("Java");
__ . Jump int x = sc.nextint(); stem.out.printf("Age: %d",
= Unary ++ + : __ break, continue, return String ss sc.nextLine(); Sy P age);
```
Ternary 2: : en _ CD)
=— _ _ true if (condition) false
Germ ye
```java
+ Example: int max = (a b) ? a: b; FBtock of ) "Block of @)
```
**[Pent :**
, (7string wasics ] [Sieg] [BCOMMENTS] [9 PACKAGES & IMPORT ] ("Bue >)
Strings immutable. <ave ! 1. Single line Package Import Reinent!
° Declare using double quotes. ry a /] This is a single line comment
Common methods: Groups related classes Reuse classes from 4
= : 2. Multi-line and. interfaces. other packages.
JF tength() = returns Length lr "4 Example: Example: !
```java
charAt(i) returns char at index This is a Good code : . +n <ave.util.S
+— substring(a,b) returns substring ! multi-line comment. needs good ' mypack; port java.util. , }
```
equals() = compares content It can span comments! _
i toUpperCase(), tolowerCase() convert case = r i OO !
```java
Examole: : /* if else for while return These words
String s = "Hello": int len = s.length(); This is documentation comment new this super final abstract have special
```
" a "3 ae a __ aa ; 3 used for generating docs. try catch throw throws finally Meaning in
= a */ } ! break continue switch case default ; Java. ps
1 11. MISCELLANEOUS (GOOD TO KNOW) i true false null instanceof
° ae w Coes Sensitive (ae and Class are different). CWeite Once,» JAVA PRO GRAM EXECUTI 10 N FI oN J OO , ,
main() is the entry point of any Java program. ( Run Anus ) , CO KEEP PRACTICING
Gamay Gave) bx (Run)
+ Code is compiled and then executed by JVM. ee Coe) Gad) ee) KEEP CODING!
¥f Master the basics, and the rest becomes easier. Happy Coding! ©) Waa anne nen , YJ

## Operators

Sy "OPERATORS IN JAVATE [oes
\ E77 symbols that
\_Java_J ff ee We \ On operands
```java
per Name Example Result int a = 10, b = 3; Operator Name Example (a=5, b=3)/ Result
```
1, Subtraction a-b aminus b 1 a-b = 7 = Not equal to al=b true
wt Multiplication a b otee ; ae = 30 ! 5 Greater than a>b true
, / Division a/b a divide by b a b ; 3 svison) < Less than a<b false
= Modulus a %b Remainder of ! a%b =1 >= Greater then or a o=b true
equal to
at+ = 10, thena=11 !
++ Increment at+ or ++a Increase by 1 ! <= Less than or a <=b false
```java
Jams ++a = 12 (a was 11) ; equal to
```
/ Zz) OO
ETS, Relational operators return boolean value
pnd (true or false).
### LOGICAL OPERATORS TO
```java
. boolean p = true, q = false; .
& & Logical AND conitene a (a>0 && b<5) true P 4 ; Used in
```
P&RG false : decision
II Logical OR True if any one (@0 11 b5) true pllq true : making and
: conditions.
_ ! Logical NOT Reverses the '(a>b) true 'P false wy,
boolean value No ,
=® 4. ASSIGNMENT OPERATORS } _ { 5, BITWISE OPERATORS } ( Beample: 3
<——<— Example: —_— - i
```java
Operator Example Same As esto. Operator Name Description int a . 5; /1 0101
```
int a = 10; i int b=3; // 0011 i
= = a = 10 a= 10 & Bitwise AND 1 if both bits are 1 bb <1 / !
" —= a-=5 aza-5 a-= 3; /a=12 A Bitwise XOR 1 if bits are different a*b =6 // 0110
```java
Ss = a *= 5 azsat5 a*= 2; //a= 24 Bitwise Complement Inverts all bits wa = ~6 / (inverts bits)
```
_ l= alz5 asa/5 ale a= 6 << Left Shift Shifts bits left Penny oo !
a %= 4; . _ Right Shift Shifts bits ri
6 UNARY OPERATORS } anna
**_—— Oe ; Example:**
```java
e Operator Name Example Description ' int a = 5;
```
+ Unary Plus +a Indicates positive value +a, 5 ! Unary operators
- Unary Minus -a Negates the value p "A HS ! work with only
_ ++ Pre / Post Increment ++a / at++ Increase by 1 +ta 6 (pre-increment) one operand.
Pre / Post Decrement) --a / a-- Decrease by 1 att & (post-increment) ! wr)
= 1 Logical NOT la Reverses boolean value 77a & (pre-decrement)
a-- 4 (post-decrement) i
**~ Bitwise Complement ~a Inverts bits ; ot ! :**
a dl! lt lilt false I ° lelaic =
\ } i a's sy ss
Oe Re
(7. TERNARY OPERATOR } 2 Remember I
a a i Know the
Syntax: aa Precedence
cscition ? canon c panmads PO Understanding operators wel Un mcs
= {_ Sonammon + _ expression" Sxpression'y makes your code clean, () for clarity
Example: efficient and powerful! QD Practice
+ makes
```java
, int max = (a >b) 20:6; // if arb then a else b
```

## Control Statements

ee = F .
288 CONTROL STATEMENTS IN JAVA b> [msm
1 g — . Control the flow
} \ = Ls Control statements are used to control the flow of execution imma, Make your code
oe pJava] of a program based on conditions. Ww , Smart! e
= 1. SELECTION STATEMENTS. y
= Used to execute a block of code "2 'f-else Stat , 3. if-else if-else Ladder
based on a condition. : ,
=a rue
False
```java
= int n = -5; oa
a ag int marks = 76;
os p[ F&rot if (marks >= 90) {
int age = 18; System. out.println (" Positive ); System.out.printin("A Grade");
aS if (age >= 18) { } else { } else if (marks >= 75) {
_= System.out.println ("Eligible to vote"); System. out. println (" Negative" ); ; fete oat printin("D Grade" );
```
= } else
```java
= } } System.out.println("C Grade");
```
= 4, Nested if Statement a
```java
sales int marks = 85; a
= if (marks >= 60) { "@ Selection Statements ore used when
System. out..println(" Distinction" ); if one condition !
```
2 Condition 2 db else f if-else two possibilities
```java
? System.out.println ("First Class" );
```
= : } e if-else if-else multiple conditions
<j i= a= } else { oe nested if if inside another if y
```java
System. out. println ("Fail"); a
```
4 a
+S { 2. ITERATION STATEMENTS (LOOPS) } OY
[_2. ITERATION STATEMENTS (LOOPS) } (Hy Which np waa?)
Used to repeat a block of code multiple times. !
while : when number of
1, while Loop 2. do-while Loop ! iterations is not known !
= in advance.
7 Conditi False 1
<— <> ? do-while : executes at least
Next i once.
**== False iterations is known :**
= __ in advance 5
```java
(int i = 3 ——_ ee a
while (i <= 5) { et 7% for (int i = 1; i <= 5; i++) { pea
sm System. out. println (i); System.out.printin (i); System.out. println (i); Example: Print 1 to 5
```
= } } while (i <= 5); _ J do-while: 12345
,° (Ge Ge) Gee Gente
Terminates the loop or Skips the current iteration Exits from the method ! Selects one option from
switch immediately. and continues with next. and returns a value. many alternatives.
- 2 ese —,
```java
for (int i= 4; i <= 5; ive) C) for (int i= 1; i <= 5; ive) { int add(int a, int b) { int day = 2;
= if . £ (3 switch (day) {
= if (i == 3) break; if (i == 3) continue; return a+b; // returns value ; , "a".
. . ; . ; i case 1: System.out.println("Mon"); break;
= System. out .println (i); 1 System. out. println (i); } case 2: System.out. println ("Tue"); break:
" } } ls I! used inside methods default: System.out.println ("Other"); :
```
cing, // Output: 1 2 Mf Output: 12 4 5 } ae
"] - —_— —-—_—_—_ J) Ve 4 TDK 7+ supports String & enum in switch fy"
Ww Choose the right control statement to write efficient and readable code! ey) ;

## OOPs in Java

core) (OOPS IN JAVA) 2
Programming) is a LAL ASD AAS v4 MH Easy Maintenance
based on objects. 5 a) _ : MM Real-world Modeling
°° AS e Behavior (Methods) '
gee! we Li
**¥ 4 PILLARS OF OOPs [3 :**
ec ee = as QS ee
### ENCAPSULATION 2. ABSTRACTION ] 3. INHERITANCE 4. POLYMORPHISM
Binding data and methods Hiding implementation One class acquires properties One method behaves
into a single unit. details and showing ' and methods of another class. differently in different /
**fa) only functionality. : (2D situations. gt:**
```java
class Account { Aig class . " Ay class Animal { .
ws , System.out. println("Eating..."); . . .
public int getBalance() { } } Pr na-~ 7 System.out. println("Animal sound");
return balance; class Car Vehicle { } ?
oe ; void start() { class extends Animal { class Dog extends Animal {
public void setBalance(nt b) { System.out.println("Car starts"); arn { void sound() {
} , , } System.out.println("Barking..."); , System.out.println("Dog barks");
```
=> Data Hiding & Security => Reduces Complexity => Code Reusability => Flexibility
CLASS vs OBJECT r TYPES OF POLYMORPHISM ,
SO mss "mere Wo A) METHOD OVERLOADING , B) METHOD OVERRIDING
```java
penviats oF eprint Instance of a class. Same method name, Same method in parent
eam se: ae onsen: Example: different parameters. and child class.
Student sl = new Student(); 'class Math { t—~™S class Animal {
int id; acm , System. out.println("Animal sound");
String name; si.name = "Alice"; return a + b; ?
void display() { stdisplay); ERR } closs Dog extends Animal {
. . as a ' int add(int a, int b, int c) { @Override
System.out.println(id + ~ + name); ' ;
} @: return a + b + c: void sound() {
} = Output: ° Ron } ; System.out. println("Dog barks");
```
puss Le= } )
[Ofer 101 Alice $$$
_ Resolved at compile time => Resolved at run time
CONSTRUCTOR THIS KEYWORD SUPER KEYWORD _ {_INTERFACE —. X
Initializes objects. Refers to current Refers to parent Contains abstract I
```java
class object. class object. methods. —\
class Student { r class Animal { m '
int id; class Student { Animal) ( Nid sounds
Student() { int ) Sgtomout.printin( Avimal) nes Dea : ts Animel {
, id = 101; 1, Student Gnt " { class Dog extends Animal { 0 . sibtia" wid soond) {
fT Is-td = te; Dog() { super veut. printin(" s*);
} } K_ this super(); a pe } System.out.printla("Dog barks")
. } System.out.println("Dog"); }
```
TYPES OF INHERITANCE CLASS vs OBJECT ABSTRACTION vs ENCAPSULATION REAL LIFE EXAMPLE
1. Single Inheritance OBJECT ' Car ).
DF Macvtlevel tokertance en ile ABSTRACTION ENCAPSULATION Car er
3. Hierarchical Inheritance Blueprint Instance Hides implementation Hides data Class Cor
4. Hybrid Inheritance Logical entity ogical, enti details Objects + BMW, Audi
No memory Memory allocated Achieved. using Achieved using e Abstraction Start button
allocation abstract class / private variables Inheritance ElectricCar extends Car
bod Zz interface & methods Polymorphism -» Different cars start
6B) (See
+ ' OOPs makes code ADVANTAGES [$ . IMPORTANT POINT [3
NOTE modular, reusable (4 Reusable Code MJ Better Productivity 1. OOPs makes programs easy to understand.
and easy to maintain. M4 Easy Debugging M Secure Programs 2. Everything in Java is an Object (except primitives).
i. MJ Modular Structure [% Real-world Mapping 3. Follow OOPs principles for better & clean code. 7)

## Classes and Objects

Building's o . as a blueprint
blocks of \ and obj
aS \ OOPs! 4 a aes
Lee LN JAVA ——_ owner
from it! 5)
7" 4 1. CLASS + 2. OBJECT SS
```java
1 A class is a blueprint or template that . An object is a real world entity that is {
= defines the properties (data) and an instance of a class. It is created
```
J behaviors (methods) that the objects Suse 4. lads.
of that type will have. , : f
=~ Syntax: BLUEPRINT Syntax: 4 = .
```java
= class ClassName { ClassName objectName = :
data members; am) a new ClassName(); H4 HH )
```
_{ EXAMPLE
( ~~ 2. Creating Objects
```java
1. Class Declaration ™ Class is the public class Main {
a) blueprint of public static void main(String[] args) {
class Student { objects. Student s1 = new Student(); // object 1
int id; // data members = Student s2 = new Student(); // object 2 r
String name; Ly Output:
- si.id = 101; si.name = "Alice"; =.
void display() { // method s2.id = 102; s2.name = "Bob'; 101 Alice
System.out.println(id +" "+ name); 102 Bob
} s2.display();
```
) we )
CaP tar
We Objects are created from a class and T yj eee Blueprint or template Real world entity
$e Multiple objects can be created from Sol. vor 2 Leste ents
ON ee al CS ee
4 oy
ond Each object has its own copy of data Declared using 'class Created using 'new
members. : (~~ One blueprint (class) keyword keyword,
NacennnnmencnccnnnnneY ——~—" Happy Coding!

## Inheritance

} ha Ss . 7 —— "is-a" relationship.
properties and Ve, Why Inheritance? -
methods of ~(ge)- ff Code Reusability } Example: = TD
another class. ° EI Easy to maintain Dog is an Animal
L = &% Extends fanctionality ~
```java
class Parent { &—~.__ Parent lass Animal { Child Class
== class Animal
1 M1 fields ond (Bese Class) void eat() { class Dog extends Animal {
"I } System.out.println("Eating. .."); void bark() {
class Child extends Parent { "<—~ Child wid. sleep() } y "9
```
+ /! inherits fields and methods (Derived Class) ° . &
a // additional fields and methods } os
re ae, yc
L { How it works? } , TYPES OF INHERITANCE IN JAVA
```java
A. public class Main ; { 1. Single 2. Multilevel 3. Hierarchical 4. Hybrid
4 d.eat(); // inherited method Sleep; .
d.sleep(); // inherited method ps?
= d.bark(); //) own method Barking. ., S) [ea
```
L az a
re Dog class inherited [6 a)
eat() and sleep() One parent Inheritance in One parent
== Pio" Anzeial claen ona child. a chain. multiple children.
I and has its own Combination of two
= _ method bark(). Y, ) GR CD + or more ye
3 r RULES
saw te Sunn does net support smultiole inher' extends : used to inherit a class. A class can have only one
a with classes. super : used to access parent class ecg ony parent
7 Fe Javo. supports multiple inheritance (f_F=2) @ A child class can have any number
through interfaces. dass Animal { of child classes.
= Wr Child class can access all non-private : weattgrelbi hie tentater), Y Use 'extends' keyword to inherit
__ private members are not inherited. "woo (ia Contr constructor and static methods
```java
1 super(); // calls parent constructor, Dog Constructor are not inherited. "
```
= L Inheritance makes your code Reusable, Organized and Easy to Maintain!

## Polymorphism

Coaice $2 WAULTIPLE INHERITANCE) [ com
means a class _—— Java does not
ws . ~ multiple inherit
and methods of Seana ses
H Inheritance?
cr OO
Java. does NOT allow a class to extend more than one class. A class can implement more than one interface.
[cas A { x interface A { interface B {
```java
void showA(){} " void showA(); + void showB();
```
4 Why' } )
```java
class B { It creates ambiquity.
void showB(){} If both A and B
} have same method, class C implements 4, 5B { = =
/1 H% Not allowed in Java the compiler gets public void showA(){ Output:
class C extends A, B { confused which one System.out.println("Method A");
// Compilation Error to use. @) } Method A
} public void showB(){ Method B
System.out.println("Method B"); Vv)
```
J terface Scanner { Interfaces have abstract methods only. BEx
```java
<a void sean(); _ Printer Scanner Class implements multiple interfaces, Le
```
je } so it must provide implementation for 10. =
```java
= class AllnOneDevice implements Printer, Scanner { all method \w
```
Le vol 1 j : . "
= P atanensprntilSrtnting..." Class No ambiguity because interfaces don't vad vu
= } AllInOneDevice contain method bodies (default). eS a
< ri ae rs (implements both)
;= stem. out. pri " ing...");
```java
= public static void main(String[] args) { ;
" AllInOneDevice d = new AllInOneDevice(); Ye A class can implement any number of interfaces.
= d.print(); Sy A class can extend only one class, but implement _
```
Satta Printing. . multiple interfaces. y . ,
```java
= } = . a Ty If two interfaces have same method, class must fe 1@) af
= (wots Multiple Inheritance in Java is achieved using interfaces, Think: Interfaces define what a class should do.
```
1 . making code more flexible and reusable. i) Class defines how to do it. @)

L ee \ .. wy
TT ragrerpin' ORPHISM IN ; uF
rare = POL AVA [-
4 pillors of OOPs. ae ee —_ i Why Polymorphism'?
Ss 1. Encapsuiction 5 _ Polymorphism means "many forms". y .
= 3. Inheritance _ ee ieee auton gy) , As BS Easy to Extend
= 4. Polymorphism @) *® different situations & Wi g Makes Code Maintainable
L i TYPES OF POLYMORPHISM
= 1. COMPILE TIME POLYMORPHISM 2. RUNTIME POLYMORPHISM
1 Same class, same method name, but different Parent and child class have same method name and
+ parameters (number, type or order). same parameters. The child class provides its own
{ Example: } _inieme
```java
int add(int a, int b) { { Use: class Animal { peal =
return a + b; te void sound() { {_Use:
= } Compiler decides System.out.printin("Animal sound"); JVM decides
return a + b + ¢; at le time. } at runtime.
= double add(double a, double b) { class Dog extends Animal { \\
return a + b; void sound() { ; i
```
= O e) L }
; = Call: } Ze } 7
```java
Math m = new Math(); —_
m.add(10, 20, 30); // calls second add() Animal a = new Dog(); // reference of parent, object of child
5 _m-add(10.5, 20.5); // calls third add() j a.sound(); S // calls Dog's sound() at runtime
```
Ly [Kev DIFERENCE } yp [REAL LIFE awauey J}
Feat Compile Time Polymorphism Runtime. Polymorphi Overloading (Compile Time) ! Overriding (Runtime)
iz One person having multiple ways Different persons doing the
yO Aso Called Methad Overloading Method Owrrding to do a tack ae task in their my
= a ~ Class 40° Cas) I speak
To i [anaes pee [eras RS) ar
rt (Fe Fe
1 Polymorphism gives you the ability to write : ste { Motto: One interface,
flexible and reusable code. te big comeenten: many implementations! ©)
= za Overriding is specialization. MO _

## Abstraction

ra 7 "
im Abstraction is \ 4 ABSTRACTION IN JAVA
ee Za 2 : 7
hiding nv, Why Abstraction? aia
detoils and ng = MH Improves security When you drive a car, you
only essential Easy to maintain know how to start, stop
features to the user. MM Focus on what an object does, and change gears but you
y not how it does don't know how the engine Y ££ ff DN
=-8 x] Ways to achieve Abstraction in Java &
=-8 71.1. Abstract Class f-——SSSCSCS;7«;C 2. Interface
=-68 A class that is declared with 'abstract' keyword. An interface is a completely abstract class.
Tt can have abstract methods (without body) It contains only abstract methods (by default
```java
<8 and concrete methods (with body). .————_.. public and abstract). ; .
abstract class Shape { Can have abstract interface Vehicle { All methods are public
+e abstract void draw(); // abstract method and non-abstract void start(); dnd eieteact.
void color() / method. void. stop(); All variables are public,
```
<-8 Of ; concrete " Cannot create ; static and final.
```java
System.out.println("Color method"); object of abstract } J Class impl
class. interface usi
```
} hy
e Child class must 'implements' keyword.
ee feasts)! [ae ee
```java
abstract void sound(); s dlass Dog extends Animal { void start(); public void start() {
sin wid sleep() { void sound() { void. stop(); System.out.println("Car started");
<9 System.out.println("Animal. is sleeping"); mnt ets perks) public void stop() {
y} 2 System.out.println("Car stopped");
```
[cs wz Wd
```java
Pe vrata vod main ©) ares) { public class Test { }
eseandC 11 Dog barks v.start(); // Car started "
a-sleep(); 11 Animal is sleeping by yy v.stop(); /! Cor stopped ('Ai\
```
eT 3a ee...
K Ww "—— a —_,_-———_ SOo'> SO V's
ey Use Abstraction to hide unnecessary details and show only what is important.
Takeaway It helps in building secure, flexible and easy to maintain applications. A)

## Encapsulation

**a VAT:**
Ley Goriables) ont a i. Cr
methods eae Why Encapsulation? ! Data _—_ Methods
**= ails anit [4 Protects data from outside access (variables) eu :**
3 i Anne Ape S
< of the object : MJ Helps in code reusability.
**components: EI Better control over data. (4) :**
= into a single unit. }
i? < How Encapsulation is Achieved? [3
= @) Declare variables Provide public getter G) Provide public setter ) Access and modify
she as private . methods methods dota, through methods
private variables can To read (get) the To update (set) the Variables are accessed
be accessed only within value of private value of private and modified only
```java
the class. variables. variables with through getter and
; class Student { public class Main {
rivate int rollNo; // private variable . a
<—Ft orivete String name; pre Dota ie hdd public static void main(String[] args) { T _
=X public int getRollNo() { and can be s.setRollNo(101); Roll No: 101
, return rollNo; accessed only s.setName( Alice"); Name: Alice
```
=— . . Name through methods. \
```java
eres String et Q { System. out. println("Roll No: " + s.getRollNo()); LY
setter sith walidati System. out.println("Name: " + s.getName());
public void setRollNo(int rollNo) { ' }
=—t if(rollNo 0) }
this.rollNo = rollNo; ae
```
lse ot "eo £ f ,
```java
+o] System. out.printin( "Invalid. Roll. No"); What "happens _without Encapsulation?
FA Pa ait setName tring name) é 4) i Hos class Student { A Student s = new Student();
Pie = name; VY wed public int rollNo; Direct access s.rollNo = -5; // invalid
7 System.out. println( "Name cannot be empty"); = public String nome; No security s.name = ""; // empty
```
} 3 —» Invalid data Ke
sp } _ possible MS >)
hy -———{_Key Points SL Remenber! A Real Life Analogy
tr Encapsulation = Data Hiding + Abstraction emember: wily the medicine inside
SQ wW Use private variables and public methods. Never expose your data directly, ) capsule protects ane

## Constructors

**SO. "(CONSTRUCTOR IN TAT:**
Remar C ad AVA L
TP Sava is Se \ Lo a
= _ bo initialize objects. Key Points oo initialize the object
It is called a, M2 Constructor name is same as the class name. . at the time of
7 automatically ai _ ° MM It has no return type, not even void. y creation.
7] MM It is used to initialize the object. \ Se 5
= ( BM We cannot coll it explicitly. i) ae
) BM Tk can be overloaded. 'ITT
r { Default Constructor }
```java
+ class Student { ;
int id: If we don't write any constructor, Java provides
```
== Sectna name: c ra ) a default no-argument constructor.
11 Constructor Constructor colled Example: =
```java
= id = 101; _ int id; provided by Java
name = "Alice"; String name; has no parameters
= System.out.println("Constructor called"); } and empty body.
aL public class Main {
7 public static void main(Stringl] args) {
1. rave cate wed main(String] aras) { Student s = new Student(); // default constructor
; Student s = new Student(): Y coma led System.out.println(s.id); // O
= System.out.printin(s.id + " " + s.name); ) System.out.println(s.name); // null
```
I (Things t Remember } =
Constructor is called only once, at the time of object creation. we C tor be inherited. I,
aH Constructor name = class name. 5 '
It has no ret type. Ww If we write any constructor, default constructor . 7
== It initializes the object. [F=] is not provided. . .
It can be overloaded. __J $e Constructor overloading is possible. —_
(Ne-erg ) 2. Parameterized Constructor Overloading
```java
= class Student { class Student {
class Student { int id; int id;
= int id; String name; Student() { id = 0; }
Student() { Student(int i, String n) { Student(int i) { id = i; } Multiple
a id = 1; id = i; Student(int i, String n) { tors
```
} (im. nome = a3 vim id = is with different
```java
i parameters } System.out.println(n); parameters
```
$7 Constructor is the heart of object initialization in Java. )

## This Keyword

Lo (umes THIS KEYWORD IN Jayay~ (m=
ae keyword hoe . f "this" as a
thot refers to y te =e it ff y reference to
+ method or ly M To distinguish between instance variables and
whos \
= i thod/ constructor . °
= constructor 's S me parameters '
iz being called). E4 To call the current class constructor. vStg q
= YD To pass the current object as an argument. Or)
```java
MJ To return the current object from a method. Nog .
When local variable (or parameter) has the same name We use this() to call another constructor of the same class.
+ ae . class Student {
int id; : String ;
_— String name; Without this, a )
```
Java. thinks Student() { this() must
```java
_— void setData(int id, String name) { we are trying this(0, "Unknown"); // calls parameterized constructor f 4) yp. gy
= this.id = id; // refers to instance variable to assign the } statement in
this.name = name; // refers to instance variable parameter to Student(int id, String name) { the constructor.
} waetrl this.id = id; , yy)
J. \ } , this.name = name;
```
= KM
i se US 2 SSC Ee 4. To return current object from a method [
= We can pass the current object to another method. Useful in method chainina.
```java
a class Student { class Student { +f :
void show() { Student setId(int id) {
System.out.println(this); // passing current object host) this.id = id; 7m 0:
} return. this; y object s.setId(101).show();
: void display(Student s) { display(this) } W
System. out.println(s.id); void show() { iL
} System.out.println("ID: " + id);
```
} this refers to }
current object (s1) }
ao \_ a _fy fh ff ty a py
= this keyword is all about the current object. It helps avoid ambiguity, ! this is mostly used in Vf
= Te oJ call constructors, pass the object, and return the object. instance context ale Uf

## Static Keyword

ta use for memory . aa - J
ike \ ap
i been on to ofl [1 To share common data among all objects. S -= shared by all
rother e.@ vu objects of the
```java
te objec: Y [1 To define a method that belongs to the class. \ y 4 ya 4
z B [4 To create utility methods (no object required). 9 SS ak o class! }
```
an . , [To save memory. SF , 1
d 1. Static Variable (Class Variable) } 2. Static Method (Class Method) ji
```java
= A static variable is shared by all objects. A static method belongs to the class.
It gets memory only once when the class is loaded. It can be called without creating an object.
_ static int count = 0; // stotic vari Example: static int oddi(int oy int b) {17 static mathod
Of Counter cl = new Counter(); , return a bj
```
= count++; «sama variable chared COUOH 2 =e Comte' }
```java
} Counter <3 = new Counter();
el.show(); // Count = 3 class Test {
1, System. out. println( Count = " + count); ¢3.show(); // Count = 3 int sum = MathUtil.add(10, 20); // call without object
5 , } System. out. printin("Sum = " + sum); // 30
```
+ All objects share }
the same 'count'! 9 cr
3. Static Block 4. Can static access non-static members?
a A static block runs only once when the class is loaded. Static methods/blocks can access only static members directly.
a a Demo { To access non-static members, we need an object.
class Ex
i {(onteat dase Cramp (QR Soe, Swe
```java
< x = 100; // static block : int x = 10; oy
, nes os . static void show() {
System. out. printin("Static block executed");! Static block executed static void show() { Evade 4h) now Examglats
, ; } 100 System. out. println(x); // Error! System. out. printin(obj.x); // OK
class Test { "ee } }
public static void main(String[] args) { r
1. System. out.println(Demo.x); // 100
" } Static belongs to the class,
```
(Quick Summary [_Tnportant Notes
Member Belongs To Memory Access Call Using WY 1. static keyword is used with variables, methods and blocks.
T static variable Class "a aoe, Shared ClassName. varName Y 2. static members are loaded in the memory when .
oo Runs once VY 3. static methods cannot use 'this' or 'super'. Vi
static block Class when class ( Automatic )
. is loaded YP 4. main() method is static because it is called &
L non- static Object Rach okject Per object obj.varName / obj.method() by JVM without creating an object. :

## Exception Handling

; is mechanis 0 \ J , 6
handle ae he = Why Exception Handling? - 4
errors $0 ' [J Maintains normal flow of the . 6 4
" flow of the vi, ae A
program car ~ & Helps in displaying meaningful messages. Gr) \ YF ready to handle
mointained. TH Helps in logging and debugging. ¥ them!
7 What is an Exception? } q Types of Exceptions
= An exception is an event that occurs during the 1. Checked E ions Unchecked Excenti
= of program and disrupts the Checked at compile-time. Checked at runtime.
nod Maeteutione: A\ Must be handled or declared Not mandatory to handle.
=— using throws. e Example: NullPointerException,
. : IO ion, SQLExcepti ArithmeticExcepti
de, Syntax } Example: I0Exception, ception ception
try { May throw
/1 code that may throw exception a as Flow of Exception Handling }
```java
= catch (Exception Type e) { A JVM creates Finds the Exception
```
/1 code to handle exception exception. on exception —>] matching handled and
3 ; Problem object catch block normal. flow
in ti
a } If no matching catch block is found,
the program terminates abnormally. @)
```java
class Demo { —q Common Exception b
public static void main(String[] args) { , : Classes
result = a / b; // may throw exception C b divide Thrown for arithmetic errors, ¢.g., divide by zero.
" System.out.println("Result: " + result); wore an ei .
```
: ST ae ty wet at nf
} continues IOException Thrown for input/output errors.
```java
7 System.out.printla("Program continues normally."); normally, & ClassNotF hen a clase ie not found. LF
```
ee er a (Bast Prats}
Ce ES Oe NS OE. It is used to that a
tr : .
» 1) vig ode moy throw on "on. M Always handle specific exceptions.
ee ned era*y; cuaad ton vod check() throws OEscepin ( SF Newer igre exceptions
```java
= } catch (NullPointerException e) { top to bottom. M1 code MJ Use meaningful messages.
System.out.printin("Null Pointer Error"); First matching }
2 System. out.printla("Some Other Error"); executed. exception using try-catch or further
```
= fe (Remenber! Good exception handling makes your program reliable, user-friendly and easy to debug. yy)

## String Handling

i ol, & Strings are widely used in real applications. ay. String handling
Y BJ Java provides a rich set of methods in —_ a strings.
A ss String class to handle strings easily. iG ¥
Tp Ce eeting ig) [Romy Wad Sg Ma) ,
T Using string iteral (stored in String constant pool) Method Description' = Example
an lrman
Leo aan antes tg
wading, $e
1 sd] [ees
ye Seen ate 'imetand [ene a tan)
Once created, they cannot be changed. 0
Le ee
```java
System. out.printin(s); // Java Programming
J stem.out.printin(s); // Java (original unchanged) = F
Surtees printinGs)s 1 teen Gongnel enone 5, Sting Conpor 6. String Builder vs String Buffer }
L 4, String, Coneabanakin. Using == (checks reference, not content) StringBuilder
String s2 = "World"; Used in single-threaded Used in multi-threaded
i String s3 = sl +" " + 82; // Hello World Using equals() (checks content) eswiroamants environments
String = new String("Hello"); Pn sn seen,
@ Using concat() method System. out.printin(a == c); // false te sh new Java"); }
String s4 = sl.concat(" ").concat(s2); System. out. printin(a.equals(<)); // true sbvinsert(5, is"); // Teva is Programming :
System. out.printin(s4); // Hello World sb.delete(S, 8); // Java Programming
Always use equals() to compare content! sb. reverse(); Hf grimmargorP avaJ 4 }
@ startsWith(String prefix) : "Java". startsWith("Ja") // true public class Demo { A Stri ore i table in Java.
a indexOf(char ch) : "Java".indexOf('a') "1 String name = "Alice"; _ MI Use string literals for efficiency.
lastIndexOf(char ch) : "banana". lastIndexOf('a") // 5 String msg . Hello : + name ef; J Use equals() for content comparison.
aes de ace System. out. printla("Length: " + name. length()); String class provides many useful
```
toCharArray() : "HK . toCharArray() CH ' i] =
System .out.printin("Starts with Al: " + methods.
```java
split(String regex) "a,b,c". split(",") //["a","b","c") name. startsWith("Al"));
T He Master String handling to work with text data effectively in Java! iy)
```

## Collections Framework

(COLLECTION FRAMEWORK IN Java
provides a set of : "Ae
= dasses to tore \ Ef It is a unified architecture for representing and oF " Collections
manipulate vist maniguleting csllections =
ond i - ° { @. 5 make it easy
1 groups of objects J GF Bt includes interfaces, implementations and algorithms. {\ =] to store, access
efficiently. yY & Ik reduces programming effort and increases speed @T) ss and process
```java
\ UM it is part of java.util package. ; , '
```
ten ag
List Set Queue HashMop LinkedHashMap TreeMap Hashtable
ra) Be) '
} 4 1. List (Ordered) ) 2. Set (No Duplicates) § 3. Queue (FIFO) f
Maintains insertion order. Does not allow duplicate elements. Follows First-In-First-Out order.
I Allows duplicate elements. Does not maintain any particular order Used for processing elements in a sequence.
Elements can be accessed by index. (HashSet). Examples: LinkedList, PriorityQueue,
= Examples: ArrayList, LinkedList, Vector Some implementations maintain natural ArrayDeque
) order (TreeSet).
Index: 0 1 2 3 . , Front Rear
tk 1 @
+ Stes dei tye pi mgt frm ae
```java
© Does not extend Collection interface. List <String> list = new ArrayList<>(); List: [Apple, Banana, Cherry]
```
Examples: HashMap, LinkedHashMap, Tora P es, Set: [20, 10] (order may vary)
```java
<a TreeMap, Hashtable list. add("Cherry"); Map: {A=1, B=2}
System. out.println( "List: " + list); = 7
Key Value Set<Integer> set = new HashSet<>();
set.add(10); set.add(20); set.add(10); Note:
= System.out.println("Set: " + set);
P [292] Neha Mep<String, Tnteger> map new HashMapc>(); (rate of samants in Se
= , map.put("B", 2); may vary. i)
System.out.println("Map: " + map);
```
[J Tk includes interfaces (List, Set, Queue, Map) and their ' y
FD implementations. WE Improves. performance qep
LA Collections support generics. WW Provides high-quality, reusable data structures 4
=D OF Fail-fast behavior: If collection is modified while iterating a
(except through iterator), it throws ConcurrentModificationException. = YP Easy to maintain and extend :
Sey Collection Framework = Ready-made data structures for efficient programming! QD

re COLLECTION FRAMEW )
tie Framework provides Se
Bo Oo gare ond maine — gi Key Po
cm grours of = a see ! It is part of Unified Architecture
efficien™s VY CY Increases code reusability and reliability = \\ jova.util Generic Support (<Type>)
= (Af Provides high-performance data structures. 9 ts package! ° Fad-Fast Behav:
a, / a one ! 1 <2 Iterator for traversal
. ee we j _ Y © High performance & quality
: >: nome 1. Hierarchy Overview } __
<a' K Key {All collection classes
= Y) '\ (iractly or indirectly)
<i Collection<E> "K.V
(interface) pier A
dm List<E> Set<E> Queus<E> ,
(ordered) (no duplicates) (FIFO) HashMap LinkedHashMap TreeMap Hashtable
= (unsorted) (insertion order) (Sorted by key) (legacy)
. PriorityQueue Deque<E> ;
eee) Se ES) (ES) chy =
TreeSet i
L es ste
{2 Important Inarfum 3 Retr Crome) a
_ Iterable<E> =: Provides iterator() method. Iterator is used to traverse the elements. Collection framework uses Generics
Collection<E> : Root interface of List, Set, Queue. e It is fail-fast (throws (added in Jova 5).
```java
RlsiE> + Ordered collection, allows duplicates. f List<String> list = new ArrayList<>();
e Set<E> : Unordered collection, no duplicates. Iterator<String> it = list.iterator(); list. add("Hello");
Queue<E> : FIFO order. while(it.hasNext()) { String s = List. get(0);
i Deque<E> : Double ended queue. String s = it.next(); ~*~
```
° : i // process element ( Provides type safety
715. Fail-Fast Behavior }——~ -[ 6. Useful Methods (Examples) }
```java
Jig tranred o ReationEncopt "List <Integer> ums = new ArrayList <>(); Works for List
```
pe? jose Fremont [ Rnome cence mma, mma); mmnatsatd; ond SO
. . elaments ore
**s(o-aqual"A°D) fase] Parmenter of ements Clacton srt nme, Callin rernOrtw(:**
Meads 1 Cecepton! cllection is empty 11 Descending
Bo aux
dy 8. Synchronized Collections (Legacy) p< 9. Unmodifiable Collections p——— _- 10. Special Collections
Hecti in licati Creates read only ootlactions. Arrays.aslist() : Converts array to List.
```java
List<String> List new ArrayList<>(); Collections.singletonList(obj) : Single el t list,
i, List<String> syncList = ] List.add("A"); list.add("B™); i) .
: Collections.synchronizedList (new ArrayList<>(); List<String> unmod = @] Collections. emptyList() : Immutable empty list.
Map<String, Integer> syncMap = ée) mated 1 engyt Collections.nCopies(n, obj) : n copies of an object.
;: Collections. synchronizedMap(new HashMap<>()); /f urmod.add("C"), // UnsupportedOperationException
```
LO eS
**4 11. Collection vs Map 12. When to Use What? R :**
Collection (List, Set, Queue) I Use ArrayList Fast access, more reads. Q Remember! :
**= GL Woe Linadtst Frege rte agra s:**
GL Ue Hast Me alan, fst prt, Che he righ nla
= Sn iit Std te Oe hae
Extends Clacton interface. Not a part of Callin SF Use Prion "> Priority based processing, HI Handle exceptions.
. —srs (J Use HashMap = ->Fast_key-value access. EI Follow best practices! &
(Examples: ArrayList, HashSet Evang: Hash, Tretap GJ Use TreeMap Sorted by keys.
er { Collection Framework = Powerful, Flexible and Essential for Java Developers! }

## Multithreading

, ce il
multiple threads See 2 =e =. _\
cy un eoncurreniiy =~ "i Why Multithreading?) —~~, / vi
= Me j
A thread is a lightweight sub-process.
i, 3. Ways to Create a Thread 4 4. Important Thread Methods }
—I = e
```java
(a) By extending Thread class (b) By implementing Runnable interface { Method Description
```
= , Starts the execution of the thread. qs
das Mle end Tad ( ca Miah prs Raa (
```java
public void run() { public void run() {
```
a, Pauses the thread the A
7? : hve"
```java
pina = na Myra; Than & +n hades) Dt al
at t.start(); t.start(); the run() is just
'- class PrintNumbers extends Thread { Output
+ for (int i = 1; i <= 5; ive) f ans, Alp a we may get inconsistent data.
```
= *"-p " « i); Thread: A 2
```java
' try { Thread. sleep(500); } catch (Exception e) {} Thread: A 3 synchronized
} Thread: B 3 class Counter { = wt
= Thread: A 4 private int count = 0; whose
public class Damo { Thread: B 4 . hronized void increment() { can access
public static void main(Stringl] args) { Thread: A 5 re we the block/method.
PrintNumbers ti = new PrintNumbers(); Thread: B S , at a time.
PrintNumbers t2 = new PrintNumbers(); . }
t1. setName("A"); ic int getCount() { return count; }
1 t2. setName("B"); (ana wir (A
tl. start(); vary because threads
```
= ' Fe Theasd Cammunioation 4 8. Daemon vs User Thread 7?
1 Threads can communicate using wait(), notify() and notifyAll(). User Thread Daemon Thread 'O}
**lockedObj. 0); ff relonses wets, e e :**
```java
lockedObj.notifyAUl(); // wakes up all waiting threads Rs te . Example: main thread. ° Example : Garbage Collector.
```
9. Advantages 10. Best Practices 11. ExecutorService (Thread Pool)
```java
" Makes applications more responsive. of Minimize use of shared data. == ExecutorService ex = Executors.newFixedThreadPool(3);
Better utilizati CPU. _ Fully. ll ef ex.execute(() System.out.println("Task 1"));
ot a 4 BE Use synchronization ] & ex.execute(() System. out.println("Task 2"));
[J Allows background tasks to run Uy Avoid deadlocks. a ex. shutdown();
```
J without blocking main flow. sy Use pools ( Service) = 4 a
12. Common Problems R 7
Race Conditi Deadlock Starvation Livelock [J Threads run am! rrently,
DEY (Multithreading makes your Java programs faster, smarter and more efficient! }

## File Handling

ey update ond ,-— Ores --~,
, p Ef Data con be shared betomen programe. Or) =) treated as a ? es fl
7 Sg came: SG, cs MS ME ee
The File class represents a file or directory
ts CommonLy Used Constructors: _ —_ Always close
a File(String pathname) —7 .txt, java, .csv, .log dat, .exe, .mp3, . jpg aa
= nai and Writers) and OutputStream) yy
Kaiten (3. Seon low}
mr createNewFile() creates a new file __
isFule() checks if it is a file Byte Streams Character Streams
Po isDirectory() checks if it is a directory (For binary files) (For text files)
```java
1+ list() returns files in a directory _ ; nas
OO OutputStream base class for writing bytes Writer base class for writing characters
```
'_ (Te Why two types? OF
R \_sffisentty eoverding to the type of dete
= 4. Common Classes { 5. Reading a Text File (Example) -< 6. Writing to a Text File (Example) }
```java
ak Description public class ReadExample { public class WriteExample {
R os Giutnedealin br ams Eafe public sate wed main(String} org) (
4 : bytes try (BufferedReader br = new BufferedReader try (BufferedWriter bw = new BufferedWriter
= String line; bwwrthel"Malle Jeval\n");
while ((line « br.readLina()) null) { bu write( "File handling is easy.");
\ System.out. println(line); System.out.printin("Data written successfully!");
```
nr Rn tre f= Re] Syptam.ok pita Eror: + egutage
FO rowae we ornare wee] ? )
rela
=) BufferedWriter // try-with-reseurces automatically closes the stream. Aa 14 Pileldiriter() ovenarttes the file.
if vendLinal) reads ona line ok « time. = Hf Use FileWriter("fila", trua) to append.
9 47. Working with Files (Using File Class) } { 8. Directory Operations } { 9. Deleting Files / Directories }
```java
= File f = new File("example.txt™); Fille dir = new File("MyFolder™); File f = new File("temp.txt");
f exists(); / true or false dir.mkdir(); // creates single directory f.delete(); // deletes file
Toy f-createNewFile(); // creates file dir.mkdirs(); // creates multiple directories
f delete); 1 deletes file Stringl) files = dir.list(); // list files in directory Bile dir = new Filel "Myfelder");
f .getName(); M1 fle name System. out. printin(name );
```
. , Note: Directory must be
- 10. Best Practices Jd 11. Common Exceptions 12. Summary }
[4 Always close streams (use try-with-resources). FileNotFoundException file not found. [I File class represents files and directories.
EX Use Buffered: streams for butter performance. IOException L input/ error. [4 Streams are used to read/write data.
17 [I Handle exceptions properly. f a ;
;* wi Always close the stream after use.
c a4 _ File handling in Java makes your application persistent, reliable and data-driven! iy) J

## Java 8+ Features

brought mons f =
_ Perf. ; te. future!
iw fraltensliiy t be used An interface with exactly one Shorthand notation of lambda
i as a method argument, or code abstract method is called a expressions.
```java
I Before (Anonymous Class) @FunctionalInterface . ;
public void run() { face My ae 2
a, System. out. println( "Hello" ); void show(String msg); e— Method Reference
' } Wf } list. forEach (System. out: :println);
```
After (Lambda Expression) MM Can be used in lambda expressions
. Runnable + = ()-> System.cut.println("Hello") H Provides target type for lambdas BE More and easy to use!
Lag {Doak Mate Tfme {5 Sc Ras ere} ~) -{ 6, Now Dla wd Tne AP (nts) }
Interfaces can have default method Interf can have static methods. Old Date API was mutable and not thread-safe.
```java
i implementation. Java 8 introduced new API.
i default void show() { static void display() t LocalTime time = LocalTime.now(); —ia es
System. out.printin( "Default Method"); System.out.println( "Static Method" ); LocalDateTime dateTime = LocalDateTime.now();
```
i } } DateTimeFormatter fmt =
```java
} } DateTimeFormatter . of Pattern ( "dd-MM-yyyy " );
```
'in a
Process collections of objects in a functional way. Helps to handle NullPointerException
```java
FD ListeInteger> list = Arrays.aslist(1, 2, 3, 4,5); it o better way. Used for asynchronous programming.
int sum list. st O Optional<String> name = Optional.ofNullable(getName());
Tx filter(n -» n 2 == 0) if (name. isPresent()) { CompletableFuture<String> future «=
mapToInt(n n n) System. out. printin(name.get()); CompletableFuture. supplyAsync(() -» "Hello Java 8");
```
} else {
1, .sum(); és . #,
```java
, souk.printial "Name not found"); future.thenAccept(s -» System. out.println(s)); P
```
Sees moe
LL 3
m Parallel streams make stream operations Built-in support for Base64 encoding and decoding. Run JavaSerint code on JVM.
run in parallel. String text « "Java 8":
Tp list.parallelStream() CQ string epenre ScriptEngine engine =
```java
.forEach(System.out: :println); vencodeToString (text. getBytes()); =~ Seritngaterngr gtgneigtionat rather »;
, // Improves performance on multi-core systems String decoded = new String( Object result = engine.eval( print("Hello from Is"):")5
```
(G3 ge Arta} {TR png Pesan} {5 rd Cais]
```java
'i Annotations can be applied to any use of types. Allows on annotation to be repeated. . Some new methods added to Collection
List<@NonNull String> names; @Repeatable( Hobbies. class) interfaces. a
im, @NonNull String name; ote ees Cleaner forEach() removelf() s
```
e Fae spliterator() uC) o
} : spliterator replaceA e
dm V Helps in static type checking tools @Hobby( "Reading" ) annotations! stream() computelfAbsent()
```java
class Person { }
```
Cag Taaoeay ry

## Interview Questions

L —B—, <«——{ IMPorRTANT}~.% gt
, P actice these = _ i
_ questions to 1) rs) 4, Confident
next i WW "=
i \ i Oo / ° . Learning!
7 AY )
1. What is Java? iw 1. What is Abstraction? B= 1. What is Exception?
2, Whot are the features of Java?
2. What is ion? 2. What are the types of Exceptions?
4. What is the difference between 3. What is Inheritance? Types? . is difference between
= JRE, JDK and JVM? 4. What is Pol hism? Types? checked and unchecked exceptions?
5. What is the difference between s Method Overload: 4. How does try-catch-finally work?
i ne and equals()? we «4? 5. What is throw and throws?
7 6. What is String Pool? end Overvisiing
7 what are acc mars in Jw? 4 6. What is the difference between 6. What is the difference between
TD 8. Whot is final, finally and finalize? class and. object? Error and Exception?
Array and ArrayList? <> nat cable and local variable? 'g Gracefully!
10. What is the difference between <S— AS O
TD 1. What is Collection Framework? 1. What is a Thread? 1 What is File class? uy
= tins Set and Mg? between 2. What are the ways to create a Thread? 2, How to read a text file?
```java
3. What is ArrayList and LinkedList? start() and run()? 3. How to write into a file? ;
```
4. What is HashSet and LinkedHashSet? 4. What is synchronization? 4. What are Streams in Java?
S. Whek is HashMap end TreeMep? 5. What are the ways to achieve Gp 5. What is the difference between
_. 6. What is the difference between 0/7, synchronization? : leInputSt leRead
HashMap and Hashtable? a, , \' r ont Fi ,
Ao Es, 6. What is deadlock? ®) 6. What is buffering?
+k 7. What is Comparator and a Whet ae ? r= ffering
Comparable?
7 1. What are Lambda Expressions? 1. What is garbage collection? a
dy 2. What is Functional Interface? A 2. What is the difference between PMNS Spina roneverkt
1. Wheto API? , "= ond scale)? 2. What is IoC and DI?
fo 4. What is Method. Reference? Seog, , ference bowen fe? 3. What is the difference between ,
```java
5. What is Optional class? ; ° 3 BeanFactory and ApplicationContext'
```
4. What is a static block? 4 Wht an te &
ED 6. What is default method in interface? 5. What is serialization? wee oe different scopes
7. What is CompletableFuture? 6 What is the difference between oo.
, int end I ? Ao) 5. What is Spring Boot?
### SQL (Basic) 1 44. Behavioral. Questions (Examples) } 42. Coding Questions (Examples)
++ 1. What is the difference between
WHERE and HAVING? ' en about yourself: 1. Reverse a String.
dm 2. What is JOIN? Types? 3 Mee ey 2. Check if a number is Prime. 9 ~/Y
= INNER JOIN and LEFT JOIN? ; ne eult yur (.s) a Find doh ne Sts
4. What is normalization? and how you handled it. \— 5. Implement a Stack us
_ 5: What is Primary Key ond 6. Where do you see yourself in C¥INBZ) "ang Genes
: Foreign Key? 5 years? yy 6. Binary Search.
TIPS TO CRACK THE INTERVIEW } Se
= ot +, Practice Today
= [A Practice coding problems regularly. [A Be calm, confident and positive. Qe, ) Sue
sey CONSISTENT PRACTICE + CONCEPT CLARITY = INTERVIEW SUCCESS!

## Frequently Asked Questions (FAQ)

rr' q a a . all e . —_— \ /
**fs \ "FREQUENTLY ASKED ) iy @:**
Aaa Answers B os (0. ,
An on ao\\ (QUE ava Sr) 7
(4) what is Java? (2.) What is JVM? (3) What is the difference )((4) What is OOP?
between JDK, JRE and JVM? ;
Java is a high-level, object- JVM (Java Virtual Machine) A programming paradigm
oriented programming allows Java programs to run JDK : Development kit based on 4 principles:
language. 6 on any platform. JRE : Runtime environment v
=> V Inheritance
<= (os) JVM : Executes bytecode ' Polymorphism si
Java [ava (avn) (s. y, hovrecten ri
between == and equals()? Array and. ArrayList? and finalize()?
== : Compares references Array : Fixed size literals to save memory. L. class)
(e.g. objects) e Homogeneous elements If same literal exists, it ; Finally : block always
of objects e Can grow or shrink Pee FOOL e finalize() : called by
= Fee Garbage Collector Tag
What is Exception Handling? (10) What is Multithreading? (41) What is the difference (12) What is Interface
between List and Set? and Abstract class? <-'
It is a mechanism to handle Running multiple threads
runtime errors and maintain concurrently to make List : Ordered, duplicates allowed terface «100% ahrtin UP
normal. flow of program. better use of CPU. Set : Unordered, no duplicates Abstract class : 0 to 100
Keywords: try, catch, i} Cw (ean abstraction
finally, throw, throws. ° he ad Op [L10, 20, 10] { 10, 20} :
A special. method used to : What is Polymorphism?
initialize objects. Overloading : Same method name, tet ete What is Encapsulation? 9
, ; 1 4: erenced objects to
lg different parameters (compile-time) free What is Abstraction?
e No return type QRS. up memory. What is this keyword?
« Nome came oz clas' ' Overriding : Same method name, What is super keyword?
meuza same parameters (run-time) What is try-with-resources? ff
: ww What is Serialization?
a What is HashMap?
Ake . ie a : What is Comparable?
&- _Interview Tip Interview Tip Quick Code Example b What is Immutable object?
```java
(J Understand the concept class Hello { What is Spring Framework?
[Practice coding public static void main(String[] args) { Nae 7
(J Write clean code System.out.println(" Java. is Awesome!"); _ [==
```
[ Revise collections & OOP } SN [</> 2
_— ut a ee
\W\) Gee : Practice y fp Concept clarity Stay consistent

## Practice Questions

{ aye a
```java
S(t =) PRACTICE QUESTIONS;
```
Code better, i> aaa S44 2 j ].®.
higher ' " 5) ( Practice
i? ' this! = we oday,
/—, i ? Write i features.
one is hey 1. Explain the four OOPs concepts 1. What is on exception? 1. What is Collection Framework?
= 3 What is the examples 2. What are the types of exceptions 2. What is the difference bebween
JOK, JRE and JVM? 2. What is the difference between in Java? List, Set and Map?
FAD 4. Explain access modifiers in Java. abstraction and encapsulation? . Wit is the difference bebween 3. What is ArrayList?
5. What is the difference between 3. What is method overloading? checked and unchecked exceptions? 4. What is HashMap?
at == and ? Gwe i j
equals() example. Writs to 5. What is the difference between
6. What is String Pool? 4. What is method overriding? ' HashMap and. HashTable?
ArithmeticException.
. 7. Write a program to reverse a String. 6. Write to sort &.f
5. What is the difference between Whok is the block? a program [FE
fg 8 What is the difference between terface and abstrect class? the use of Really Voc a List of integers. ab
p = w A\
Java
TS 4. what is o thread? 1. What is File class? 1. What is Lambda expression? 1. What is garbage collection?
Je 2. What is the difference between 2. How do you read a text file? 2. What is Functional Interface? 2. What is the difference between
process and thread? 3. How do you write data into a file? 3. What is Stream API? final, finally and finalize?
GD 3. Whot is thread life cycle? b. What is the difference bal 4. What is Method Reference? 3. What is serialization?
4. How do you create a thread? FileInputStream and FileReader? 5: What is Optional class? What is static keyword?
Demonstrate with example. 6. Write a program to filter even 5. What is the difference between
a 5. What is buffering? : StringBuilder and
5. What is synchronization? numbers using Stream API. String, String
'- 6. Whet is deadlock? ve: 6. Write a program to copy the 7. What is ina, StringBuffer?
7, ca
1. Write a program to check if a number 1. What is the output? 1. Identify and fix the error: 1. What is the difference between
```java
' w prime or nek. int x = 5; public class Test { static and non-static method?
2, Write a program to find Fibonacci if(x++ 5) O void main(String] args) { 2. What is the use of this keyword?
```
series. . ° asm
3. Write a program to count the number else , Pr 3. What is a constructor?
```java
_ of vowels in a String. System. out. println(++x); } 4, What is the difference between
```
4. Write a program to find the largest == and equals() for objects?
**17 element in an . 2. What is the output? i x :**
s. we mt ° ons 2. Wentify ond fix the erver 5. What is the difference between
```java
he ee String s = naw String( "hallo"; int() arr = new int(5] deep copy and shallo copy?
ry search </> System.out.println(s == "hello" ); orr(5] = 10;
System. out. printin(s.equals( "hello")); =
```
= --~-{ TIPS TO PRACTICE }-----~ fat
, 1. You are given a large log file. How will you read it I Keep Practicing!
efficiently line by line? w a. little e
L. _ Solve very day. & is the
2. Design a class Employee with id, name and salary. Consistency is key.
i 3. You have a List of integers. You need to remove (A Write code by yourself. Yr Clean code
duplicates and sort it in ascending order. lent
4. You are building a multi-threaded application where
Yh. fe aa Fee FL ST FT ei
( Br Practice + Patience + Persistence = Success a

## Programs and Practice

= ay ge a FS = LSS
ai—< ey -¥ 7
= = eee
' a. 2 = Soe _ ee __/z b 1
?<—t Practice makes perfect! Keep coding =
i Hello World Program (2) Add Two Numbers
(7 . a i ei a ea ea ee _ ( ~ ~~ *,
```java
public static void main(String[[] args) { tt public class AddNumbers { .
ou —4 System out. printin( "Hello, World!"); : public static void main(String[] args) {
, Scanner sc = new Scanner(System.in );
Ti a } System. out. print ("Enter first number: ");
i } int a = sc.nextInt();
) 4 \L ee , System.out.print("Enter second number: "); :
int b = sc.nextInt();
a4 (3) Check Even or Odd int sum = a + by . :
, System.out.println("Sum = " + sum);
s import java.util. Scanner; }
public class EvenOdd { \. Be _. _ y
i public static void main(String[] args) {
Scanner sc = new Scanner(System.in ); 4) Factorial of a Number
i System.out. print ("Enter a number: "); ren errr ran nny
int n = sc.nextInt(); import java.util.Scanner;
4 . 7a public class Factorial {
if (n 2 == 0) . . €£ fa i) public static void main(String(] args) {
4 System.out.println( "Even Number"); "Sg Scanner sc = new Scanner(System.in );
else f eA . System.out. print ("Enter a number: ");
System.out.println ("Odd Number"); 'GZ '4 int n = sc.nextInt();
<. } i long fact = 1;
} ( ! for (int i = 45 i <= nm; ise) {
```
te ! fact *= i; O
```java
a 4 Syst t.println("Factorial = " + fact);
=z ystem.out.println(" Factoria act); !
```
H Table of a Number I 4
' a aaa §
```java
import java.util.Scanner; ! (6) Prime Number Check
= —e ! public class Table { me a
public static void main (String(] args) { import java.util.Scanner; »°AVe
th l Scanner sc = new Scanner(System.in ); public class PrimeCheck { OY. ,
System. out. print ("Enter a number: "); public static void main(String[] args, { ;
int n = se.nextInt(); Scanner sc = new Scanner(System.in );
at System.out.print("Enter a number: ");
for (int i 1; i <= 10; ive) { ) int n = sc.nextInt(); )
4 System.out. println(n en x ei ee "4 (nn i)); boolean isPrime = true;
1 } : if (n <= 1) isPrime false; :
7 5x1=5 for (int i = 2; i i c= mn; ive) { i
T } } J 5x2 10 ! ! ' if (n i == O) { isPrime = false; break; }
```
a: rr i
```java
4 1 Pc 10 =50 ! } System.out. println (isPrime ? "Prime Number" : "Not Prime");
```
aT a . _ ;
Fibonacci Series
```java
import java.util. Scanner; ; ; ; ov i
public class Fibonacci { for Cint i= 3; i <= nz ise) {
=, 3 public static void main(String(] args) { int = a + b; O, 1, 1, 2, 3, 5, 8, 13, ...
Scanner sc = new Scanner(System.in ); System.out.print(c + " "); é
A System.out.print( "Enter how many terms: "); a »b; fe) . .
a int n = se.nextInt(); b ¢3 °
```
int a = O, b = 1; } -G.#)
```java
TEs System.out.print(a + " "+ b+" "); } 3)
```
+ 4X Code. Compile. Run. Debug. Repeat.

## Tips and Best Practices

: \ = a. = psy oe aS
< =PTpS & BEST PRACTICES)
3 @) Understand the Basics B GaBQ Solve Problems Actively
74 = Practice Regularly ) Review & Revise
= 15 =~ ==]} Consistency is the key to 1} Revise important topics and code
improvement. S regularly.
iz GB) Gs Write Code Daily ! (7) Discuss & Learn
- Daily coding builds confidence Discuss solutions, ask doubts and
G FS and problem-solving skills. ) & B learn from others.
- BEE ,
a KK Read error messages carefully and ! Vs Be Patient with Yourself. r
understand the root cause. Every expert was once a beginner! 7}
_" ! \ eet
AN Cat ep We ee OA 2 eS
& =f CONCLUSION Lz @&
=< Yam = a 6 ee eS SS . . y
ke a> NH
**i- Congratulations on completing this notes! Remember:**
rr er—a =
! You have 'oren an ater step towards ! wi Stay curious Q Your hard
i becoming a tter Java programmer. I Keep practicing </> work today
Keep learning, keep practicing and builds !
a _ ( Learn from mistakes jour
=—@ never stop exploring. Success
re lO + (We view comes ! ! Be consistent tomorrow,
> a after the hardest RY
Ik LC dimb! & J i Enipy the journey By}
<_—_" iN ea A " ) J
a CE
Believe in yourself. Stay positive. Keep going. <>
: Ww: You've got this! & VF +
