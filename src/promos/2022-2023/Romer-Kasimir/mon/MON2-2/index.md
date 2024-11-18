---
layout: layout/mon.njk

title: "MON 2.2 - Langage assembleur"
authors:
  - Kasimir Romer

date: 2023-01-25

tags:
  - 'temps 2'
  - 'assembler'
  - 'reverse engineering'
  - 'arm'
  - 'x86'
---
<!-- Début Résumé -->
Dans ce MON, je vais apprendre les bases du langage d'assemblage ARM. Si le temps le permet, j'étudierai le débogage avec gdb car c'est un bon cas d'utilisation pour appliquer les connaissances de l'assembleur.
<!-- fin résumé -->

<!-- ## Structure de ce MON
1. Introduction
  - What is assembly language?
    - Assembly vs high-level language
  - Use cases of assembly language
    - Super fast execution
    - Embedded systems (memory constraints, ...)
    - Reverse engineering -> most important for me personally
  - Differences of different assembly languages (x86, ARM, ...)
2. Assembly language for ARM
  - why? -> ARM is used in many embedded systems and will be used more and more in the future
  - follow tutorial on https://azeria-labs.com/writing-arm-assembly-part-1/
3. Assembly language for x86
  - not in depth, only show the key differences to ARM assembly
4. Reverse engineering with gdb, radare2 and Ghidra (only if time permits)
  - gdb
  - radare2
  - Ghidra
5. Useful resources
  - Online resources
  - Tools (like online assemblers, ...) -->

## Introduction
{% prerequis "**Prerequisites**" %}
To follow this MON (or any tutorial other on assembly programming), you should have basic knowledge of computer architecture and programming. You should at least:
- Understand the basic concepts of a computer (CPU, memory, input/output, ...)
- Being familiar with binary and hexadecimal numbers
- Know the basics of at least one high-level programming language like C++ or Java

For a deeper understanding of machine language and compilers, see the [MON of Jean-Baptiste](../../JBD/Mes_MON/compilateur) (but that's not necessary for understanding this MON)
{% endprerequis %}

### What is assembly language?
Assembly language is a very low-level programming language. It is being translated to machine code (binary code executed by the CPU) by an assembler. Because it is so hardware-near, it is very fast and efficient. However, it is harder to read and write than high-level languages like C++ or Java, that's why it only used in few use cases nowadays.

### Use cases of assembly language
Assembly language is nowadays mostly used in **embedded systems** like microcontrollers, where the hardware is very limited (in terms of memory and processing power), so the performance of the code is very important. Because assembly language is hardware-near, it is used in cases where hardware-specific functions need to be used. Additionally, assembly language is used in **reverse engineering** to understand how a program works. The code recovered from a program can be disassembled to assembly language and then analyzed.
Besides those use cases, it is great to learn assembly language in order to **understand the architecture of a computer** with its CPU, registers, memory and I/O. It is also useful to understand how a program works in general and how it is executed by the CPU. This allows better software development and debugging, e.g. by knowing potential for optimizing or better securing the software.
Other special use cases are **OS and driver development** because some of the functions in those area can't be implemented in high-level languages. Assembly language is used unknowingly by many programs, because the compiler that compiles high-level languages (C and C++ code) **generates assembly code**.

### Differences of different assembly languages (x86, ARM, ...)
There is no single "assembly language" because the instruction set of every CPU varies and therefore the language to control those instructions also varies. This means that every CPU has its own assembly language, but as they are very similar, it is possible to learn one assembly language and then learn the others relatively quickly. They share big parts of the syntax, so one can adapt quickly to a new assembly language if he needs to program for a different CPU. Nowadays, mainly two families of CPUs, and thus two families of assembly language, are used: x86 and ARM.

#### x86
The x86 family is used in most **desktop computers**. The CPUs of the x86 family use a **CISC (complex instruction set computer)** architecture. CISC CPUs have a larger, more complex instruction set with many specialized instructions for a variety of tasks. This allows them to perform a wider range of functions, but at the cost of slower execution times and increased complexity in the CPU. Because the instruction set is so complex, it is not easy to learn x86 assembly.

The most well-known CPUs of this family are the Intel Core i3, i5 and i7 CPUs and the AMD Ryzen CPUs, so the chances are high that the device you are using to read this MON at the moment operates with on a x86 architecture.

#### ARM
The instruction set of the ARM CPU family is much simpler because it uses a **RISC (reduced instruction set computer)** architecture. RISC CPUs have a small, fixed instruction set with a limited number of instructions that can be executed quickly. This reduces the complexity of the CPU and allows it to execute instructions more quickly, at the cost of some flexibility. However, some instructions that can be executed in one step on a CISC CPU need multiple steps on a RISC CPU.

ARM CPUs are used in most **mobile devices and embedded systems**. The most common CPUs of this family are the Apple A-series CPUs like the A15 Bionic which is used in the iPhone 14 and the Qualcomm Snapdragon CPUs like the Snapdragon 888 which is used in the Samsung Galaxy S21. In many embedded systems, ARM Cortex CPUs are used like the Cortex-M4 which is used in the popular STM32F4 microcontroller. ARM also spreads into the field where x86 is dominating, e.g. with the Apple M2 chip which is used in the newest MacBook Air and the MacBook Pro and is considered extremely energy-efficient while still being very powerful. This shows that ARM will get even more relevant soon and could replace the x86 architecture in many domains.

## Assembly language for ARM
{% prerequis "To learn ARM assembly, I used the following sources:" %}
- [Assembly Language Programming with ARM – Full Tutorial for Beginners (YouTube)](https://www.youtube.com/watch?v=gfmRrPjnEw4)
- [azeria-labs.com - Writing ARM assembly](https://azeria-labs.com/writing-arm-assembly-part-1/)
- [Larry D. Pyeatt: "Modern Assembly Language Programming with the ARM Processor" (book)](https://www.amazon.fr/Modern-Assembly-Language-Programming-Processor/dp/0128036982/)

The YouTube tutorial focuses more on showing the different instructions, while the azeria-labs blog series digs deeper into some of the topics and allows a very good understanding of the most important concepts. In my opinion, the combination of those two sources is great to learn ARM assembly, they complement each other well.  
{% endprerequis %}


### Running ARM assembly code
To use the ARM assembly language, you need a device containing an ARM (micro)chip where the assembled code is stored and executed. For example, the _Raspberry Pi 4 Model B_, the current version of the Raspberry Pi computer, uses a Broadcom BCM2711 SoC (system-on-a-chip) that includes the Cortex A-72 ARM chip as CPU. This means that you can use the ARM assembly language directly on the Raspberry Pi to get a real-world experience and direct hardware integration, e.g. you can blink the onboard LED etc.

If you don't have access to an ARM chip, an emulator can be used. The advantage is that you can inspect the whole memory at every given time, easily understand changes that the program makes to the memory, and that you don't need to flash the device with the new code after every change that is made in the code. You can find an online ARM emulator [here](https://cpulator.01xz.net/?sys=arm-de1soc).

In this MON, I will mainly use the emulator to write and execute the assembly code. Maybe later, I will test it also with the Raspberry Pi 4 that is laying around in my room.

### ARM assembly basics
#### Registers
Registers are the closest memory to the CPU. It is a small amount of memory that is directly accessible by the CPU, thus the CPU can read and write to the registers very quickly. One register can store data of the length of one word. A word is a fixed number of bits that can be stored in a register. The number of bits depends on the CPU, for example, the ARM Cortex-M4 CPU uses 32-bit words, so one word is 32 bits long and therefore a register can store 32 bits.

Some of those registers are general purpose registers (e.g. R0-R10) and some of them are special purpose registers:
- R7: holds the syscall number
- the program counter (PC): stores the address of the next instruction to be executed
- the stack pointer (SP): stores the address of the top of the stack
- the link register (LR): stores the address of the next instruction to be executed after a function call
- the current program status register (CPSR): stores the status of the current program (e.g. CPU mode, interrupt mask, overflow flag, carry flag, zero flag, negative flag)
- and more that will be described later when they are necessary

#### Instructions
In general, an instruction in ARM is constructed as following (based on [this article](https://azeria-labs.com/arm-instruction-set-part-3/#:~:text=INTRODUCTION%20TO%20ARM%20INSTRUCTIONS)):
```armasm
MNEMONIC{S}{condition} {Rd}, Operand1, Operand2
```
- MNEMONIC     - Short name (mnemonic) of the instruction (e.g. ADD, MOV, LDR, ...). It doesn't matter if the mnemonic is in upper or lower case.
- {S}          - An optional suffix. If S is specified, the condition flags are updated on the result of the operation
- {condition}  - Condition that is needed to be met in order for the instruction to be executed. This will be explained in the paragraph **Conditional instruction execution**
- {Rd}         - Register (destination) for storing the result of the instruction
- Operand1     - First operand. Either a register or an immediate value 
- Operand2     - Second (flexible) operand. Can be an immediate value (number) or a register with an optional shift

##### Entry point
The emulator automatically inserts the first two lines of the program automatically:
```armasm
.global _start
_start:
```
_\_start:_ is a label that is used to divide the code into segments. If we go to a label, we execute the code below this label. _.global_ makes the start label globally accessible.

##### Move and load
The _MOV_ instruction moves a value from the source register to the destination register. The syntax is:
```armasm
MOV <destination register>, <source register> or <value>
```
The _LDR_ instruction loads a value from a memory address to the destination register: 
```armasm
LDR <destination register>, [<register where an address is stored>]
```

A value can be a number or a label. The value is stored in the destination register. If it is a number, it must be preceded by a #. So the first instructions can be:
```armasm
.global _start
_start:
    MOV r0, #30         ; move the decimal value 30 to register r0 
    MOV r1, #0x1F       ; move the hex value 0x1F (31 decimal) to register r1
    MOV r2, r0          ; move the value from register r0 in register r2
    MOV r3, 0x20ffab12  ; store a specific memory address in register r3
    LDR r4, [r3]        ; go to the address that is stored in r3 and load the value that is found there   into r4
```

##### Comments
Comments are used to explain the code. They are ignored by the assembler and therefore not executed by the CPU. The syntax for comments in assembly is:
```armasm
; <comment>
```

Unfortunately, the CPUlator emulator can't handle comments in this style, so for CPUlator, the comments are written in C style (_//_):
```armasm
// <comment>
```
Note that this won't be recognized by any ARM assembler in the real world.

##### End the program
To end the program, we need to make a system call to let the operating system know that the program has finished. The syntax for a system call is:
```armasm
MOV r7, <system call number>  ; move the system call number to the r7 register. The system call number for exit is 1.
SWI <interrupt number>        ; make the system call by interrupting the CPU (SWI = software interrupt).
```
When the OS receives the interrupt, it looks at the r7 register to see which system call was made. In this case, it is the exit system call (1), so the OS knows that the program has finished and can free the memory that was allocated for the program. In the emulator, software interrupts are not supported, but in later real-world use, this is how a program is finished.

##### Addressing modes
There are different ways to address the memory. The most common ones are:

**immediate addressing**: the value is stored in the instruction itself
```armasm
MOV r0, #30 ; move the decimal value 30 to the r0 register
```
**register direct addressing**: the value is stored in a register
```armasm
MOV r0, r1 ; move the value in the r1 register to the r0 register
```
**register indirect addressing**: the value is stored in the memory address that is stored in a register
```armasm
LDR r0, [r1] ; load the value in the memory address that is stored in the r1 register to the r0 register
```

##### Arithmetic operations
The most basic arithmetic operations (addition, subtraction, multiplication) are very easy to use in ARM:
```armasm
ADD r2, r0, r1 ; add r0 and r1 and store the value in r2
SUB r2, r0, r1 ; r2 = r0 - r1
MUL r2, r0, r1 ; r2 = r0 * r1
```
There's no division here because divisions can lead to floating point numbers that are difficult to handle. We won't cover operations on floating point numbers in this MON.

##### CPSR register
Negative numbers are stored as 2's complement, so -1 is stored as ffffff. But the computer doesn't know if _ffffff_ is a representing a negative number (-1) or a huge positive number (16777215). To solve this, the CPSR register is used. Each bit in this register has a special purpose. The MSB (most significant bit) is the _N_ bit. If it is set to 1, it indicates that the last operation returned a negative value. Similarly, the carry bit and the overflow bit of the CPSR are used.

{% attention %}
To use the CPSR register, the suffix "S" must be appended to the mnemonic (use _SUBS_ instead of _SUB_, _MULS_ instead of _MUL_, ...). Else, the CPSR won't be used.
{% endattention %}

Example: 
```armasm
SUBS r2, r0, r1   ; r2 = r0-r1 and the "negative" bit in CPSR is set if r1<r0.
```
Another bit in CPSR is the _carry_ bit that indicates if a carry took place, e.g. when the operation returns a value bigger than the register can hold. For that, a slightly different add-operation is needed:
```armasm
ADCS r2, r0, r1 ; ADCS = "add with carry and use the cpsr register" - r2 = r0+r1+carry
```

##### Logical operations
**AND**
The AND operation iterates through every pair of bits A and B and returns a binary value X based on this table:
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

In ARM assembly, it works as following:
```armasm
AND r2, r0, r1 ; bitwise AND between r0 and r1, stored in r2
```

**OR**
The OR operation iterates through every pair of bits A and B and returns a binary value X based on this table:
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

In ARM assembly, it works as following:
```armasm
ORR r2, r0, r1 ; bitwise OR between r0 and r1, stored in r2
```
(Yes, _ORR_ is the right instruction)

**XOR**
The exclusive OR (XOR) operation iterates through every pair of bits A and B and returns a binary value X based on this table:
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

In ARM assembly, it works as following:
```armasm
EOR r2, r0, r1 ; bitwise XOR between r0 and r1, stored in r2 - the instruction is eor, not xor
```

**Logical shift**
Logical shifts are operations to shift bits of a register. The [official documentation](https://developer.arm.com/documentation/dui0068/b/Thumb-Instruction-Reference/Thumb-general-data-processing-instructions/ASR--LSL--LSR--and-ROR) explains each one in greater detail than I do here.
- **lsl**: "Logical shift to left" - move bits in the given register to the left. This equals a multiplication by two, but is much more efficient. The MSB gets dropped.
- **lsr**: "Logical shift to the right" - move bits in the given register to the right. This equals a division by two, but is much more efficient. The LSB gets dropped.
- **ror**: "Rotation to right" - Like the _lsr_ instruction, but the LSB doesn't get dropped, it is re-appended as MSB. There is no _rol_ instruction to rotate to left, but if you execute the _ror_ instruction 32-n times (n being the number of rotations to left), it has the same effect. 

In ARM assembly, it works as following:
```armasm
LSL r1, r0, #1 ; do one lsl on r0 and store the result in r1
LSR r0, r0, #5 ; do lsr 5 times on r0 and store it back in r0
ROR r0, r0, #1 ; do one ror on r0
```

##### Conditions
**Branching**
Conditions and branches are the equivalent to _if-else_-statements in higher level languages. In ARM assembly, we do a "compare" (CMP) instruction between two values/registers and after that, we can jump to different locations using branches.
```armasm
.global _start
_start:
  ; fill some values in r0 and r1
  MOV r0,#1
  MOV r1,#2

  CMP r0,r1   ; compare r0 and r1
  BGT greater ; if CMP revealed that R0 is greater than R1 -> go to "greater" label
  BAL default ; branch always (avoids stepping into "greater" after the execution of the last instruction) to the "default" label

greater:
	MOV r2, #0xff
	
default:
	MOV r2, #0xaa
```
The following branch instructions are available:
- **BGT** - greater than
- **BGE** - greater than or equal
- **BLT** - less than
- **BLE** - less than or equal
- **BEQ** - equal
- **BNE** - not equal
- **BAL** - always

**Looping**
By using the branches, we can implement loops like _for_ or _while_-loops in higher-level languages. In this example, we load a list with the values from 1-10 in the variable _list_ and then we iterate through all values until we reach the end of the list:
```armasm
.global _start
.equ endlist, 0xaaaaaaaa ; memory after the list

_start:
	LDR R3,=endlist	; load the value of "endlist" in R3
	LDR R0,=list	  ; load address of list in R0
	LDR R1, [R0] 	  ; load the first value of the list in R1
	ADD R2, R2, R1	; add R1 to R2 (R2 = R2 + R1)

loop:
	LDR R1,[R0,#4]!	; store the next value in list in R1
	CMP R1, R3		  ; check if this value equals the "endlist" value 
	BEQ exit 		    ; if this is the case: go to "exit" label
	ADD R2,R2, R1	  ; else: add r1 to r2
	BAL loop 		    ; goto "loop" 
	
exit:
	MOV R4,#0xffffffff	; just a visual indication that we're in exit now	
	
.data
list:
	.word 1,2,3,4,5,6,7,8,9,10
	
```

**Conditional instruction execution**
To make matters simpler, instead of branching, we can use conditional instructions to execute the instruction only if a condition is met. Almost every instruction in ARM assembly can be modified so that it only gets executed if a condition is met.
This happens by exchanging the "B" in the conditional branches with the instruction, e.g. _BLT_ (branch if less then) becomes _MOVLT_ (move if less then) or _BEQ_ (branch if equal) becomes _ADDEQ_ (add if equal).
Example:
```armasm
MOV R0,#2
MOV R1,#5

CMP R0,R1
ADDLT R2,#1   ; add 1 to R2 if the comparison returns that R0 is less than R1.
MOVEQ R2,R0   ; move the value of R0 to R2 if R0=R1
```

##### Functions
Simple functions in ARM assembly can be easily implemented with the known concepts of branching. If we use _BL_ to branch (instead of _BAL_), the location of the instruction that follows the branch is being stored in the link register, so after the function is executed, if we branch back with _BX_, the program jumps to this address and continues execution after the branch:
```armasm
  MOV R0,#2
  MOV R1,#5
  BL myfunc     ; branch to "myfunc"
  MOV R3, #0xff

myfunc:
  ADD R2, R0, R1
  BR lr         ; branch back to the address stored in the link register
```

**Push and Pop**
If we want to preserve the register values, but we need the registers else (e.g. for executing a function), we can store the current registers to the stack and read them back from the stack to the registers afterwards. This is done by using _PUSH_ and _POP_.
```armasm
_start:
  MOV R0,#2
  MOV R1,#5
  PUSH {R0, R1}   ; store R0 and R1 on the stack
  BL myfunc       ; branch to "myfunc"
  POP {R0, R1}    ; R0 and R1 get restored from the stack
  MOV R3, #0xff
  B end           ; branch to "end" to avoid jumping into myfunc

myfunc:
  ADD R0, R0, R1  ; R0 gets overwritten in the function
  MOV R3, R0      ; store the value of R0 in R3
  BR lr           ; branch back to the address stored in the link register

end:
; do nothing
```
Note that the stack is a LIFO (last in first out) architecture, so the data that is pushed last needs to be popped from the stack first.

## Useful resources
### Tutorials
- https://www.youtube.com/watch?v=gfmRrPjnEw4 (2:30:00 freeCodeCamp tutorial on ARM assembly)
- https://azeria-labs.com/writing-arm-assembly-part-1/ (tutorial on ARM assembly)
- [Larry Pyeatt: Modern Assembly Language Programming with the ARM Processor](https://www.amazon.com/Modern-Assembly-Language-Programming-Processor/dp/0128036982) (great book on ARM assembly)

### Tools
- https://cpulator.01xz.net/?sys=arm-de1soc (online ARM emulator)
- https://defuse.ca/online-x86-assembler.htm (online x86 assembler/disassembler)

### Other resources
- ARM Developer Suite Assembler Guide: https://developer.arm.com/documentation/dui0068/b (main documentation for ARM assembly)
- Ben Eater - "Build a 6502 computer from scratch": https://youtube.com/playlist?list=PLowKtXNTBypFbtuVMUVXNR0z1mu7dp7eH
This is a YouTube series in which a computer is built from a microcontroller, every step is explained. It is very entertaining and educating at the same time
