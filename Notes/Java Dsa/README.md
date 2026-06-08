# JAVADSA Full Notes

Source: [JAVADSAFullNotes.pdf](./JAVADSAFullNotes.pdf)

> Study notes extracted from the PDF. Content is organized by topic with OCR cleanup applied.

## Table of Contents

- Introduction to DSA
- Time and Space Complexity
- Arrays
- Strings
- Recursion
- Sorting
- Searching
- Hashing
- Bit Manipulation
- Sliding Window Technique
- Two Pointers Technique
- Prefix Sum
- Stack
- Queue
- Linked List
- Trees
- Binary Search Tree (BST)
- Heap and Priority Queue
- Graphs
- Greedy Algorithms
- Dynamic Programming
- Backtracking
- Interview Patterns and Tricks
- Frequently Asked DSA Questions
- Tips and Conclusion

## Introduction to DSA

=—. a _ TOPIC 4 l/
"J Let's 4 wae
om, Understan y
_ psa! INTRODUCTION [<
= , Se
Se ,
What is DSA?» == LY
DSA stands for Data Structures and Algorithms. ) Sg
a. ¢; It is a way to organize data and solve problems
efficiently.
7 a
! A data structure is a way to store and organize oe relat 4
data so that we can use it efficiently. M eM
Examples: 1. Eee
= CTD @-o"s- COED 6h
+ -_ Array a _ Linked List a _ Stack Queue Tree
ty 2) (Ageing?
ee ; Ye
An algorithm is a step-by-step procedure or a set 4. Plan y
: a rules to solve a problem. ' Solve y
a , Searching an element in an array ! ptimize
: Sorting the elements
te Finding the shortest path in a graph
> Solving mathematical problems
Soy ssa,
Pita a te he use "Oo '
(Why is DSA Important?) Ot
Oo og a Good DSA
, V Helps to write efficient and optimized code. ! °° _
S Improves problem-solving skills. Better Logic
SJ Essential for coding interviews. = 5)
7 Used in real-life applications (Apps, OS, DBMS, AT, etc.). Better Programmer
T— ie In short: DSA helps us to solve problems in the best possible way! QY

## Time and Space Complexity

Tr =~ ' So Wve problems
<P. ve in less time
' OMPLEXITY [===
Tq _ Memory. ig
an, vel ae?
SY 3\ 1. TIME COMPLEXITY (i
Zt = It helps us to : .
om, Time Complexity is the amount of time an algorithm VY Compare algorithms .
i takes to run as a function of input size (n). ' oS Find the efficient solution
"me Oe Vv Predict performance for
Common Complexities (increasing order of time) NX large input J
FD Complerity Notation Example
em, ( (As n increases) )
20) ZZ tn
O(a") Rear (ag ower w
Input Size (n)
__2. SPACE COMPLEXITY -__-__---_ Exam maple, yo
<a! ity i amou
! Space Complexity is the nt of memory 1] rn-Phace Algorithm (0(1) Space) GE ay2 18)
; an algorithm uses as a function of input size (n).
_— Me ht Uses constant extra space le J
< ma . regardless of input size. ,
\ ; ; Uses same array
1) Auxiliary Space : Extra space used by Extra Space Algorithm (O(n) Space)
t—{) the algorithm (variables, e Uses extra memory that grows 5]1,4{[2/ 8.
_ structures, etc.) with input size. f- -4
yy 2) Total Space : Auxiliary Space + rR, a
Ty Input Space } (Uses extra arrays)
a ine fie
TY iv Always aim for lower time & space complexity. V Analyze before coding.
- For large input, small improvements make J Better complexity = Better performance (69) eet »)
**amr, { a big difference! kee :**

## Arrays

SD .t. ( Let's se = \ ae'
" C nderstane ARR AY S b> - Za
**7% Arrays" ¥v ' Arrays store :**
, «1; Yr vn elements
wre Same
7 is me '
An array is a linear data structure that stores a collection mory) locations.
of elements of the same data type in contiguous memory 0
I locations. Elements are accessed using an index. }
Array: arr of size 5 : All elements are of the same type.
<=, ! Elements are stored in contiguous memory locations.
arr 10 20 30° 40 50. : We can access any element directly using its index.
'Index: 0 4 ) 3 4 Index of first element = 0
en Index of last element = n 1 (for size n)
Indexing in Java starts from 0. : Size of array is fixed (cannot grow/shrink). hg :
+ ee, a a ~shMiw "ae 3
```java
int[] arr = new int([5]; // array of size 5 Syntax: arrLindex ] 7
```
; Time
7 or : Example: ;
int{] arr = {10, 20, 30, 40, 50}; // init arr[2] = 30 // 3rd element
tO rr[O}] = 10 // 1st element
gava i arrlod = 10 st cement "1
<= a0 LP ta AS Pe a a
{Common Operations -———-—---~, {Example Program (Java) j-—-———=——-=—=-——.,
```java
_— 1. Traversal (visit all elements) O(n) , int[] arr = {10, 20, 30, 40, 50}: :
```
a ; ; l F tJ F ] F }
```java
2. eran (at end, if space) 0(1) System.out.println("Elements of array:");
tr 3. pectin (at end) al Bt) : for (int i = 0; i < arr.length; i++) { e arr serge !
4. Insertion (at beginning/mi e) n : System.out.print(arr[i] +" "); 3 of !
```
5. Deletion (at beginning/middle) O(n) } SIZe OF OFTaYy
Sf CQuick Summary ed « i
Same type 1 Fast access ae bis lement ! ' Practice Makes
<= as
ae Contiguous memory O(1) to access 7 Wi in wed men . Perfect!
' O-based indexing element mes ; , }

## Strings

Explore , P < Clo
:=. Strings: : + St, Worlds"
, ( What is a String? ) --~ [fF c = wv
tof Examples DN
<= A String is a sequence of characters. In Java, a string is an ie a
Hello
: object of class String. ) "Java DSA"
- Strings are immutable (cannot be changed once created). : "12345"
i Strings are stored in the String Constant Pool. , "A" S
. nn .
ae a 7 Ke. fh. (empty string) $v
```java
e Using String literal (recommended) , Strings are immutable.
<= . String s = "Hello"; /] stored in String Pool , We cannot change characters of a string.
Using new keyword : Any operation that seems to modify a string
<=, ; : cll i create i actually creates a new string.
```
i = i " ")- creates
```java
tring s = new String("Hello"); new object , String index starts from 0.
<=: ! e Empty String Length of string = number of characters in it. !
String s = ""; // length = 0 I Java supports Unicode characters.
```
ane, N oor ee Me
AE Pao RB oe, e> '
_, (Common Operations ~\ Example }
=" a ; ee f \
```java
, e length() returns length of string String s = "Hello World"; » 1
```
charAt(i) returns character at index i : /}
**{ , e substring(i, j) returns substring from i (inclusive) ° s.length() 2 & :**
**to j (exclusive) e s.charAt(1) 'e' : :**
+—* , e equals() checks content equality : s.substring(0,5) "Hello" .
```java
< equalsIgnoreCase() case-insensitive comparison ! ; s.equals("Hello World") true :
```
: e toUpperCase() / toLowerCase() convert case ! ee 7
1 concat() joins two strings : s.contains("World") true
contains() checks if substring exists s.toUpperCase() "HELLO WORLD"
+— \ e startsWith() / endsWith() prefix / suffix check Me
```java
sy _-& String vs StringBuilder) == = = Fe { Quick Example Program (Java) a
It 1 ' : public class Demo { }
____String StringBuilder 1 " public static void main(Stringl] args) { !
. j Sustem.out.println("Lenath: " + s.length());
```
Slo te object J P 9 9
```java
} System. out. println("First char: " + s.charAt(0));
t—4 Stored in Strina Pool Stored in heap System.out.println("Substring: " + s.substring(5));
```
in ing 0 in memory } }
DDT \ } y
vv ( Strings are everywhere in programming. Master them to solve many problems easily! }

## Recursion

dene SEE ig : y Down Solve
the best 99 Z Smaller Combine
solve & PS ; m y ;
rt -. to solve <7 a
**p version L > :**
smaller ee v7 ane i —= /,
**alent of ee >, LS :**
<=, . Recursion is a technique where a function calls 1 Sy . i
. itself to solve a smaller instance of the same problem , vy ]
wv J until reaches a base case. a ) Cor a,
__ EE ' solution has two ) -;°
r , I 2 Call Stack
t—-_ The condition where recursion stops. @) Function is called.
. (Example)
Example: n == 0, n == 14, etc. r v ue
: Ik checks the base case. : : !
```java
= 2) Recursive Case (Recursive Call) GB) If not base case, it calls itself fun(3) ; \* down) !
```
**The part where the function calls itself with smaller input. :**
with a smaller input. a v fun(2)
' \ ty (4) This continues until base case = Return
EE . is reached. fun(1) Values
= ! v ee (come up)
a ee Se _ es 7 come
= (step by step). .
Base Case: O! = 1, i! = 1 ON
5 If , 1, Common Examples
```java
: int fact(int n) { :
if (n <= 1) // Base Case : %# Factorial GCD of two numbers
return 1; Fibonacci Series String Reversal
'= , return n fact(n 1); // Recursive Case Tower of Hanoi Subset Generation
```
7 ! } : #* Binary Tree Traversals Permutation Generation
Power Calculation (a"n) ,
"eo ava PO
aos Zee
= : fact(4) = 4 fact(3) 3 "beeantages- - oo
= 4+ (3 fact(2)) Makes code short and easy to understand.
, = 4 « (3 « (2 fact(1))) A Useful for problems with repetitive structure. G)
st Calls = 4 « (3 « (2 1)) wen. No
**= ! = % Uses extra memory (call stack). @) :**
) X May be slower due to repeated calls. !
Dr Ee te Me
<=, Y Tip: Always write the base case carefully, otherwise recursion may go infinite! QY

## Sorting

. it,
a8 = \ t's ." aa BZ
oie QRTING ALGORITHMS 7: ° ozz sexe
YD orgerize! } in order (Asc/Desc)
Y . a V Improves search
=, A pc 7 V Better performance
_~———~——_. (7s OF algorithms
( What is Sorting? ) ' Example ) _ ah
Ty ae eS Be ' VES RS '
, Unsorted Arra ;
Sorting is the process of arranging elements of an array or : J
tx collection in a particular order (ascending or descending) [64 ][_25 [ 12 22 iz -\
ition. i
**based on some condition ! Sorted Array (Ascending) , :**
(Types of Sorting Algorithms} ?
: Bubble Sort Repeatedly swap adjacent elements e Merge Sort Divide the array into halves, .
if they are in wrong order. sort them and merge. a =
CODE
OD « Selection Sort Repeatedly select the minimum ! Quick Sort Select a pivot and partition the ° )
7 element and place it at the correct position. array around it. SORT
7 e Insertion Sort Insert each element to its correct Heap Sort Use Heap (Max/Min) to sort 1 A REPEAT
position in the sorted part. elements.
" _--( Example: Bubble Sort (Ascending) }. (Example: Insertion Sort (Ascending) Time Complexity
eens ernment?
a hoy CITE) hm: IESE
**rod :**
toy [2 Te [ee] om 1% TATTLE) ett, [ttn ot] oo oo om ore
i" OC iad OC Gog] O60)
Merge Sort O(n log n) O(n log n) O(n log n)
: (sea) v Step 3: [4] 2 [4] 5] 8] Cnet 2
: it
1 2 4/]5 8 vSoted) So
- Organizes data systematically. Bubble Sort Small data / Learning purpose
+— Y How Bubble Sort Works? Faster searching (Binary Search). ! Selection Sort When swaps are costly )
e Compare adjacent elements. WY Improves efficiency of other _ Insertion Sort -» Nearly sorted / Small data ,
e If they are in wrong order, swap them. algorithms. Merge Sort Large data / Stable sort needed
I< e After each pass, the largest element v ati in ee Quick Sort 5 General purpose (in-place, fast in
comes to the end. , ications (databases, average case
tt leaderboards, reports, etc.) Ww _ Heap Sort When extra space is limited
+. Key Takeaway: Sorting is one of the most fundamental techniques in DSA.
i ! Understanding different sorting algorithms helps in choosing the best one for a given problem!

## Searching

poo ts {SEARCHING , (C) fae
+2 \L. . Se / in target element
em La Wie collection,
BD me fc
( "na? Pa erly,
<= ° aaa VV
: Searching is the process of finding a target element in a Input: collection and target element
a , collection (array, list, etc.) and returning its position (index). : Output: index of target (if found) else -1
If the element is not found, return -1. _ Efficiency depends on the algorithm used =
) Some algorithms require sorted data ig
51 TYPES OF SEARCHING ALGORITHMS <
sg =:
LINEAR SEARCH BINARY SEARCH
Works on both sorted and unsorted arrays. ° Repeatedly divide the array into halves.
7 Example: e If equal return index.
F— e If target is smaller search in left half.
<_ arr = [} 10 25] 7 30] 15. » target = 30 e If target is larger search in right half.
Index: 0 1 2 3 4 Example:
mar» ee
= Step 1: Compare 10 with 30 x
eT Step 3: Compare 7 with 30 xX
. . Step 1: mid = 3 arr[3] = 12 < 16 search right half
Step 4: Compare 30 with 30 W Found at index 3. P
Pseudocode: AZ Step 2: mid = 5 arr[5] = 23 16 search left half
AD fori fromO toned) Time Complexity (2 5 8 12 16 23 38°
if arr[i] == target Best Case : O(1) Step 3: mid = 4 arr[4] = 16 Found at index 4 W
SO] rete fase Gate OC) (2 Ts [8 [ey [os [ae
ee J, rt 1 low = 0, high = n-1 } Time Complexity Ww
;= Tat ar re ae while low <= high
aw 1 LINEAR SEARCH vs BINARY SEARCH mid = (low + high) // 2 Best Case : O(1)
Feature Binary Search i arelmid] == target: return mid Average Case : O(log n)
eT FeFe._
**=. ae GS ry Remember:**
. (_ Tips ) wv Use Linear Search for small or unsorted data. : Right algorithm
4. v Use Binary Search for large, sorted data for better efficiency. makes search VY
7 wv Always handle boundary conditions in Binary Search carefully. . fast & efficient!
en 7 5

## Hashing

Ploy with '1 IT i] b tes!
== ale ~(o,)- Mt Powerfull =
" .?.* a we rh a Te a ae ae use less g
**What is Bit Manipulation? —--—_- A Binary Representation .-___ [_ me': SA :**
f eS. oe oe oe ee me \ ( Sees SS _ BY
Bit Manipulation is the process of performing operations All numbers in computers are stored in , "
on individual bits of a number using bitwise operators. : : binary (Os and 1s). f Think in :
= Li og :
xample: : l ) !
Used to optimize solutions, reduce space complexity P , Binary
ase, and solve many tricky problems. i ;
we Decimal 10 = Binary 1010
Ve Ve \] }
Bitwise Operators in Java ---{ How Bitwise Operators Work? ) == =
OR ms esr ee
ee ooo ( = 6 Gin ore)
om, 0111 (7) : (Left shift)
fame a ! oOtt 1 (Right. shift)
Se = se a
! —+> n&1 0 (even), 1 (odd) a @) Check if a number is even or odd
```java
Ts Check if a number is power of 2. ower of 2 int n = 10; : 10 = 1010
```
n& (n- 1) == 0 has only if ((n & 1) == 0) & Even 1010 & 0001 = 0000 Even
**ae Set, Clear, Toggle a particular bit. one set bit! cise » Odd :**
T we . ;
```java
Count number of set bits (4s). ; / Check if a number is power of 2
```
Ww int n = 8; 8 = 1000 :
I Swap two numbers without third variable. an if ((n & (n- 1) == 0) Power of 2 1000 & 0114 = 0000 Y
**aaa Trggle (Flip) the 3:d bit (0-indexed) :**
```java
Set ith bit n (1 << i) Examples n= 5 (0101) n=n (1 << 3); // flip 3% bit Makes
```
Clear ith bit n& ~(1 <e i is 2 Ged bt) // 0104 1000 = 1104 (13) x Perfect! )
" Toggle ith bit n 4 (1 << i) Clear: 0101 & 1011 = C001 (1) SS a :
= Swap Two Numbers (Without Third Variable) oY Use bitwise operations to optimize your code.
```java
int a = 7, b = 3; LoN ; ~Y Always think in binary for better understanding. :
==, a=a%b; // After swap : W Left shift is faster than multiplication by 2.
```
ces OSS go oo
```java
a= ab; W Right shift is faster than division by 2. YAY
```
<a, ay ap. nn
: eo" Bits may be small, but the power they hold is huge! Master them Y

## Bit Manipulation

Store & Find ; , Y Goal: }
Data. Supe _ (WASH TABLE) wars data 20 that
\, Fast: a = we can find it
<= Y Ui Vz very quickly!
C\sthat te Hachinn? ) Unk C.n-b w
! Hashing is a technique used to map a key to an index A hash function h(key) converts a key into an index. !
cy ina table (array) using a hash function. _ The index is used to store or find the key in the
It allows insert, delete and search operations in hash table. l
stay overage O(1) time. Good hash function distributes keys uniformly. Vy
Hash Table _ ;
Take a key. ! Hash function: h(key) = key 5
+o 0 Insert keys: 15, 6, 25, 17, 10
**Apply hash function h(key) J 1 6 Index Hash Table 1 tation:**
am Go to that index in the table. 4 = : 4 FG 6%5=1 index 1
== free 2 25 25%5=0 index 0
Store the key (or value) _(2) 4] o3 f. 17 %5 = 2 index 2
om, t that index. %5 = 0 index 0
Meee i; Collision at index 0 (15, 25, 10)
<= oe ae aN a
_e— { al a Se Ea
a yy . ' °
< ! When two different keys map to the same index, it is ! ! 1) Separate Chaining 2) Open Addressing
: called a collision. Each index stores a list (linked list) : If collision occurs, try the next :
==. of keys that hash to that index. : empty slot (probing).
Example: : Index ,
_ Using h(key) = key 5 0 [45 ]J>[25]>[t0] = Example: Linear Probing ,
HS 0 and 25% 5 ciao ab Inder 0 7 1 [fe ]> nu 9 4 23 4 ?
wee NULL
dy 2 TOMEI
(Operations in Hash Table ;—-----=—~, 3 NuuL oo a ee
+ abe.) -s Add Le Ae 4h illed using probin
coy Insert(hey) Add hey to the tole = CY) MEF sg eroting
- Search(key) Find key in the table \,
Delete(key) Remove key from the table Ch ee
_ Advantages X Worst case can be O(n) when many collisions occur.
+ V Average time complexity of insert, search, delete is O(1). X Performance depends on the hash function.
" v Effictent for lenge datneete. oa, 3 i, Requires extra space for the table.
v~ Widely used in real-world applications (caching, indexing, etc.). \ }
= (p Hashing helps us store and access data quickly. Choose a good hash function Be)
} and handle collisions wisely! Y '

## Sliding Window Technique

**Smart wal to o ING WIND 7 => Goal:**
a process Part S Evaluate a window of size k
= (subarray / subst 4 (or variable size) by sliding
S arrays / strings efficiently. A vv
! W " window" of the data. ects , , 1 )
° e keep a : (part) Initialize « window with one or k elements ! Subarray / substring
ia ey Do some calculation on this window. Calculate something for the current window. -oblems
next element(s) and update the answer. Expand right (add new element) Fixed size window
ty This avoids repeating work and reduces time 7 Shrink left (remove old element) viv
! @) Repeat until the end. Counting / Sum / Max /
bo a ESEXESEVESEN AE ee rage al
(2 [tt sift 3 2 Window 0.21 Oe _ !
Gasp) = GEG an ing
re 1 RDU STA] we ny tre
Current Window (size = 4) ' 4
Ae i L2] 4] 5] 4] 3] 2 Window [2.4] AS
S KL A\ and soon... = / \ J
f FT ; 7 nes at fs &
a eT SSS = 4
1. Fixed Size Window ! 2. Variable Size Window ! wW Maximum Sum Subarray of size k
Window size (k) is constant. Window size is not fixed. Wf First Negative Number in every window of size k
am We move window of size k We expand and shrink based Y Count of Anagrams
from start to end. on condition WZ Longest Substring without Repeating Characters
Example: Max Sum of Example: Longest Substring WZ Longest Substring with At Most K Distinct Characters
KX Subarray of size k without Repeating Characters Minimum Window Substring
**Gf Fruits Into Baskets :**
a We expand right and on
SS Windows: shrink left when needed. (Complexity 00
: CTETTEISEDT) Bop Sete,
os (1..3): }1 5 4 Sum = 7 : ole Ls Lelie < [6/6 Each element is visited at most twice !
t . (2..4): 5} 113] Sum = 9 «Mos! L p (by L and R pointers). S
(shrink) (expand) Space Complexity: 0(4)
i oy \ (excluding the data structure used) J
. _ a ee
t E . Lo a _
Py reat «0 b> Uh tar Aer (2}4]}5 [41] 3] 2] k-3
# Add the next element (expand window) Window = (L..R]
while window is invalid: re aR
. cream PZ RD tt 7 8
```java
# R left element (shrink window l ; . i +
```
te tare ee a ) Shrink with Lo)
**FD Upaate wind stat wien codon J 3] te) 543 9 9 :**
3 Updos Fea Update nor # 03.5) 132 6 9 J!
vb a 's velit ____)} \ + Add next element with R Remove left element with L ,
Any (Advantages = _isadvantages Tips Key Takeaway
S a P ! ' i
_ 0 Reduces time complexity Not suitable for all problems Clearly define what the window
(from O(n") to O(n) pepresents 66
. . ; Process '
XS W Uses constant extra space + ond when to shrink. by maintaining a window,
'Tr coding inberviews cs ' & iki iniki the right time. Z
Y Sliding Window = Less Work, More Efficiency!

## Two Pointers Technique

**a ore Pe Goal:**
"wig ; Solve problems efficiently
si: two pointers t () POINTERS APPROA CH by aiding extra space
ne ing on the \ oS ee and unnecessary nested
se ioe problems \s A smart technique '° wet sc i Ww.
to \ ns LY
Sr What Two Pointers? --—---.---—- ne :
What is Two Pointers? \ solving poirs or subarrays/substrings.
(" h the data Problems involving pairs
throug ;
E-) . =p: difference, "
! structure (usually an array or ! Finding elements with a specific condition (sum,
in the same direction,
iT} The pointers von pa speeds. I r e Reversing or rearranging data.
. ' Problems w _4
Cf ! This technique helps reduce time complexity ° ee
from O(n2) to O(n) in many cases Tan .
\ Common Prob y, 1
Cf) a a
inters i ,
og 3. Different Spee . . from sorted array .
Cf ) 2. Same Direction dy Remove duplicates
1. Opposite Direction ! f One pointer moves faster !
One pointer starts from AGN Reiners St om than the other to cover We Velid Pali t Water
+ nt mov
From the end. They move Be Trapping Rain Weer
towards each other. . 3Sum / 4Sum (variations !
en GEGEE) GEER) 3 gs Agr) reg
ts) lt t Be Linked List Cycle (Floy Hey —_]
R : ' : cle
L inding duplicates, Use for: Linked list cycle,
RD Use for: Pir sum, Palindrome Use for: ira Remove Trapping Rain isan, Some ! y,
Cad we Tur. . , blems, . ee
check, Container With Mos weed Pe subarray pro JM
Water, etc. a
7 a eo \
Sn " How It Works? (Examples ) i
anna How Tt Works? ( «Sorted Array 3, Valid Palindrome
bef 2 Remove Duplicates from Sorted Array Check i string is palindrome
Si _ Pair Sum in Sorted Array 1, 2, 2, 3, 3, 4, 4 J (ignoring non-alphanumeric). .
```java
Find if pair with sum Use slow (i) and fast (j) pointers String: "A man, a. plan Trlelalelel
J+ Array(R]} Action Ee zy; R
```
**[See R [ar Are tt in :**
(Not needed) - - ipping von-epharumai
ne rr iis
p GL 8! Go ees Vv
(First 4 elements are unig Time Complexity: On),
SY Time Complexity: O(n) Time cre a
\nannennnnan vty)
a "1; = a See 2
tt) "Ads nF es aa UP: a Understand the problem clearly. !
, omplexity significantly. Not opplicable ! Decide direction and moveme
S : constant extra space O(1). \ nent Handle edge cases (empty
O Uns . Finding correct pointer Test with dry runs on small examples.
ee . : Less Space, More
Y Two Pointers = Less Time

## Prefix Sum

```java
A—t = O a WA); N
```
3 a
mre) of PRE UM 72
cumulative sums Sj
F Quickly find the s
GD to crower rong \ (CUMULATIVE SUM) jen
sum queries in ' bt aes = elements in any
1) time! = Wf yyy range of an array.
Prefix Sum array stores the sum of elements from 1. Create prefix[0...n-1] Sum of elements from index L to R
cy Me Desinning up fe that index prefix[0] = arr(0] (O~indexed)
< ! prefix(i] = sum of arr[0] to arr[i] (O-indexed) 2. For i from 1 to n-1: sum(L, R) = prefix(R] _ prefix[L 1]
ics prefsts) = prefialic a] arr (# L 0) !
" prefix(R] (if L=0) .
'hoy oy FED
Ps Fi 3 r # arr is O-indexed ( 5
ro prefix[0) = arr [0] i
= Prefix Sum (prefix): for i= 1 to n-4: arr : [ 2, 4, -1, 3, 5]
Features oo i oT
WF Query Time : O(1) Works only for static (unchanging) arrays. -
vy Extra Space : O(n) Can be extended to 2D Prefix Sum for matrices. !
ot YR Best for many range sum queries on a static array. \
am . = ——=s ZA
f° SY) SO DIPFERENCE ARRAYS [ex
cm in 0(1) each and ¥ é' . Efficiently perform many
in O(n )! array.
**s _--- SCR iar ----.__ Range Update using Difference Aeroy'}---. Tai ine :**
Tom djacent elements of the original array.
e diff[i] = refi) = arr[i-1] (for i 0) asp Mech Toler then updating cath
a Py After doing all updates, convert diff back to arr __ in the range one by one,
= , using prefix sum on diff. ]
**wes Example Perform these updates on arr of size 5 (all zeros):**
c-, arr (initial): [3 5 2 6 1 J 1) Add +5 to range [1, 3]
Difference array (diff): We want to add +10 to range [1, 3] 2) Add +3 to range [0, 2]
3 2 -3 4 5] Step 4: Build ditt Start with aff =[0 0 0 0 0]
<_ T T 1 I tT Step 2: Update diff Upiis hed, Bad, wis'
<_ sree EIS creel rey diff[4] -= 10 + -5 10 = -15 Update 2: L=0, R=2, val=3
am arr[i] = arr{i-1]) + diff (i) Step 3: Convert diff back to arr
7 arr[O] = diff[0] Index : 0 1 #2 3 «4 Rebuild array: !
"Tr arr[i] = arr[i-1] + diff[i] arr 3 16 1
a Feature Prefix Sum Difference Array _ When to Use? Key Takeaway
Use Case Range Sum Queries Range Update Queries Use Prefix Sum when you need to answer 66 ) }
Update Mot efficient Very efficient (0(1)) many sum queries on a static array. . . .
;= Query 0(1) Need rebuild (O(n) S Un O heres stan, yo sand to abe Prefix Sum Quick queries after preprocessing.
Extra Space O(n) O(n) STs array later. reconstruction.

## Stack

ct aw - »
```java
C Last In = oa ~> <= Goal: ;
```
EP® (First ) S K apg so that
. LIFO F = 1 item added
q : _ < cs removed.
ER an a a.
a _ . ? Sp ff yee
r What is Stack? a \ Basic Idea .
cr A stack is a linear data structure that follows ! Think of a stack like a stack of plates. ye
, the LIFO (Last In First Out) principle. es We can odd a plate on the top. !
im. ae . lements take I >»
< Ineertion and! deletion of eleman $ place : e@ We can remove only the top plate. er ——= ,
at the same end, called TOP. SS
ae ' e The bottom plate is removed last. eS,
iin Fa ae ; Oo. Tr)
Gas --. pees a ...)
Start
AY TOP : : e push(x) : Add element x to the top. (Empty Stack) 7
S 7 ED push(10) TOP
(Points to the # pop() + Remove and return the top element. ! push(20) 30 <
A : top element) push(30)
<q : 30 Stack! ° peek() : Return the top element without ! —_____» 20 l
: removing it. 10
**<h 10 e isEmpty(): Check if the stack is empty. :**
a= n isFull() + Check if the stack is full 20 < TOP mae Top
'bee BOTTOM (for fixed size stack). !
```java
(ue, mieh() and nan() laa? = x a; »
```
mS free i
oT ea h(x) , ry TOP eee , 1) Fixed Size Stack (Array Based)
; ; Size is fixed.
4 = : e Add the element x 20 20° ° Uses array
at the new TOP. 10 «— TOP 10° 10 e Overflow possible.
Ar Remove the element EW 30 <— TOP _ Size is not fixed. Ex
q —_ . st.
at TOP. 20° /20 aim : ° bse inked it cx
ee ec
4 ' ! is available. NULL
am Applications of Stack Te "Fi ee
. i . ac ing
1. Parentheses Matching 1 \
AX ; (maze, puzzles) 4 Simple and easy to implement. X Limited access (only top
N 2. Undo Operations 5. Function Calls 7 7 element is accessible).
(in editors) ! = (recursion) W Efficient operations (0(1)). ! X Overflow possible in
em ' 7
q 3. Expression Evaluati 6. Syntax Checking Y Useful for many problems. : fixed size stack.
oon I in Compilers mt
A . Ne Ki
Cor ie pea
We Stack follows LIFO (Last In First Out). OD Kale 'calm isind Vetacla ie ibe! ,
**WW All operations are done at the TOP. :**
WW push = insert at top, pop = delete from top. j x 5 (Use staexs to solve problems step by im) J

## Queue

Gh' rt \ aN woe aT = b> KKK AN
**First in 7 Goal:**
Ae (First Out!) Sore data 0 that
\ : 7) ; Yyie ts first 0
E wy] = First In First Out (FIFO) a Aa
_-----, What is Queue? }----____ on. ile, os
ff SE ye EE ll \ (- 4
Key Idea p=
"am A queue is a linear data structure that follows —_
, the FIFO (First In First Out) principle. ° of queus Uke a line of people.
ce New people join at the end (REAR).
< Insertion is done at the REAR. The person at the front leaves first (FRONT). :
Deletion is done at the FRONT. REAR
c> Rapala) oper fo)
Representation —\\ perations an ail a,
<> e enqueue(x) : Add element x at REAR. , Start (Empty Queue) !
FRONT REAR ELE TT) Fees)
, dequeue() : Remove and return element =
e= v from FRONT enqueue( 0)
ro = Feo LTT] Frareo
40 front() : Return the element ot FRONT
without removing it anquanel20)
< Oe rear) : Return the element ot REAR. sof2o]
: Queue enqueue(30)
a= isEmpty() : Check if queue is empty, jso[2o{3o] F-0,R=2
, isFull() —: Check if queue is full dequeue() removes 10
se (for fixed size queue). = = _ 20{30] F-4,R=2
< Me : dequeue() removes 20
OO Cie) Fake
CPD 7 How enqueue() and dequeue() Work? ~--—. i 3777 ne
enqueue(x) ae Mao ees oN
Am : Add element at REAR. Special Case: 1) Linear Queue (Simple Queue) !
< ! Move REAR one step forward. a : Elements re added ot REAR
ae Fekea whee ona, 22120130] J
FO [10] 20} 30] } [20] 20] 30] 40) ce cums Once REAR reaches end,
on oe FeR=0 : (overflow may occur). F R !
1 ew) 8. When lt aimee SSS nn
pa ! Remove element from FRONT. _ r 4 2) Circular Queue
**: Eee: daguaat) sv Last petion te mace (aS :**
Example: ueue back to first position.
re [ele] =] 0) (lal + ein ee ga a0]
wo we
cr a rn PT (haze) a CA ea Le Vea
Applications ~--. -—--_ Advantages ---.. --, Disadvantages ~ co Implementation (Array based) -—----—-~.
**Ax (ep) Print Queue A Simple and easy to i , Fixed size queue may Variables:**
```java
< , ' 2. CPU Scheduling H couse overflow. int queue(MAX], F = -1, R = -1; Queue Array
```
an, space. I
5 Lawl Onder 7 of FRONT and REAR. Underflow Condition: t t
**Powe :**
& Remember: Queue follows FIFO First In, First Out! Q

## Linked List

Zs S=_—_ 3 ;
**Dyno C ; Goal:**
re "9% ai wat GP Pets to the next
ch et eh i ea BD EA
i A linked list is a linear data structure where
The first node is pointed by HEAD.
<n' elements (nodes) are stored in non-contiguous ! ! ° 'y 'ys
4 P
memory locations. Each node contains: The last node points to NULL. -
**am Data (value) ! Size is dynamic (grows or shrinks at runtime). @:**
_ Address (link) of the next node + Efficient insertion and deletion.
\ (Node) dh
am ss a Se ms a A A A A A S : m me s
= 1. Singly Linked List Structure of a Node: Ex ;
2. Doubly Linked List ! l [5] PEL REL pb NULL
S 3. Circular Linked List (Singly) : create) + Create an empty list
traverse() : Visit and display all nodes ,
**: insert_at_end(x) : Insert x at end :**
,= : : insert_after(key, x) : Insert x after given key !
S \ _/ delete_at_beg() = Delete first node
e delete_at_end() : Delete last node
am delete_after(key) : Delete node after key
search(key) : Search a node with key !
Insertion at Beginning HEAD ! ( O = ' \
'T_T HEAD I Dynamic size
Lf PEL oT Jone => "(5] Le] [20] Easy insertion/deletion
**ant Ineertion af End ! Efficient memory utilization :**
HEAD an i
c= feo] < "->[10] [20] (Disadvantages }
Deletion of a Node with key = 20 Extra memory for pointer
;= HEAD _ HEAD No random access
} NN tase " €3} Traversal is required
ant oo ites ene ce —"'('O;OOOO.TLTLCULUCUL \ to access a node
Applicati ee ae ee _ 7
1 pplications / =< (Singly Linked List) Fa Memory Representation (Singly) p-on ny
= LY 1. Implementation of Stocks, Queues _ Visit each node from HEAD to NULL. 500 '000 +000
```java
. 4. Dynamic Memory Allocation printf ("Yd " temp- >data); !
```
5. Undo/Redo in Applications 8 ea ke Boe. !
a if mp Th ' 11
a \ JM 4
Sk Linked List connects nodes, not just data! Y

## Trees

L Sl a ee
**; A Wee @S i the oa Goal:**
<n. Hierarchice ' es , hi chi al str -ture
e i; Ye with parent-child
a=: : relationships. Ly.
S A tree is a non-linear dota structure made up of Root : Topmost node (no parent) !
modes connected by edges. It has a hierarchical Parent : A node that has children \ 7
CT structure with a single root node and zero or more Child : A node which has a parent "I
subtrees. Root Siblings : Nodes with the same parent 'I
a= ! vi) : Leaf Node : Node with no children
1 is root Internal Node : Node with at least one child
. 2) © 2, 3 are children of 1; Degree of a Node : Number of children of that node !
ryt Ly
< Oo (5 6 7) 4,9 ore children of 2) Degree of a Tree : Maximum degree among all nodes
6, 7 are children of 3 Level : Position of a node (root is at level. 0)
am MC _) Height of a Tree : Maximum level of any node
--— Trees J oN Binary Tree Representation
4. General Tree 2. Binary Tree
tr A node can have any A node can have at most 1. Linked Representation Example Binary Tree
< : number of children. two children (Left & Right).
eS 2 ke sf
ee Node
3, Full Binary Tree 4. Complete Binary Tree . va (40) (80) (60)
<n See: node has 0 or 2 All levels are completely ,
rey struct Node *left;
children. filled except. possibly 5
**(a) the last level, which is @) struct Node *right; Inorder Traversal (LNR):**
2 Filla from left to ight oth 40, 20, 50, 10, 30, 60
te YY © AO® :
a es . : ,
=r a
4 1 Inrder (LN) 2 Preorder (MLR) & Peter (LRN) A tree with m nodes has n= 1 edges.
! aad a Right ! ode — Right Left —» Right Node (Where n 0)
ro Qa a OuN 'Qn W Only one path exists between any two
" a , a ¥ a les j !
am M4 vs ' \ \ y fi y wv Removing any edge disconnects the tree.
) Ys .
(50) (60) ! (4+) (50) (60) ) \@ W Adding an edge creates a cycle.
No a = Oe = o oo wo a —_ ee Z
(¢, ower 1F 42) , den 1+ eo a "ae
a=: r~{ Common Operations: ' Applications a——— 1 Advantages & Disadvantages .
create() : Create a tree ! W Expression Trees (compilers) Advantages [Disadvantages
am ° inert : Insert a new node W File systems (directories) -W Represents hierarchical data X More complex to !
delete() : Delete a node SW Hierarchical data (org charts) naturally. implement.
search() : Search a node YW Searching (e.9., Binary Search Tree) W Efficient search, insert 2X Consumes more memory
<__. traverse() : Traverse the emo BF Decision making, AI, networking and delete (in BST). (pointers).
**bvene Is W Scalable and dynamic. Not suitable for simple :**
a 1 linear data
cm NK a —J ee! \ _ /
WW Trees reflect real-world hierarchies beautifully! Y ]

## Binary Search Tree (BST)

so \ SO BINARY SEARCH] [=
: Tree @x . ,
" ech Property! TR BS T) i a Phar
. ie ae a as are fast and
Le Ue ov L
aA A Binary Search Tree (BST) is a binary tree in Example BST ° his a Bi Tree.
« which, for every node: \ !/
### (50) For any node, LEFT < NODE < RIGHT.
ax ! ° hee oe ce LEFT subtree are LESS Inorder traversal of a BST gives the keys L
S "key (30) (70) in SORTED (ascending) order.
e All keys in the RIGHT subtree are GREATER No duplicate keys (or duplicates are handled !
ge than the node's key. (20) (40) (0) (20) consistently).
ann =z a
Hf Node The left child of a node
< struct Node { ° ° °
int key: contains smaller keys.
int Keys left hey [right ee nce OMY O
am struct Node "left; rig con
struct Node *right; / \ greater keys. Go) (30) (60) (70)
oe [Left Right rn il as
< ae _Subtree _Subtree All keys < 40 All keys 40
em a
. Basic Operations OT
= OL. Search(key) 2. Insert(key) 3. Delete(key) 4. Inorder Traversal
TF Start from root and follow e Start from root. three cases Visit Left -» Root Right
ta ' If key == node->key Found where key should go. 1. Leaf Node Remove it. Result is sorted order.
< IF key < node->key go LEFT 6 Insert as a leaf node. 2. One Child Replace with (50) 7
If key node->key go RIGHT a the child.
s ig 7 (20) (60) with inorder successor
Ol 0) (smallest in right subtree)!
l _, or inorder predecessor
oe oh d Gs) Ge cme. 20) (40) (60) ©)
p= (Search 30 Found } (25) Insert 25 Output: 20, 30, 40, 50, 60, 70, 80
« (TT ent _/
ee Wo. oe (J Th
fig oon Baamples Insert in BST )-———-—--—-—-—-—-—-—~. {Time Complenity
cy 60) 60) Search : O(h)
0) ORR , , Insert: O(h)
: 30) €) ( Where h = height of the tree
= : (30) (40) l° Best Case (balanced) : O(log n) :
JS Insert 50 Insert 30 Insert 70 Insert 20 Insert 40 Worst Case (skewed) : O(n)
re ~----_ Advantages ~ Disadvantages _ Applications
I wo Efficient Search, Insert, Delete (avg. O(log n)) Performance depends on tree height TY Symbol tables
, W Inorder traversal gives sorted data x Can become skewed (like linked list) wv Database indexing
aa wc im worst case
Wi used in databases, compilers, etc. Requires balancing to maintain efficiency
, vay (3. (use AVL / Red-Black Tree) @) Te Range queries
G¢ BST = Binary Tree + Search Property = Fast and Smart Data Management! QD)

## Heap and Priority Queue

"a "2 Pn a a a " ,
A Co \ Le : 4 Goal:
Binary Tree . ;
eT-© based structure . I Efficiently find and remove
used to implement $$ the element with highest
4. Priority Queue! Mfg. Yin (or lowest) priority.
< iy . W
< / Pee et ae Max Heap Min Heap Lt
A Heap is a Complete Binary Tree that satisfies (50) (10) ?
Max Heap : Parent node is greater than (30) (40) (20) (15) :
<_ or equal to its children. I , )
sine totem OOO®O O68 O®
4 , equ i i
<n or equal to its children. 50 2 30, 50 = 40 10 < 20, 10 < 15
yr _ Array Representation Types of Heap _-~ Priority Queue using Heap __
rrr .
S A heap can be efficiently represented 4. Max Heap In a Max Heap based PQ, element with
For index i: : Root has the maximum key. highest priority is at root.
gO == ===) Used when highest priority 'Ina Min Heap based PQ, element with
e Left Child = 2i +1 element is served first. lowest priority is at root.
_ Right Child = 2i + 2 Yy
(dnl . . or F
SE A 1 2. Min Heap = a
So _ Example (Max Heap) Root has the minimum key. O(log n)
: element is served first.
L&R 7 Tee fan]
"ee :
GO vue: (oo [woo] 5] 5] : we
! 1. Insert (push 45) 2. Delete Top (pop) 3. Peek Top 4. Build Heap (from array) :
am avert ob the ond. Replace root with last element Return the root element. Convert array to heap in O(n).
Heapify Up (compare with parent Remove last element. (For Max Heap, highest value)
and swap if needed). Heapify Down. Array : [ 10, 30, 20, 5, 15, 25,2]
<n 45 Initial Heap !
ou hatte
= . remove last
he a of
e= ety Pon, SD ,OO@M®
tro Scan V Efficient insert and delete (O(log n)) Does not support fast search Heap is a Complete Binary Tree
eduling . : ; ; that satisfies Heap Property.
"4 Sy Huffman Coding SV Uses less Not suitable for operations , Min H Ng
TY Top K elements OF Goad fe vorits hosed . requiring ordered traversal _ ee Pry oe
er-* TE Event Simulation gions priory operations Not stable (order not maintained) ° feet riority Queue
Ri Heap makes Priority Queue operations FAST and EFFICIENT! Wy) f,

## Graphs

Ta a -* N
"a yy
' 4 Goal:
ome model real-world ' - ee = J Represent, traverse and
connections! eee A Graph is a non-linear data structure Pita solve problems involving
a yg consisting of vertices (nodes) connected connections efficiently,
Tf by edges. i WW.
a a a —_— are Pw a = —, e
pi (A Basic Terminalogy (2. Types of Graphs (3. Graph Representations
Vertex (Node): An entity in the graph. Undirected Graph fA) (@) Adjacency Matrix
dee: Conmedton betuesn tu vetin J \ La Q
2 oe enn @}—© met tte
+t Degree: Number of edges incident on a vertex.' S -t}o}o (D)
FO plots topo
oo ee
om ° Weighted Graph
S Cycle: A path that starts and ends at the aX @) Adjacency List fA)
ARQ Com Gap Ta ph ben wT oe
is a
Pe ote ne OE
: / [pae oa
ETD (a) BFS (Breadth First Search) (b) DFS (Depth First Search) 5 Connected Component: Maximal set of vertices Undirected Graph
\Idea:) Visit all neighbors (Idea:) Go as deep as possible where every pair is reachable. Degree of a vertex = number of
a at the present depth along a path before Cycle Detection: Check if a cycle exists in a graph. edges incident on it.
< before going deeper. backtracking, 8 Teeke . TY
opological Sort: Linear ordering of vertices ina Sum of all degrees = 2 x (number
Example Example DAG (Directed Acyelic Graph). of edges)
two vertices. Directed Graph (Digraph)
TQ CK ®B " we (igus)
= BFS starting from A: DFS starting from A: / Total Degree = In-Degree + Out-Degree
"a raversal
S G One MST VF Road / Network routi
Connected Components Or) 1 6) ) 1 (B) SR Web page ranking (Google)
mimomar PY Creat design
4 $1 yay
lA Ni Cy Med oe eno
ee oe Coe
= Total weight = 1+4+2+1=8
CQ Adacency List: Space O(V + E) Flexible (directed / undirected, large dense graphs Graphs help us represent
BFS / DFS: O(V + E) weighted 7 urwighted), *n ore mae connections end. solve
Dijkstra (with min-heap): O((V + E) log V) Vi Many efficient elgor _ ws a real-world problems
am WA Useful for optimization problems. Harder to visualize compared effici '
S @) 1 A to linear structures. (3) iclently: cp
i W Understand the structure, choose the right representation, Wy)
P, and apply the right « jorithm! ;

## Greedy Algorithms

om, .
Sm F GREY ALGORITHMS [=
t~ best AY iy' Solve problems by
+ ot each step: alway
Y ye ae always choosing th
= , : W 2 st immediate option
(What j 'thm? ) Ly a overall result).
A greedy algorithm builds a solution step by step. Y When the problem has Greedy Choice Property =
: At each step, it chooses the best local (immediate) (local optimum leads to global optimum).
tt : option. It never reconsiders previous choices. !
W When the problem has Optimal Substructure CY
It is simple and efficient but does not always give ! (optimal solution contains optimal solutions to \ y)
<= the optimal solution. I \
\ Ww } subproblems). .
a 0 How Greedy Algorithm Works? ) ON Example : Activity Selection Problem
! Start with an empty solution. Given activities with start and finish times, select
= J the maximum number of activities that do not
Q) Choose the best option among the overlap.
**ts available choices. J Activities (sorted by finish time) Greedy Selection:**
Add it to the solution. Ai A2 A4 AS
a Solution par a 2
FD Pept saps 2-4 at the stim UEP gg a) te
compe as a] a ik iy
finishes earliest.
ao J res] _Se tite etag
Activity Selection Problem Given items with value and weight, and a knapsack of capacity W.
tm Fractional Knapsack Problem a ] Take the fraction of items to maximize total value. !
Te See Gri [BO] [em [eae Tre Tee] Sent by vr
Minimum Spenning Troe (Prien's, Kruskel's) CJ 1. Take item 1 (weight 10) value = 60
FD « diikstre's Shortest Path (non-negative weights) O-@f i: {4 to 6 60 Oe mee
Job Sequencing with Deadlines J 2 20 100 5.0 5 take 4/3 of item 3 (ight 10) + vale = 40
' ' {3 30 120 40 qotat Value = 200 (Capacity = 40)
=<, Me \ f
! v "ee ona te implement. X% Does not always give optimal solution. wy Always check greedy choice property. 1,
Usually (less time complexity) : _ Needs proof to show it works for a ! SY Sort the data if required.
7 w~ Works well for optimization problems ; particular problem. .
with greedy choice property. (3 Not suitable for all problems. LW Prove correctness for the given problem.
I—O i 72. eS Sa ?
L Greedy Algorithms: Choose wisely now to save time and resources later! Y

## Dynamic Programming

Solve once, " . y, z, °
\ Y : PROGRAMMING J Py breaking them into
a C. overlapping subproblems
What ts Dynamic Programming? Fae wo
om, i a
Dynamic Programming (DP) is an algorithmic technique ei
used to solve problems by: : ! e Don't compute the same thing again and again.
SD 1. Breaking the problem into smaller subproblems. ° Store results of subproblems.
2. Solving each subproblem only once (Memoization). Build the solution from the stored results.
Ir 3. Storing the solutions and reusing them. € : : )
. Break into Solve & Store Use Stored Get Final
! It is mainly used when problems have: vy Subproblems the Results Results Aneuek !
Ne Ne yy
I r ( Approaches } -— ~\ Example: Fibonacci Series
1. Memoization (Top-Down) _ 2. Tabulation (Bottom-Up) Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
<=. ! e Use recursion + a table (memo) to store ! Solve smaller subproblems first. Formula: F(n) = F(n-1) + F(n-2)
results. Store results in a table (usually an array). Base cases: F(0) = 0, F(1) = 1
Compute only when needed. Iterative approach.
Easier to implement. : Ae Re ee
i G=-S-ey) Bebe oore
Without DP (Recursion): Many repeated calls!
a ) With DP: Each F(n) computed once and stored.
, Both give same result,
) ) , :] but Tabulation is usually r,
1.1 1.2 24 { 22 recursion. stack) from exponential (0(2**))
} ; to linear (O(n)).
pf Ee Se = 7
1 Optimal Substructure (optimal solution contains Fibonacci Series ! Feature Memoization (Top-Down) Tabulation (Bottom-Up)
[ Curaeing Ssbpstans (same sbeetemt S arc Chain Malipcan =A Computation On demand Bottom-up erder
Wctadens locenae [BE] [eee cso oa ewe
SID CN nd Min ls 2S a cor ore
NUL A .° Longest. Increasing Subsequence (LIS) ! Performance May have overhead Usually faster
+ } ! (recursion)
_ ¢_ We Identify f the problem has overlapping subproblems. =
=." . are nee cee deli] represent?): Dynamic Programming turns repeated work into smart work!
$e Store and reuse results to avoid recomputation. QD "Store once, use many times, get the optimal solution. QD

## Backtracking

"S Vi! / Goal: A
Explore : ! k/- Find all poss; )
rT) Backtrack 1 Soluti 'gras
FO "success! , saitions by tryin
T-1 EY Ne Bee Meee
" . . , a a aT = & Solution,
{What is Backtracking?)) (When te Use?) ss
=, Backtracking is an algorithmic technique for solving ie When we need to explore all possibilities.
! problems step by step, trying all possitite. choices, When the problem has constraints.
If a choice leads to a dead end (no solution), we I When greedy strategies do not work. \
om backtrack and try another choice. ;
Tt is used to find all or one of the possible solutions. e Examples: N-Q , Sudoku, Rat in a Maze, =<
WW i Subset Sum, Permutations. \N
<a Me \
How Backtracking Works?
er ee ow backtracking Works: Example: N-Queens Problem
i EE
Make a choice. ! Place N queens on an NxN chessboard so that no two
! queens attack each other.
<= Check if the choice is valid and moves .
- : Example: 4-Queens (one solution)
Step 4 Step 2 Step 3 Step 4 (Solution)
tr WR FP) LELLEBLELRLEDL Rat
;= If not valid or no solution found, X f 2 Pt tT La La OE Te
a , aed
= : backtrack (undo the last choice) and i tt} CLE) ECL] J) EL To
: d oo Found! x Try positions row by row. If a position is unsafe, ®
SO hnahtrack and try the nest one RAY
(A Te ae BIT A Ed 2 Ue a a a <.. =a
Ary Genre Backrckng Agari (Peeuocede) __ Examplas Rak in Mage)
a a. —o
backtrack(state): a : ! Find a path for the rat from start (0,0) to destination (n-1,n-1).
" print/record state Key Functions yi!
```java
return vw choices(state) : 1 {o[o] o- pa [ofo o- ,
```
a for each choice in choices(state): W is_volid(state, choice)! _ a fafo fa. Rare :
eae aa Yowmae Pete te Peete
make choice W undo chai
by Se [Sti Eee] Delete pre
undo choice // backtrack @, (a aaa arr
{ a} . ¥ Try moving (Down/Right). If blocked or
S Simple and easy to implement. X Con be time consuming for large inputs. YF Use constraints to reduce the search space.
I Vv Works well for constraint-based problems. 7 X High time complexity (exponential). 3 \w® Good for problems with many choices and constraints. !
Sy Backtracking explores possibilities, learns from mistakes, and finds the way to success! QD !

## Interview Patterns and Tricks

ae, ae a
INTERVIEW PATTERWS] [=
=) SGN NS), [=
+k problem solving, Solve problems efficiently,
**patterns and smart tricks! :**
the Problem Approach Thoroughly & Discuss !
9 al A Simplify the problem.
SENT Soest oo "SE
S ! © Wink of brute force cases. ° cases. Explain your approach. icate! bag
Ask examples. optimized approach. endl edge Cec olge " o !
am 'eo . . . . ee a a A a eee" woos
_ COMMON PROBLEM PATTERNS
CA «1. Two Pointers = 2. Sliding Window 3. Fast & Slow Pointers "4, Binary Search 5. DFS / BFS
oOfofo ooo-o om: o
ET WD Used for sorted ™ " " e L
< il orrays, POS. Used for subarrays/substrings, Used in linked list cycle, middle :
. . ao Used graphs, trees,
, Trick: Move pointers based Trick: Expand window, then. Trick: Fast moves 2 steps, ick: Al , , connected components.
<n on condition to shrink space. shrink to maintain condition. slow moves 1 step. 'Wee Tet DFS for depth
T ~—sCValid Palindrome Without Repeating Characters Find Middle of LL Sorted Array Example: Number of Islands,
hay & Teploial Sor 7% Dynamic Programming} 8, Backtracking 9. Greedy 10. Heap / Priority Queue
, OO wot, A
<— Used for orderina tasks with Used for optimization with vy x x xX 5)
= or DFS + stack. transition, use memo/tabulation. Trick: Choose -» Explore —+ Trick: Sort + pick the best Trick: Use min-heap / max-heap
Example: Course Schedule II ple: Climbing , Example: Activity Selection,
am pCuserun TRICKS )—-Q——-. COMPLEXITY GUIDE }-----._--{ COMMUNICATION TIPS
TEST ETT FS] cating meh or tg OO
DNA es oe tomes nee arte 0) [eae um ag ee
Bit Manipulation For XOR, subsets, power of two, ete. xen Balanced Trees WY Mention time & space complexity.
pecus ethers !
Math & Geometry -+ GCD, LCM, prime, coordinates. : approaches
Look for constraints They give hints for optimization Se = calm tek ap By SP
Draw it! Diagrams help (arrays, trees, graphs). ( _ On) V es chay to correct yourself. !
ig _ ~ . ; me oe ee oe : _#
a a MINDSET SO STUDY PLAN (SUGGESTED) . _ REMEMBER
" 1 Practice patterns, not jut problems. oy Leaen 1-2 , 7
i -2 patterns at a time. 66
CSS " ) WF Solve easy medium hard. Ho they are about solvi be estan
ro Learn from mistakes. W Do spaced repetition w= a
\ Y Quality over quantity. GO Revise & build your template. of step by step: AW
SHV PATTERN RECOGNITION + SMART TRICKS + PRACTICE = INTERVIEW SUCCESS SP _

## Frequently Asked DSA Questions

os Solve patterns, ' . .
" _ ) WY Analyze & optimize
rir gY i a = . "Te, ~v Stay calm in interviews!
Oe 1. ARRAYS 2. STRINGS y~~ 3. LINKED LIST }~>>. 4 STACKS ~--—--.
1. Two Sum 1. Valid Anagram 1, Reverse Linked List 1. Volid Parentheses
CA 2. Best Time to Buy & Sell Stock 2. Longest Substring 2. Detect Cycle in Linked List 2. Min Stack
"] & Masmun Suberray (Kadane's) Without Repeating Characters 3. Merge Two Sorted Lists 3. Evaluate Reverse Polish Notation
4. Product of Array Except Self 3. Longest Palindromic Substring 4 Nth Node Fram End Daily T
<- ie Meee Nan 5 rus 5. Middle of the Linked. List " 5. Next Greater Element 1
7. Majority Element 6. Minimum Window Substri 6. Reorder List 6. Largest Rectangle in Histogram
S 9. Merge Intervals 8. Implement strStr() 8. Copy List with Random Pointer Ss !
**10. Set Matrix Zeroes :**
co anil mE QA o-0-0-0
or 5. QUEUES 6. TREES -~-{ 7. GRAPHS [8 HEAP / PRIORITY QUEUE
1. Implement Queue using Stacks 1. Inorder Traversal "1. Number of Provinces (DFS/BFS) 1. Kth Largest Element in Array
Am 2. Desian Circular Queue 2. Maximum Depth of Binary Tree 2. Clone Graph
= » Design 3. Diameter of Binary Tree 3. Course Schedul 3. Top K Frequent Elements
3. Sliding Window Maximum Let Order Traversal + tt 3. Merge K Sorted Lists
. Validate Binary Search Tree
Cy Number of Islands 6. Lowest Common Ancestor 5. Pacific Atlantic Water Flow 4. K Closest Points to Origin
" 5. First Unique Character 7%. Construct Binary Tree from 6. Detect Cycle in Undirected Graph 5. Find Median fi Data St
Inorder & Postorder 7. Topological Sort om
CQ front rear [ YG & !
YO OO. B—e (Min / Max Heap)
a=, Bt es » ,
< ry 9. DYNAMIC PROGRAMMING 10. GREEDY 11. BACKTRACKING --~. -{ 12. BIT MANIPULATION
**Cinwing Stars AL ativity Selection 1. Subsets " 4. Single Number :**
**<= oan Cost ire 2. Fractional Knapsack 2. Permutations 2. Number of 1 Bits :**
S 3. House Robber
& Longest Increasing Subsequence 3. Jump Game 3. Combination Sum _ 3. Missing Number
rr 5. Coin 3 Jump Game Tl 4. N-Queens ! 4. Sum of Two Integers
< 6. 0/1 Knapsack 5. Gas Station 5. Sudoku Solver 5. Reverse Bits
7. Unique Paths I 6. Hand of Straights 6. Letter Combinations of a Phone 6. Power of Two
T-OD 9. Burst Balloons to Burst Balloons 3 Generate Parent! 7. Grey Code
10. Matrix Chain ey 8. Candy B me) ; 8. Counting Bits
= 13. MISCELLANEOUS ( C Watwteh pekodaawelipe on P
TO lay Cache eS) INTERVIEW TRICKS ,
2. Design TinyURL Arrays Sliding Window, Two Pointers,
aor 3. Implement Trie (Prefix Tree) } Arey Prefix Sum, Kadane's w Clarify the question & constraints
q 4. Word Search Linked List Two Pointers, Fast & Slow VY Think out loud
5. Expression Add Operators Trees/Graphs DFS, BFS, Recursion sy Start with brute force, then optim
6. Split Array Largest Sum e DP = blems ptimize
CQ 7. Find Peak Element Optinal Scbetcee ! VY Dry run with examples
S 8. Search in Rotated Sorted reckare
tom «10. Time Based Key-Value Store)" rn 2. FE Handle edge cases Qry
k PRACTICE + PATTERNS + CONSIISTENCY = INTERVIEW SUCCESS!

## Tips and Conclusion

ce en ak ee a a
**an ( Great hinas '" i Py) 2 Remember:**
, (ver come from ) Se hy [ <=> Consistency beats talent.
t . ee fort. 2008! i \ iy Oe SE at 4 W Understand Memorize.
. e J \ = = Rs, W Practice Perfection.
< S Re SAS SB DSA is not just about solving problems, ®& V Keep learning, keep growing!
ré 4\ it's about building problem-solving skills. U 3
7. Cle = f oe
re f What We Learned _--4 Key Takeaways }---~. ---4{ Why It Matters --{ Keep in Mind
and their uses. for the right problem. interviews. a the process.
Té Common patterns to Break the problem down Builds a strong foundation Be patient and trust
solve problems efficiently. into smaller parts. for advanced. topics. the process.
(Te » Smart tricks to optimize Optimize time and space ' an Useful in real-world 7 Every expert was once
. code and logic. complexity, it projects and systems, = a beginner! &
q Ko Noe vi No 8 ,
_— a Sa a a 7
q? Se ran A ng elim) OO 05h ise jnurnay, nt race ee
Bl # Analyze different solutions. every te Enjoy . ee Kix small wins, z Q vy, p) =
rT i Ys $e Discuss and learn with others. ae" 1 eep moving forward. ~é !
Be Stay consistent and never give up! 1 You've got this! 99
, "QD _Keep Practicing, Keep Improving, Keep Achieving! @)
