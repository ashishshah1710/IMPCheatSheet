# JAVADSAFullNotes

Source: [JAVADSAFullNotes.pdf](./JAVADSAFullNotes.pdf)

> Text extracted via OCR from the PDF. Minor recognition errors may exist.

## Page 1

ee

+, SS DATA STRUCTURES .
: & ALGORITHMS

eee

---

## Page 2

= All Topics Covered in Doodle Style Images  (
 —— SO eee

(1) Introduction to DSA

(2) Time & Space Complexity

Bit Manipulation
Sliding Window Technique
Two Pointers Technique

Binary Search Tree (BST)
Heap / Priority Queue

Greedy Algorithms
Dynamic Programming (DP)

Interview Patterns & Tricks
Frequently Asked DSA Questions

@
(8)
@
(41)
@)
(3)
‘
(45)
(a7)
(19)
(20)
(21)
2)
@)
24)

h Lv Practice Today, Solve Tomorrow, Succeed Forever! @& : :

---

## Page 3

5{ TOPIC 1 }z
INTRODUCTION Joe

What is DSA?
DSA stands for Data Structures and Algorithms.

It is a way to organize data and solve problems
efficiently.

A data structure is a way to store and organize toe v
data so that we can use it efficiently. tore
Examples: | Manage v

qo ’eos- & ap

Linked List Stack Queue

2)) “Algorithms oe a ee ee
An algorithm is a step-by-step procedure or a set
eo

of rules to solve a problem.

|

| Solve

| - Examples: 7 ! Optimize v
Searching an element in an array *
Sorting the elements

| Finding the shortest path in a graph

: Solving mathematical problems

v Reaets. to write Ldineett and iy code. ace ae
V_ Improves problem-solving skills. Better Logic

V Essential for coding interviews. =

VY Used in real-life applications (Ops OS, DBMS, AI, etc.). Better Programmer

‘

$¥ In short: DSA helps us to solve problems in the best possible way! QY

---

## Page 4

Let’s
A n ee yn

2. SPACE
COM PLEXITY ©

\|_ 4. TIME COMPLEXITY < iia eek.

| Time Complexity is the amount of time an algorithm V Compare algorithms
| takes to run as a function of input size (n). J Find the efficient solution

V Predict performance for
large input
Oe
Accessing array element f (oni Rate 4 0(2")
Binary Search O(n3)

O(n?)

O(n log n)
O(n)
O(log n)
O(1)

Input Size (n)

_ 2. SPACE COMPLEXITY : —CExame ata
= — 4
| Space Complexity is the amount of memory In-Place Algorithm (0(1) Space) '511/4/2] 8)
an algorithm uses as a function of input size (n). sts Kerateedaticgranlce
-— i .
regardless of input size.

Example : Bubble Sort, Selection Sort (Uses same array)

1) Auxiliary Space : Extra space used by Extra Space Algorithm (O(n) Space)

structures, etc.) with input size.

Example : Merge Sort

2) Total Space : Auxiliary Space +
Input Space

. Key Takeaways» Fe

ae Cee ORs UY

V Always aim for lower time & space complexity. V Analyze before coding.

V For large input, small improvements make V Better complexity = Better performance ()
! a big difference! :

---

## Page 5

i Index: O

An array is a mie data structure that stores a collection
of elements of the same data type in contiguous memory
locations. Elements are accessed using an index.

(Key Points > j

_—

Representation —

ee ee ee ee ee

Array: air af aia § @ All elements are of the same type.

@ Elements are stored in contiguous memory locations.
arr — CIEIEIEIED @ We can access any element directly using its index.
@ Index of first element = 0

@ Index of last element = n- 1 (for size n)

@ Size of array is fixed (cannot grow/shrink).

\
|
|
'
|
|
|
|
|
|
|
|
|
|
|
/

OO ne eee

si Declaration in Java » J

= new int([5]; // array of size 5 hase  anlided
Example:
arr[2] = 30 // 3rd element

arr[O] = 10 // 1st element

= {10, 20, 30, 40, 50}; // init

~~ ee
—— SS =5,
¢

A Example Program (Java)

1. Traversal (visit all elements) intl] arr = {10, 20, 30, 40, 50};

2. Insertion (at end, if space) System.out.println(“Elements of array:”);

3. Deletion (at end) for (int i = 0; i < arr.length; a) poe arr.length

4. Insertion (at beginning/middle) : ; « » gives the
ginning System.out.print(arr[i] + ); fom at

5. Deletion (at beginning/middle) size or array

Fi d . / ‘
fer ba be an —_ Practice Makes
© access J P Perfect! ©

Contiguous memory danaitt Widely used

O-based indexing

---

## Page 6

A String i ss
S ring is a sequence of characters. In Java, a string is an “Hello”

“Java DSA”
“12345”
“A=

_ “" (empty string) ©

object of class String.
e Strings are immutable (cannot be changed once created).

-_—— —
es ane aneas a= anes as”

e Strings are stored in the String Constant Pool.

OO ne

- _-f Declaration in Java

— Ti Se ee

@ Using String literal (recommended)

| String s = “Hello”; | // stored in String Pool

@ Using new keyword

String s = new String(“Hello”); | // creates

new object

Strings are immutable.
We cannot change characters of a string.

Any operation that seems to modify a string
actually creates a new string.

String index starts from 0.

e Empty String Length of string = number of characters in it.

ee ee ee ee ee oe oe oe oe oe oe ee ee ee

Java supports Unicode characters.

@ length() — returns length of string String s = “Hello World”;
° mite asi : - returns betel — J | $g,lbnth () es
substring(i, j) — returns substring from i (inclusive)
to j (exclusive) e s.charAt(1) => ‘e’
equals() — checks content equality s.substring(0,5) — “Hello”
equalsIgnoreCase() — case-insensitive comparison
toUpperCase() / toLowerCase() — convert case
concat() — joins two strings
contains() — checks if substring exists s.toUpperCase() — “HELLO WORLD”
startsWith() / endsWith() — prefix / suffix check

s.equals(“Hello World”) — true

s.contains(“World”) — true

ee

4 String vs StringBuilder )

——$————— public class Demo {
String StringBuilder

_ public static void main(String[] args) {

Immutable String s = “Java DSA”;

System. out.println(“Length: ” + s.length());
System.out.println(“First char: ” + s.charAt(0));
System. out.println(“Substring: ” + s.substring(5));

Slower (creates new object
for changes)

} Strings are everywhere in programming. Master them to solve many problems easily! © ‘

---

## Page 7

Think > Break
Down — Solve
Smaller > se

ede is a titebeud where a function calls
itself to solve a smaller instance of the same problem
! until it reaches a base case.

2 See ee SS eS ee ee

“e Base Case ita Condition)
— The condition where recursion stops.
Example: n == 0, n == 1, etc.

2) Recursive Case (Recursive Call)

— The part where the function calls itself
with a smaller input.

n! = nx (n-1) x (n-2) x ...
Base Case: O! = 1, i! = 1

x 2x i

int fact(int n) {

D

if (n <= 1)
return 1;
return n * fact(n - 1); // Recursive Case

// Base Case

Dry Run for fact(4) )

fact(4) = 4 * fact(3)
= 4+ (3 « fact(2))
= 4 « (3 * (2 * fact(1)))
4 * (3 * (2 * 1))
4 * (3 * 2)

Returns
(come up)

2 ee

a

x
x

Co recursive
solution has two )

ey ek: ¥)

Function is called. Call Stack
+ (Example)

It checks the base case.

V

If not base case, it calls itself
with smaller input.

This continues until base case
is reached.

Results are returned back
(step by step).

-—_ — — —

C Common Examples _

fii
Fibonacci Series
Tower of Hanoi

% GCD of two numbers
% String Reversal

%* Subset Generation
Binary Tree Traversals * Permutation Generation

Power Calculation (a*n)

Makes code short and easy to understand.
Useful for problems with repetitive structure.

Uses extra memory (call stack).
May be slower due to repeated calls.

---

## Page 8

1
|

Ca

| GEE (2)
2

4 What. i Sorting? Sorting? )

ei me

based on some condition.

PEG at are?
“Types of S Sorting Algorithms y

¢ Bubble Sort - Repeatedly swap adjacent elements

if they are in wrong order.

element and place it at the correct position.

| |
: |
¢ Selection Sort - Repeatedly select the minimum
! |
| |
| ¢ Insertion Sort - Insert each element to its correct !
|

' |

position in the sorted part.

Avro: [5 | 1 4 [2 [8]
|
|
2 (Sot) |

Pass 1:
1|4

1{2[4]5/ 8] cmv

comes to the end

;

[

}

=

toe

e

&
oe

Key Takeaw

Sorting is the process of arranging elements of an array or

collection in a particular order (ascending or descending)

ee ee ee ee oe oe oe =

'

\

_ WV Faster searching (Binary Search).

array around it.

elements.

Unsorted Array

es oa

Sorted Array (Ascending)

Ca ie 2 ce)

e Merge Sort - Divide the array into halves,
sort them and merge.

e Quick Sort - Select a pivot and partition the

e Heap Sort - Use Heap (Max/Min) to sort

(semen *

Step a OBE Cat
sorted part) |
Step 2: nOOe BC 4
sorted part)

4

stp 3: (ETE [AIST E] cmt 2

sorted part)
l

+
/

_-— —$— —  — — ——— -

ee

Vv Improves efficiency of other
algorithms.
v Essential in real-world

applications (databases,
leaderboards, reports, etc.) wr

© When ‘> ine roam

| @ Bubble Sort -> Small data / Learning purpose
@ Selection Sort -» When swaps are costly
e Insertion Sort -» Nearly sorted / Small data
e Merge Sort -» Large data / Stable sort needed
© Quick Sort -» General purpose (in-place, fast in

average case)

ay: Sorting is one of the most fundamental techniques in DSA.
Understanding different sorting algorithms helps in choosing the best one for a given problem!

e Heap Sort -» When extra space is limited

pr

---

## Page 9

“SEARCHING

(What is Searching? )

ae ae ae ae ee

Searching is the process of finding a target element in
collection (array, list, etc.) and returning its position (index).

Input: collection and target element
Output: index of target (if found) else -1

If the element is not found, return -1.

@ LINEAR SEARCH

@ Check each element one by one from start to end.
@ Works on both sorted and unsorted arrays.
© Simple but can be slow for large data.

Efficiency depends on the algorithm used
Some algorithms require sorted data

| @ BINARY SEARCH
_ © Works only on sorted arrays.
° Repeatedly divide the array into halves.
° Compare middle element with target.

e If equal — return index.
Example: elf as is smaller —» search in left half.
ants [{10 | 25] 7 | 30 | 15 | , target = 30 e If target is larger — search in right half.
Index: 0 1 2 3 4
Step 1: Compare 10 with 30 x
Step 2: Compare 25 with 30
Step 3: with 30

with 30

Example:

arr =((Z [8 [8 [a2 [a6 [23 [30], target «1
Index: i¢) 1 2 3 4 5 6
Compare 7

Step 1: mid = 3 > arr(3] = 12 < 16 — search right half

2 | 5 | 8 | 12 | 26 | 23 | 38

Step 2: mid = 5 — arr[5] = 23 > 16 — search left half

Step 3: mid = 4 > arr(4] = 16 — Found at index 4 Y

Found at index 3.

Pseudocode:

we oes ae ae ae ee ae o”

( low = 0, high = n-4
while low <= high
mid = (low + high) // 2
if arr[mid] == target: return mid

lse: high = mid -
return -1
ro

ny Aied ) o Use Linear Search for small or unsorted data.
—~ SV Use Binary Search for large, sorted data for better efficiency.
wv Always handle boundary conditions in Binary Search carefully.

Best Case : 0(1)
Worst Case : O(log n)
_ Space Complexity : 0(1)

oe ee ee a

Remember:
Right algorithm
makes search
fast & efficient!

---

## Page 10

‘4
i
|
|
|
|
|
|

| @ Toggle ith bit > n% (1 << i)

Bit Willian is the process of evil operations |
on individual bits of a number using bitwise operators.

Used to optimize solutions, reduce space complexity
and solve many tricky problems.

ence eT ae
fae [fives
[Le oes [seen
nal [seer wi

2

@ Check if a number is even or odd.
—> n&i1i — 0 (even), 1 (odd)

Check if a number is power of 2.
—> n& (n- 1) == 0

Set, Clear, Toggle a particular bit.
Count number of set bits (1s).
Swap two numbers without third variable.

( Set, Clear _and Toggle « a . Bit ) -

}
e Set ith bit eo n = 5 (0101) |
| i= 2 (3rd bit)

|
|
|

@ Clear ith bit + n & ~(1 << i)

—>nlil (i << i)

Set: 0101 | 0100 = 0101 (7)

Clear: 0101 & 1011 = 0001 (1) |

Toggle: 0101 * 0100 = 0001 (1) |
/

int a = 7, b = 3;
a=ab;
b=a%*b;
a=ab;

—— So

// After swap

| @) Check if a number is even or odd

©) Toggle (flip) the 3d bit (O-indexed)

They help us Bhs
Problems fast &

All numbers in nictiobes are stored in
binary (Os and is).

Example:
Decimal 5

Decimal 10

= Binary 101
= Binary 1010

, eaal How Bitwise Operators Work? »

= ~ (0101)
= 1010
= -6 (in Java)

A << 1 = 0101 —» 1010 (10)
(Left shift)

A >> 1 = 0101 —» 0010 (2)

10 = 1010
1010 & 0001 = 0000 — Even |

int n = 10;
if ((n & 1) == 0) & Even
else + Odd

Check if a number is power of 2
int n = 8;
if ((n & (n- 1)) == 0) —> Power of 2

|
8 = 1000
| 1000 & 0111 = 0000 ¥
|

Practice
Makes
Perfect! ©

int n = 5; // 0101
n=n (1 << 3); // flip 3%d bit
// 0104 * 1000 = 1101 (43)

VY Use bitwise operations to optimize your code.
VY Always think in binary for better understanding.
vY Left shift is faster than multiplication by 2.

| v Right shift is faster than division by 2.

---

## Page 11

we can find it
| Nery quickly!

ee ee ee ee

Hashing is a technique used to map a key to an index @ A hash function h(key) converts a key into an index.

l ¥

. |
in a table (array) using a hash function. : @ The index is used to store or find the key in the
i
| |
| |
' )

|

|

|

|
It allows insert, delete and search operations in | hash table.

|

/

average O(1) time. @ Good hash function — distributes keys uniformly. wy

4 eee

ee ee eS ~ Exam ee a eae ee
ad Hash function: h(key) = key % 5
fa Key |
= (25) 0 Insert keys: 15, 6, 25, 17, 10 |
| (2) Apply hash function h(key) J 1 Index Hash Table Calculation: |
|  alliasiie h(key) : 0 | 15%5=0 — indexO

| ! |
>= @ Go to that index in the table. J 6%5=1 -— index 1
= Index | 25%5=0 — indexO |
| @ Store the key (or value) _@) | 17%5=22 > index2 |
==. at that index. | 10%5=0 - index 0
: | Collision at index 0 > (15, 25, 10) |

ee ee

CMT? ))  -or sae pon acer eee
a ie We \ -- Qi a ———----------

1) Separate Chaining 2) Open Addressing
Each index stores a list (linked list) If collision occurs, try the next
of keys that hash to that index. esis let. Siren

_ When two different keys map to the same index, it is 7 |

| |

! :

Example: | Py |
| Lis ]>[25 ]>[10] | Example: Linear Probing

| |

| |

: |

|

|

called a collision.

++ ++ + ? + + >> >> {++} TJ

| Using h(key) = key % 5 0

oe, | 15 %5=0 and 25%5=0 - > collision at index 0 4 [6 ]— NULL 0 ‘ ‘ 3 ‘
ee ee ‘| 2 far]> now

ge : foe [as [ar [as
~ Operations in Hash Table -—----——~~ \ | 3 NULL i

tie | © Insert(key) > Add key to the table 1 > Filled using probing

[

|

| @ Search(key) > Find key in the table

4 ° Delete(key) Remove key from the table

Se ee ee eee ea ee ae Om

ee ee ee ee ee ee - ee  — — -_,

Worst case can be O(n) when many collisions occur.

|

. ii \ |

| ¥ Average time complexity of insert, search, delete is 0(1). | | % Performance depends on the hash function. |

“7 V Efficient for large: detects. | | XK Requires extra space for the table
v Widely used in real-world applications (caching, indexing, etc.). ! \ 4 a : )

<n (We Hashing helps us store and access data quickly. Choose a good hash function Br)
| and handle collisions wisely! Y ; —_—

---

## Page 12

Evaluate a window of size k
it over the data to find the

A technique to solve problems on
arrays / strings efficiently.

yt ee + whee
an {What is is is. Sliding Window? | O-~ 777 7C_How_it works? ----------- ‘ | When to use? }---.

© We keep a “window” (a part) of the data.

@ Do some calculation on this window.

!

| @ Initialize a window with one or k elements.
— @ Calculate something for the current window.
|

=
! © Subarray / substring
i

ETD | © Them slide the window (expand/shrink) to include | | @ Slide the window: —
next element(s) and update the answer. * Expand right (add new element) | @ Fixed size window |
@ This avoids repeating work and reduces time * Shrink left (remove old element) v's

rr ‘ & ¢ e@ Variable size window
complexity. ® Update the result =

© Counting / Sum / Max /

arrey: [a] 3 [-1]-3] 5] 3] 6] 7

Example (size = 3)

rr nn rn nnn "=e
ab qunanenemenainnmanatiinensscSniibanasanesanesctiiitiesasasinmasd”

cI Min problems
Seg EUS) tt ee iy
7: ffici id
ar t ; PE TRPSHATS [2] Wines 1.31 Seine ow
“(ETS TaTeT2] wae |

Window 2. Variable Size Window

Window size is not fixed.

1. Fixed Size
Window size (k) is constant.
We move window of size k
from start to end.
Example: Max Sum of
Subarray of size k

|
|
|
|
|
!
|
|
|
|
!
|
!
array: [2] 4] 5]1]3[2] | suring: [a[oTe[b[e |e] 6
!
|
|
|
|
|
|
|
!
|
|
|
!

\
Y Maximum Sum Subarray of size k !
ow First Negative Number in every window of size k
A |
v
v I

Example: Longest Substring Longest Substring with At Most K Distinct Characters

without Repeating Characters

ee ae ee ne oe > ee ee ns om es oe ee oe ee oe ee ee ee eee es ae are ee ee a

We expand right and _ >
14 Each element is visited at most twice
i

k=3
Windows:

shrink left when needed.

Bon [bfe|b| b|

© Space Complexity:  0O(1)
_ Cexcluding the data structure used)

I a ee ee ee

L=0
result = 0
for R in range(n):

# Add the next element (expand window)
# Update window state

eines, ala : a; oa
} .
1 3 | sei) 2 ef # |
; ‘Pty left element (shrink window) | Shrink with L an [ J 5
= ! i diti '

# Update window state
# Window is valid
# Update result

return result

define what the window
From O(n) oun || eee |” yl 66

toys w Efficient for large input | % Requires careful handling of | a Chal sh Mb tepsad aad Process only what's needed
A Uses constant extra space peinters and conditions = a by maintaining a window,

“Very useful pattern in Hard to think of the right not the whole data!

---

## Page 13

au,

Catt)

aa,

aus

Ct)

ear,

aa we

C+)

Cantal)

C+)

awe

Cad)

eae

C4)

Ct)

Cf)

eT

anu,

C+)

Ct)

Ct)

¢

\

A smart technique to solve problems
in linear time and constant space.

@ We use two pointers that move through the data
structure (usually an array or string).

i
1

- @ Problems involving pairs or subarrays/substrings.
|

|

| @ The pointers can move in the same direction,

!

|

|

|

@ Sorted arrays or strings.

@ Finding elements with a specific condition (sum, difference, etc.).
opposite directions, or at different speeds.
@ Reversing or rearranging data.

© eee ene awaneanenanananasenesas®

_ @ Problems where brute force leads to TLE.
re Poe eee a et ee an eee ee /
ee —
i
1. Opposite Direction 2. Same Direction 3. Different Speeds We Pair with given sum in sorted array

One pointer starts from Both pointers start from One pointer moves faster
the beginning, the other the beginning and move , than the other to cover

|

|

We Remove duplicates from sorted array
WW Valid Palindrome
|
|
|
|
/
i
!

from the end. They move | towards the end. | bilities, le!

“a oe Hie = Ye Container With Most Water
t2tste ts) [ape sais} [Ape] sts | | sy tsum (variations)

t I | f t | a i He Linked List Cycle (Floyd's Algorithm)

Merge Sorted Array
Use for: Pair sum, Palindrome | Use for: Finding duplicates, | Use for: Linked list cycle, any ;

check, Container With Most | Subarray problems, Remove | Trapping Rain Water, Some

_ SSeS  e

Water, ete. | elements, etc. | subarray problems, etc.
JP ee ee ee a oe ee oe ee ee ee 6 ee ee ee
e i
— ~—--------[ How Tk Works? (Examples) }——————-------
1. Pair Sum in Sorted Array 2. Remove Duplicates from Sorted Array | 3. Valid Palindrome
Find if a pair with sum = 9 exists. Array: [1, 1, 2, 2, 3, 3,4, 4] Check if string is palindrome !
Array: [1, 2, 3, 4, 5, 6, 8] | Use slow (i) and fast (j) pointers bios wiumae |

String: "A man, a plan, a canal: Panama”

CPE REET)

; ; ja}mfatnfalpfalafalcfa}alt|pjala}mia
ij 1 1
ij

| me R
| Move L forward and R backward,

[AL 2T 3] 4] | [|| | sting non-lphanimeris characters

[Set [Fret ml] Ma
Boge
pf] na

(Not needed)

(First 4 elements are unique) If all matched —> Palindrome SY
Time Complexity: O(n
\ ty (n) | Time Complexity: O(n) Time Complexity: O(n) }
ee
I 1 j —— \ { = cl L
| © Reduces time complexity significantly.| | 3 Not applicable to all. problems | @ Understand the problem clearly. ~y’
|

@ Uses constant extra space O(1).
|
— @ Works well on sorted data.

|
\ 4

.. . - ieee rence = ms a .

|
| © Often requires the data to be sorted. @ Decide direction and movement of pointers.

|
ie
| can be tricky initially. @) pe eae es ee Ore
‘ J \

---

## Page 14

REFIX SUM

(CUMULATIVE SUM)

Quickly find the sum
of elements in any

range of an array.

wy.

> ~~~ What is Prefix Sum? | ------~ ~ yo Ti to Build? @ ~~ f Range Sum Query —= .
i a a ES \ ~ - - -_ - - 4 we. —-
Prefix Sum array stores the sum of elements from 1. Create prefix(0...n-1] | Sum of elements from index L to R
A the beginning up to that index. prefix(O] = arr[0] (0-indexed)

| prefix[i] = prefix[i-1] + arr[i] (if L > 0)
— r¥ ; prefix[R] (if L = 0)
by (EE
0 1 3 4
Prefix Sum (prefix):
Pia APES et] 2a
0 1 2 3 4
} | ! | !

2 =. 2+4e6 244-405 2+4-143+5=13
2+4-14328

we we ee _ -——- -

# arr is O-indexed  )

prefix(O] = arr[0]

for i = 1 to n-1:
prefix[i] = prefix[i-1] + arr[i]

(ar :[(2, 4 -1, 3,5]
prefix ; nid, Gy 5, 8 asi
Sum of arr[1...3] ?
= prefix[3] - prefix[0] |
=8-2=6 (4+(-1) + 3= 6) |

Bile a emmaincinamesncineeasasenan

CS Tips
: O(n) | si vJI,
| : oe © Can be extended to 2D Prefix Sum for matrices. |
‘i

a =J)--. -—- Gia

i Bt ke Soe Sait! i |e ae }
=e ee | _ 73 aL ae ol © After all updates, rebuild the array in O(n).
‘ * if (Red <n) diff[R+1] -= val © Much faster than updating each element |

| @ diff{i]) = arr[i] - orr[i-1] (for i > 0) ot
GY After doing all updates, convert diff back to arr See a Se

= arr (initial): rc s38 2 6& 29 1) Add +5 to range [1, 3]
Difference array (diff): We want to add +10 to range [1, 3] 2) Add +3 to range [0, 2]

|

|

|

!

!

'

| Original array (err): [3] 5 | 2 | 6 | 1 |
oO” 6, t 27 's* -¢
!

|

Step 1: Build diff
af: [3 2 -3 4 -5]

Start with diff = [0 0 0 0 0]

WE ears
Le) 1 2 3 4

= t I i I t a » Update 1: L=1, R=3, val=5
: Update dil
\ 3 S-Be2 25-3 6-294 1-6-5 | ot ry et afi} +5 +[0 5 0 0 0}
\ 2 , , aff(4] -5 +~[0 5 0 0 -5]
diff[1] += 10 —- 2+ 10 = 12
=, From diff to original array diff[4] -- 10 —- -5 - 10 = -15 Update 2: L=0, R=2, val=3
Vv 0} = diff[O ! | . _ =
ro Co) <a’ || Updeted af: [3 12 -3 4 -15] Pages SIP Ss 8 0 6)
2. For i from 1 to n-1: =| diff(3] 3 + (3 5 0 -3 -5]
4 orr[i] = arr[i-1] + diffi) Step 3: Convert diff back to arr

Index 0 1 2 3 4

LR Gad ary ir ed

arr(O] = diff[O)
for i = 1 to n-1:
arr[i] = arr[i-1] + diff[i]

“When to Use? _ iia
WS Use Prefix Sum when you need to answer 66 = |
Update Not efficient | Very efficient (O(1)) many sum queries on a static array.
Preprocess O(n) 0(1) many rengs i the final Difference Array —+ Quick updates before
Extra Space | O(n) ‘thy ter

---

## Page 15

A stack is a linear data structure that follows
the LIFO (Last In First Out) principle.
Insertion and deletion of elements takes place
at the same end, called TOP.

wae ewes eu=en a= aenanananes””

{
|
|
|
|
1
l
|
|
|
|

removing

: Check if the stack is empty.

: Check if the stack is full
(for fixed size stack).

¢ Increase TOP by 1. pment
e Add the element x
at the new TOP. | 10 |— Tor

at TOP.
¢ Decrease TOP by 1.

. Backtracking
(maze, puzzles)

2. Undo Operations — . Function Calls
(in editors) (recursion)

. Syntax Checking

| Pe Stack follows LIFO (Last In First Out).
we All a are done at the TOP.
| We push =

: Return the top element without

Store data so that
the last item added
is the first one
removed.

_ Basic Idea

@ Think of a stack like a stack of plates.
e We can add a plate on the top.

e We can remove only the top plate.

@ The bottom plate is removed last.

: Add element x to the top.

push(10)

: Remove and return the top element. push(20)

push(30)

it.

1) Fixed Size Stack (Array Based)
e Size is fixed.

e Uses array.

e Overflow possible.

2) Dynamic Stack (Linked List Based)
e Size is not fixed.

e Uses linked list.

¢ No overflow until memory

is available.

SS SS Sy

\
!
1 |

| element is accessible).
|
|
|
|
|

l
V Efficient operations (0(4)). !
! _ X& Overflow possible in
|

|
fixed size stack.
|
\

Keep calm and stack it up!
(Use stacks to solve problems step by step.)

---

## Page 16

First In
First Out!
(FIFO)

—{ Key Idea
A queue is a linear data structure that follows | | a

the FIFO (First In First Out) principle. | © Think of @ queue like a line of people.
@ New people join at the end (REAR).

@ The person at the front leaves first (FRONT).

REAR

*® enqueue(x) : Add element x at REAR.

Insertion is done at the REAR.
Deletion is done at the FRONT.

° dequeue() : Remove and return element
from FRONT.

front() —: Return the element at FRONT —
rear() : Return the element at REAR.
isEmpty() : Check if queue is empty.
: Check if queue is full dequeue() — removes 10

(for fixed size queue). I | | _|2o}30] | |

dequeue() — removes 20

------ ~~” How enqueue( ) and dequeue() Work? --——_ See — F
i Cie at Guach
_enqueue(x) _ Pee | ——= \
© Add element at REAR. © Special Case: ) | | 1) Linear Queue (Simple Queue) |
| ee epee | | @ Elements are added at REAR

a: aeaeny la ee. ai and removed from FRONT. 10] 20/30] | |
fo [ols] > felayeyo] + Once REAR reaches end |
FT etc || ne more itn t t |
FeR=0

N 3. When last element
© Remove element from FRONT. 7 2) Circular Queue

FeRe-t
| @ Move FRONT one step forward. © Last position is connected

Cae bard + _ Fpl 1 | © Better uiization of space.
F F |

Variables:
|| int queue[MAX], F = -1, R = -4;

| | . 1 |

A Useful in real-world | é |
(Tickets, Banks, etc.) = = 1 ed
. Level Order Traversal || r a | ,

ewan anhk> of. 3 a
~

-

‘Q Remember: Queue follows FIFO - First In, First Out! Vy)

---

## Page 17

A linked list is a linear data structure where
elements (nodes) are stored in non-contiguous
memory locations. Each node contains: The last node points to NULL.

© Data (value) Data | Next | | Size is dynamic (grows or shrinks at runtime).

e Address (link) of the next node Efficient insertion and deletion.

The first node is pointed by HEAD.

Types of of Linked List
4. Singly Linked List

2. Doubly Linked List

nu ~+{ 10] |ee[20] e230] fe in ‘ Basic Operations ag —————

: Create an empty list
traverse() : Visit and display all nodes

| nM Fao] > [zo] > insert_at_beg(x) : Insert x at beginning
insert_at_end(x) : Insert x at end

| : :

\

------ SS - e

| 3. Circular Linked List (Singly)

insert_after(key, x) : Insert x after given key
delete _at_beg() : Delete first node
delete_at_end() : Delete last node
delete_after(key) : Delete node after key

© search(key) : Search a node with key

-4 “How Insertion and Deletion Work? (Singly ‘Linked List) )

civil at Beginning rg f =
HEAD ' @ Dynamic size

|
|
|
i soll [20] Fe Nu. => “.D-ECbEL+ ee @ Easy insertion/deletion

| Insertion ot End @ Efficient memory utilization

fi +2. > Le L HL m | { Disadvantages )
| Deletion of a Node with key = 20 | © Extra memory for pointer
HEAD al HEAD ! [x] No random access
L_,ftoy (20]'»[30] }> NULL > fo] [eT b NULL (sequential access only)
 & 7 a ! © Traversal is required
\ to access a node

\
~ -

Memory Representation (Singly)

500 1000 2000

. Dynamic Memory Allocation | printf ("Yod _ temp->data);
. Undo/Redo in Applications

---

## Page 18

A Tree

represents

Hierarchical
Dota!

7]

-—<—<— ee

\
@ Root — : Topmost node (no parent)
@ Parent : A node that has children

| @ Child : A node which has a parent
@ Siblings : Nodes with the same parent

(
A tree is a non-linear data structure made up of
|
|
| @ Leaf Node : Node with no children
|
|
|
|
|
|
\

1
|
|
nodes connected by edges. It has a hierarchical |
structure with a single root node and zero or more
subtrees.

!

— Root

e 1 is root
© 2, 3 are children of 1 |

!
© 4, 5 are children of 2 |

@ Internal Node : Node with at least one child

© Degree of a Node : Number of children of that node
@ Degree of a Tree : Maximum degree among all nodes
@ Level : Position of a node (root is at level 0)

© Height of a Tree : Maximum level of any node

[a
Ca ee re es )
i= a + Types of ie ———-_____
| 4. General Tree 2. Binary Tree
tor | A node can have any A node can have at most ' 1. Linked Representation
number of children. two children (Left & Right). |

iV ECS

4. Complete Binary Tree
All levels are completely
| filled except possibly
the last level, which is
filled from left to right.

Inorder Traversal (LNR):
40, 20, 50, 10, 30, 60

|

| em - Tree Traversal (for Binary Tree) } ——-------------- ore ——————

1. Inorder (LNR) | 2. Preorder (NLR) | 3. Postorder (LRN) wv A tree with n nodes has n - 1 edges. |
i Node —> Right Node —> Left — Right | Left —» Right —> Node | (Where n > 0)

VW Only one path exists between any two
nodes in a tree.

| Output: 40, 20, 50, 10, 30, 60
pl °

eS Se ee ee ee ee ee ee ee ee ee ee ee ee ee

‘/‘ _—yy *. )
————————

|

!

X More complex to
|

l

!

!

|

|

|

\
W Expression Trees (compilers) |
WF File systems (directories) !
WW Hierarchical data (org charts)
|
|
!
1
|

|

|

_ W Efficient search, insert % Consumes more memory i

! and delete (in BST). (pointers). ;
VW Scalable and dynamic. X Not suitable for simple

© search() : Search a node WY Searching (e-g,, Binary Search Tree)

© traverse() : Traverse i, | YW Decision making, AI, networking

---

## Page 19

| BINARY SEARCH ;
TREE (BST)

A Binary Search Tree (BST) is a binary tree in Example BST

\
e It is a Binary Tree.
which, for every node: \ | yy
@ For any node, LEFT < NODE < RIGHT. ~

© All keys in the LEFT subtree are LESS a

in SORTED (ascending) order.
© No duplicate keys (or duplicates are handled
consistently).

e All keys in the RIGHT subtree are GREATER

!

|

|

|

|

|

than the node's key.
|

than the node's key.
\

i
i
|
|
|
|
@ Inorder traversal of a BST gives the keys
|
|
|
|
\

~-----—-—--4-

oo

struct Node { The left child of a node
contains smaller keys.

int key; left | key | right The right child contains

struct Node “left;
struct Node *right; y \ greater keys.

Cee cee ee an > ae a oe ~— — —

eS SED GE GENE SEED GENS ee EE EE SE ES EE SS Ee

a oe —— | Basic Operations a a , i as ——a
{ - | \
1. Search(k
aes earch(key) 2. Insert(key) 3. Delete(key) | 4. Inorder Traversal
Te rem St eae Re * Start from root. ae | Visit Left + Root — Right
the path. e Find the correct position '
If key == node->key —> Found | where key should go. 1. Leaf Node — Remove it. | Result is sorted order.
=
sl e If key < node->key — go LEFT e Insert as a leaf node. 2. One Child - Replace with |

the child.

3. Two Children — Replace
with inorder successor
(smallest in right subtree) |
or inorder predecessor

(largest in left subtree).

© If key > node->key —> go RIGHT

: OCh)
: Oh)

! ( Where h = height of the tree

@ Best Case (balanced) : O(log n)
c Worst Case (skewed)

me re a ee a ee a ee ae ee a ee ee ee ee

---- CT —-- en

X Performance depends on tree height
| | % Can become skewed (like linked list)

Efficient Search, Insert, Delete (avg. O(log n)) |
Inorder traversal gives sorted data
in worst case

v

v

Wo Dynamic size |

WV Widely used in databases, compilers, ~ she % Requires balancing to maintain efficiency
if (use AVL / Red-Black Tree)

= Fast and Smart Data Management! ()

“$Y BST = Binary Tree + Search Property

---

## Page 20

bosed structure : :, ] Efficiently find and remove
used to implement Se the element with highest

Priority Queue! Lp Yl (or lowest) Priority.

Max Heap
A Heap is a Complete Binary Tree that satisfies
the Heap Property.

\
|
|
I
I
|
e@ Max Heap : Parent node is greater than
or equal to its children, |

|

: Parent node is smaller than |

|

/

or equal to its children.
50 = 30, 50 = 40 10 < 20, 10 < 15

30 2 10, 30 = 20, 40 2 35, 40 2 25 20 < 40, 20 < 50, 15 < 30, 15 < 25

|
|
|
|
|
|
|
I
|
|
|
|
|
|
|
|
|
|

dl \

> he Priority Queue using Heap __
i 5 a . y \
A heap can be efficiently represented

| | ,
| using an array (0-based indexing). . Max Heap _ @ In a Max Heap based PQ, element with

highest priority is at root.

Root has the maximum key.
| | Used when highest priority @ In a Min Heap based PQ, element with
| @ Left Child | element is served first. lowest priority is at root.

| @ Right Child |
Root has the minimum key. Insert (push) O(log n)

Used when lowest priority Delete Top (pop) O(log n)
element is served first.
Peek Top
| Build Heap

‘ How Operations Work? (Example using Max Heap) )

1. Insert (push 45) 2. Delete Top (pop) | 3. Peek Top | 4. Build Heap (from array)

\

|

:

@® Insert at the end. | @® Replace root with last element. suis iis wat Wael Convert wo yt
@ Heapify bn with parent | @ omni last element. (For Max Heap, highest value) | |
and swap if needed). | @ Heapify Down. | Array : [ 10, 30, 20, 5, 15, 25,2] |

Insert 45 | Initiol Heap
Replace 50 (25)
(50) aad (Start from last non-leaf to root)

(40)  Heapity Up | (30) (40) (G0) (40)

% Does not support fast search —
| : ; that satisfies Heap Property.
's Algorithm | ne Sat eng eae eee © Max He Fe Mani A
eS ap ’
aves i ary od a | | @ Min Heap -> lowest priority at root. |
YY Top K elements | requiring ordered traversal - :
WV Good for priority based operations @ Used to implement Priority Queue !

ee cr do vuenanter efficiently,

Heap makes Priority Queue operations FAST and EFFICIENT! @

---

## Page 21

(\\

[\\

({\\
a

{\\
H

((\\
L

™
H

/\\

AN
a

aN
L

™
LY

((\’\

aN
L

by edges.
Gt - Ss a =
~~~ 1. Basic Terminology ~~~. —-{ Fr’ 2. Types. of "Graphs

@ Adjacent: Two vertices are adjacent if
there is an edge between them.

@ Degree: Number of edges incident on a vertex. |

@ Path: A sequence of vertices connected
by edges.

@ Cycle: A path that starts and ends at the —
same vertex.

@ Connected Graph: There is a path between
every pair of vertices.

Se ee ee = Se

A Graph is a non-linear data structure
consisting of vertices (nodes) connected

© Undirected Graph A

© Directed Graph ve

(a) BFS (Breadth First Search) | (b) DFS (Depth First Search)
|

(Tdea:} Visit all neighbors [Idea:) Go as deep as possible
at the present depth | along a path before
==, (222g

: o
| & ®
@©@ © ©

!
1
|
|
|
|
|
i
1
|
1
1
!
1
|
|
|
I
!
!
|
'
|
!
t
/

BFS starting from A: starting from A ee
A, B,C, D, E, F B, D, E, C, F >
See ee ee yg ee J
a Common Algorithms — _ 8. Minimum Spanning Tree (MST)
| A tree that connects all vertices with minimum
total edge weight. A
One MST
| (x) —{8)
! 4
?
2

} Rectatok (a4 gf oieral | % Complex to implement for
© Adjacency List: Space O(V + E) VF Flexible (directed / undirected, large dense greghs
© BFS / DFS: O(V + E) Ts saben x

Bs

Total weight = 1+4+2+1=8

W Many efficient algorithms available.

where every pair is reachable.

Cycle Detection: et Chen nan!
Topological Sort: Linear ordering of vertices in a
two vertices.

* Weighted Graph (positive weights) —> Dijkstra’s

@ Degree of a vertex = number of
@ Sum of all degrees = 2 x (number
of edges)

Directed Graph (Digraph)
@ In-Degree: Number of edges coming in.

@ Total Degree = In-Degree + Out-Degree

FE Social networks (friend connections)
YE Road / Network routing

VE Web page ranking (Google)

VY Recommendation systems

FE Dependency resolution

FY Al and Game development

© Out-Degree: Number of edges going out.

---

## Page 22

[
|
|
|
|
\

Solve problems by
always choosing the
(hoping for the best

A greedy algorithm builds a solution step by step. ~¥ When the problem has Greedy Choice Property
At each step, it chooses the best local (immediate) (local optimum leads to global optimum).

option. It never reconsiders previous choices.

~¥ When the problem has Optimal Substructure
It is simple and efficient but does not always give (optimal solution contains optimal solutions to

the optimal solution. subproblems).

, _ Example : Activity Selection Problem —
@ Start with an empty solution. ices Given activities with start and finish times, select

Q@) Choose the best option among the Best Choic | overlap.
available choices.

@) Add it to the solution.

4) Remove the chosen option from
further consideration.

6) Repeat steps 2-4 until the solution

is complete.

Activity Selection Problem = Given items with value and weight, and a knapsack of capacity W.
Fractional Knapsack Problem | | | Take the fraction of items to maximize total value.

Huffman Coding (Data Compression)
Minimum Spanning Tree (Prim’s, Kruskal’s)
Dijkstra’s Shortest Path (non-negative weights)
Job Sequencing with Deadlines .

V Simple and easy to implement. | XX Does not always give optimal solution.
~ Usually fast (less time complexity). % Needs proof to show it works for a
\ % Not suitable for all problems.

“

the maximum number of activities that do not

Greedy Selection:
Ai > A2 > A4 — AS

Greedy (by Value/Weight):

1. Take item 1 (weight 10) > value = 60

. Take item 2 (weight 20) > value = 100

. Take 1/3 of item 3 (weight 10) > value = 40
Total Value = 200 (Capacity = 40)

\
|
;
!
|
i
|
|
|
|
|
|
|
;
!
|
|
/

wv Always check greedy choice property.
YY Sort the data if required.

---

## Page 23

DYNAMIC ~
PROGRAMMING

,
lm
/
Dynamic Programming (DP) is an algorithmic technique | Don’ : .
t te th and ,
used to solve problems by: | : i pean Hag nm gem again
1. Breaking the problem into smaller subproblems. _— a
2. Solving each subproblem only once (Memoization). |e Build the solution from the stored results.
l

3. Storing the solutions and reusing them. : ;
; : Break into Solve & Store Use Stored Get Final
Overlapping Subproblems + Optimal Substructure w _ , - .

|
\

aoe

4

1. Memoization (Top-Down)

e@ Use recursion + a table (memo) to store
results.

| 2. Tabulation (Bottom-Up)

@ Solve smaller subproblems first.
© Store results in a table (usually an array).

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
Formula: F(n) = F(n-1) + F(n-2)
Base cases: F(O) = 0, F(1) = 1

! @ Compute only when needed.
@ Easier to implement.

2

eres [ems |e |e
Hig! 1.2 2.1 2.2

\

@ Iterative approach.

[Seat [sss] — Leo fo ft] 23] 5 | 8 |
: ; Without DP (Recursion): Many repeated calls!

With DP: Each F(n) computed once and stored.
Both give same result,

but Tabulation is usually <
more space efficient (no

recursion stack).

Time complexity reduces
from exponential (0(2**))
to linear (O(n)).

_{ Characteristics of DP Problems | --. (Common Problems Solved Using DP).
2 — ,, ——— =— = =

Fibonacci Series
0/1 Knapasck Problem
Longest Common Subsequence (LCS)

(
|
| Can be soe using Menaization or Tabulation |
|

‘

‘
'

“GAN W% Define state clearly (what does dpli) represent?).
W Choose base cases carefully.
W Store and reuse results to avoid recomputation. 1)

Se ce ee ee ee oe a > ee es ee oe ee ee ee ee ee ee oe ee es eee

Dynamic Programming turns repeated work into smart work!
Store once, use many times, get the optimal solution. yy)

LY

---

## Page 24

—

12)

+ = =

Mf;

Backtracking is an algorithmic technique for solving
problems step by step, trying all possible choices.
If a choice leads to a dead end (no solution), we
backtrack and try another choice.

It is used to find all or one of the possible solutions.

a
I

x

ee —

— eC

—@ Moke a choice.
| @ Check if the choice is valid and moves

us towards the solution.

| @ EF valid, move forward (make next choice).

7 backtrack (undo the last choice) and | Solution
try another option. Found! x

|
backtrack(state):
if solution(state):
print/record state

return
for each choice in choices(state):
if is_valid(state, choice):
make choice
backtrack (next_state)
undo choice // backtrack

em a a ee ne ee we we we we we we we oe we ee ae ee

\
!
Wo Finds all possible solutions. :
Vo Simple and easy to implement. |
|W Works well for constraint-based problems. |

(> qu Gn Gn GED GED GED GEDaED aan ee eewaneranan” —

@ Examples: N-Queens, Sudoku, Rat in a Maze,

en»

Ca
‘oie €

X May explore many unnecessary paths.

ee ee ee es ee cee es ee oe ee ee ee ee _— oe oe oe S

Hy Backtracking explores possibilities, learns from mistakes, and finds the way to success!

{

@ When we need to explore all possibilities.
| @ When the problem has constraints.

e When greedy strategies do not work.
|

|

|

|

BACKTRACKING

Subset Sum, Permutations.

Place N queens on an NxN chessboard so that no two
queens attack each other.

Example: 4-Queens (one solution)

Step 3 Step 4 (Solution)

~— ee

_—— ee ee ee

Find a path for the rat from start (0,0) to destination (n-1,n-1).

ee ———— > ae oe ow a ee ae

—— ee ee eS eS  -,

vw Prune early: Cut off invalid paths as soon as possible.
w Use constraints to reduce the search space.
Ww Good for problems with many choices and constraints.

J anenasenses,,

---

## Page 25

(/\\

[/\\
a

™
a

/\\

(/\\
a

(\\
a

(/\\

Mm MM MM 2 M™ Mm MM Mm mm
a a a L a

[\\

(/\\

 & TRICKS #

patterns and smart tricks!
—_—

EW PATTERNS)

Oe \” = -
| ro~
_ YR GOLDEN RULES _ '

ey 1 || Write code that others

Understand Plan Your Test |
Solve / Code
% : al WV Simplify the problem. |
output & constraints. © Think of brute force > , ain © Check val 5 ici cate!
eee te | COMMON PROBLEM PATTERNS
1. Two Pointers 2. Sliding Window  ' 3. Fast & Slow Pointers | 4. Binary Search 5. DFS / BFS
| — |) choo || o-o-o-0 || GT ao
; : slow fast L m r (2) (3) |
Used fer gorda, ervayey patra Used for subarrays/substrings Used. in linked list middle |
gp a ned pitted: i: ce cycle, Used for sorted array, search (4) (5)
; ; _ ada | Used for graphs, trees,
Trick: Move pointers based Trick: Expand window, then Trick: Fast moves 2 steps, Trick: Al dittde hich | quewrenibed’ components.

Trick: Use BFS (Kahn's Algo)

slow moves 1 step.

Example: Linked List Cycle,
Find Middle of LL

Trick: Define state, write
transition, use memo/tabulation. Trick: Choose -> Explore —

Unchoose (backtrack).

or DFS + stack.

: Course Schedule IT

ee? -a
”. ' ae ae et oe

Use HashMap / Set -» For frequency, lookup, duplicates.

Trick: Sort + pick the best
choice at each step.

half to keep. Trick: Choose DFS for depth,
eee ee BFS for level/shortest path.
Sorted Array Example: Number of Islands,
_ Course Schedule
9. Greedy “10. Heap / Priority Queue
(1)
000 —> ¥ 3) @

O® ®

Used for top K, merge, streaming
median, etc.

Trick: Use min-heap / max-heap
smartly.

Example: Kth Largest Element

COMMUNICATION TIPS ~

>

J

Bit Manipulation —* For XOR, subsets, power of two, etc.
Math & Geometry -+ GCD, LCM, prime, coordinates.

Reverse & Think Backwards -* Sometimes easier!

O(n?)

| | GS Be calm, think step by step.

0(2'n)

LY O(n!)

_ STUDY PLAN (SUGGESTED)

| 'D Practice patterns, not just problems. W Learn 1-2 patterns at a time. ‘
Y Learn from mistakes.

A Revise & build your template.

"SHV PATTERN RECOGNITION + SMART TRICKS + PRACTICE = INTERVIEW SUCCESS SP

Wo It's okay to correct yourself.

8

---

## Page 26

(T\\
}

(/\\
L

1AN\
i

[/\\

[/\\

(/\\

(/\\

([\\ ({\\

((\\

({\\

([\\

(/\\

([\\

(/\\

(\\ (/\\ (/\\ (\\ (/\\

((\\

(/\\

“FREQUENTLY ASKED —

DSA

4 ARRAYS ~——SOC=CS*~SS:SC, STRINGS 3. LINKED LIST >, 4, STACKS

| 1. Two Sum 1. Valid Anagram || A. Reverse Linked List 1. Valid Parentheses |
| 2. Best Time to Buy & Sell Stock 2. Longest Substring 2. Detect Cycle in Linked List 2. Min Stack
| & Aten Stergyiaetes's) roe Mapseimy Caters 3. Merge Two Sorted Lists 3. Evaluate Reverse Polish Notation

| - 5. Middle of the Linked List 5. Next Greater Element I

| 7. Majority Element 6. Mini Window Substri 6. Reorder List 6. Largest Rectangle in Histogram

| 8. Rotate Array 7. String to Integer (atoi) 7 Add Two Numbers (LL)

9. Merge Intervals 8. Implement strStr() 8. Copy List with Random Pointer

10. Set Matrix Zeroes |

all EQ o-0-0-0 |

---~-{5. QUEUES }-----~, 6 TREES 7. GRAPHS 8. HEAP / PRIORITY QUEUE

Design < ! ; age of grey — 3. 3. Top K Frequent Elements
Sliding Window imum, i . Order Traversal :
, Coures’ Sait 3. Merge K Sorted Lists
5. Validate Binary Search Tree *. z 5
4. Number of Islands tte L c er 5. Pacific Atlantic Water Flow 4. K Closest Points to Origin
5. First Unique Character | Construct Binary Tree from G. Detect Cycle im Undirected Greph | | 5 Find Median from Data Streom
| Inorder & Postorder 7. Topological Sort
| | : age ™ 8. Dijkstra’s Algorithm (40)
Es ig le ye wD
| front rear fa OnOnOnO
| (3) (4) | (Min / Max Heap)
9 DYNAMIC PROGRAMMING ~ 10. GREEDY — 4. BACKTRACKING --. 12. BIT MANIPULATION
’ a nae _- 1. Activity Selection | Subsets | | 4. Single Number |
> as poy rt 2. Fractional Knapeack | | 9 Permutebions | | 2. Number of 1 Bits
3. House Robber 1
tak Davenmng tidal 3. Jump Game 3. Combination Sum 3. Missing Number |
5. Coin Change 4. Jump Game Il 4. N-Queens 4. Sum of Two Integers
6. 0/1 Knapsack 5. Gas Station 5. Sudoku Solver 5. Reverse Bits
7. Unique Paths 6. Hand of Straights 6. Letter Combinations of a Phone . &- ul te
8. Edit Distance 7. Minimum Number of Arrows Number :
i med % Gray Code
Balloons 7. Generate Parentheses 8

8. Candy . Counting Bits
—— HK : My 1010 <—» 0101 __

eS a

INTERVIEW TRICKS

FF Clarify the question & constraints
FF Think out loud
YF Start with brute force, then optimize

oO
© Trees/Graphs — DFS, BFS, Recursion
°

DP —+ Overlapping Subproblems,

Optimal Substructure BE Ory run with examples

YF Write clean & modular code

Betraing + Eps a pn 27> Le Hae we ce

Ss

— SAY PRACTICE + PATTERNS + CONSISTENCY = INTERVIEW SUCCESS! @

---

## Page 27

Vv Consistency beats talent.
|| Z Understand > Memorize.
W Practice > Perfection.

DSA is not just about solving problems,
it’s about building problem-solving skills.

SADX- © Important data structures | @% Choose the right date structure © Helps in cracking coding
and their uses. for the right problem. interviews.
@ © Powerful algorithms and @ Identify the pattern before © Improves logical thinking
problem-solving techniques. jumping to code. and problem-solving.
© Common patterns to @ Break the problem down @ Builds a strong foundation
solve problems efficiently. for advanced topics.

© Smart tricks to optimize @ Useful in real-world
projects and systems.

= Se, A
__ TIPS FOR SUCCESS

Fe Solve problems daily. DSA is a journey, not a race.

WW Revisit and revise regularly. ! ; ,
a petra ith Enjoy the process, celebrate small wins,
W Discuss and learn with others.
ww Stay consistent and never give up! You've got this! iy)

and keep moving forward.
