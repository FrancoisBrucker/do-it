---
layout: layout/post.njk

title: "MON 2.2 - Langage assembleur"
authors:
  - Kasimir Romer

tags: ['assembler', 'reverse engineering', 'arm', 'x86']
---
<!-- Début Résumé -->
TODO resume
Assembly language (x86, ARM, ...) (+ peut-être reverse engineering avec gdb, radare2 et Ghidra)
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
In order to follow this MON (or any tutorials on assembly programming), you should have basic knowledge of computer architecture and programming. You should at least:
- Understand the basic concepts of a computer (CPU, memory, input/output, ...)
- Being familiar with binary and hexadecimal numbers
- Know at least the basics of one high-level programming language like C++ or Java

For a deeper understanding of machine language and compilers, see the [MON of Jean-Baptiste](../../JBD/Mes_MON/compilateur) (but that's not necessary for understanding this MON)
{% endprerequis %}

### What is assembly language?
Assembly language is a very low-level programming language. It is being translated to machine code (binary code executed by the CPU) by an assembler. Because it is so hardware-near, it is very fast and efficient. However, it is harder to read and write than high-level languages like C++ or Java, that's why it only used in few use cases nowadays.

### Use cases of assembly language
Assembly language is nowadays mostly used in **embedded systems** like microcontrollers, where the hardware is very limited (in terms of memory and processing power), so the performance of the code is very important. Because assembly language is hardware-near, it is used in cases where hardware-specific functions need to be used. Additionally, assembly language is used in **reverse engineering** to understand how a program works. The code recovered from a program can be disassembled to assembly language and then analyzed.
Besides those use cases, it is great to learn assembly language in order to **understand the architecture of a computer** with its CPU, registers, memory and I/O. It is also useful to understand how a program works in general and how it is executed by the CPU. This permets better software development and debugging, e.g. by knowing potential for optimizing or better securing the software.
Other special use cases are **OS and driver development** because some of the functions in those area can't be implemented in high-level languages. Assembly language is used unknowingly by many programs, because the compiler that compiles high-level languages (C and C++ code) **generates assembly code**.

### Differences of different assembly languages (x86, ARM, ...)
There is no single "assembly language" because the instruction set of every CPU varies and therefore the language to control those instructions also varies. This means that every CPU has its own assembly language, but as they are very similar, it is possible to learn one assembly language and then learn the others relatively quickly. They share big parts of the syntax, so one can adapt quickly to a new assembly language if he needs to program for a different CPU. Nowadays, mainly two families of CPUs, and thus two families of assembly language, are used: x86 and ARM.

#### x86
The x86 family is used in most **desktop computers**. The CPUs of the x86 family use a **CISC (complex instruction set computer)** architecture. CISC CPUs have a larger, more complex instruction set with many specialized instructions for a variety of tasks. This allows them to perform a wider range of functions, but at the cost of slower execution times and increased complexity in the CPU. Because the instruction set is so complex, it is not easy to learn x86 assembly. The most well-known CPUs of this family are the Intel Core i3, i5 and i7 CPUs and the AMD Ryzen CPUs, so assumingly it is the CPU that is used in the computer you are using to read this MON at the moment.

#### ARM
The instruction set of the ARM CPU family is much simpler because it uses a **RISC (reduced instruction set computer)** architecture. RISC CPUs have a small, fixed instruction set with a limited number of instructions that can be executed quickly. This reduces the complexity of the CPU and allows it to execute instructions more quickly, at the cost of some flexibility. However, some instructions that can be executed in one step on a CISC CPU need multiple steps on a RISC CPU. ARM CPUs are used in most **mobile devices and embedded systems**. The most common CPUs of this family are the Apple A-series CPUs like the A15 Bionic which is used in the iPhone 14 and the Qualcomm Snapdragon CPUs like the Snapdragon 888 which is used in the Samsung Galaxy S21. In many embedded systems, ARM Cortex CPUs are used like the Cortex-M4 which is used in the popular STM32F4 microcontroller. ARM also spreads into the feld where x86 is dominating, e.g. with the Apple M2 chip which is used in the newest MacBook Air and the MacBook Pro and is considered extremely energy-efficient while still being very powerful. This shows that ARM will get even more relevant in the near future and could replace the x86 architecture in many domains.

## Assembly language for ARM
I start my learning journey with the book "Modern Assembly Language Programming with the ARM Processor" by Larry D. Pyeatt. Because it is over 500 pages long, I won't cover all of it and instead follow the tutorial by freeCodeCamp on [youtube](https://www.youtube.com/watch?v=gfmRrPjnEw4) which covers ARM assembly. Additionally, I will follow the tutorial on [azeria-labs.com](https://azeria-labs.com/writing-arm-assembly-part-1/) because it sets the foundation for following courses on exploit development for ARM which is an interesting topic in cybersecurity.

### Running ARM assembly code
To use the ARM assembly language, you need a device containing an ARM (micro)chip where the assembled code is stored and executed. For example, the _Raspberry Pi 4 Model B_, the current version of the Raspberry Pi computer, uses a Broadcomm BCM2711 SoC (system-on-a-chip) that includes the Cortex A-72 ARM chip as CPU. This means that you can use the ARM assembly language directly on the Raspberry Pi to get a real-world experience and direct hardware integration, e.g. you can blink the onboard LED etc.

If you don't have access to a ARM chip, an emulator can be used. The advantage is that you can inspect the whole memory at every given time, easily understand changes that the program makes to the memory, and that you don't need to flash the device with the new code after every change that is made in the code. You can find an online ARM emulator [here](https://cpulator.01xz.net/?sys=arm-de1soc).

In this MON, I will mainly use the emulator to write and execute the assembly code. Maybe later, I will test it also with the Raspberry Pi 4 that is laying around in my room.

### ARM assembly basics
#### Registers
Registers are the closest memory to the CPU. It is a small amount of memory that is directly accessible by the CPU, thus the CPU can read and write to the registers very quickly. One register can store data of the length of one word. A word is a fixed amount of bits that can be stored in a register. The amount of bits depends on the CPU, for example, the ARM Cortex-M4 CPU uses 32-bit words, so one word is 32 bits long and therefore a register can store 32 bits.

Some of those registers are general purpose registers (e.g. r0-r6) and some of them are special purpose registers:
- r7: used for system calls
- the program counter (PC): stores the address of the next instruction to be executed
- the stack pointer (SP): stores the address of the top of the stack
- the link register (LR): stores the address of the next instruction to be executed after a function call
- the program status registers (SPSR and CPSR): CPSR stores of the current program (e.g. CPU mode, interrupt mask, overflow flag, carry flag, zero flag, negative flag), SPSR records the pre-exception value of the CPSR.
- and more, that will be described later when they are necessary

#### Instructions
##### Entry point
The emulator automatically inserts the first two lines automatically:
```armasm
.global _start
_start:
```
_\_start:_ is a label that is used to divide the code into segments. If we go to a label, we execute the code below this label. _.global_ makes the start label globally accessible.

##### Move
The _mov_ instruction moves a value from the source register to the destination register. It doesn't matter if the instructions are in upper or lower case.
The syntax is:
```armasm
mov <destination register>, <source register> or <value>
```
A value can be a number or a label. The value is stored in the destination register. If it is a number, it must be preceded by a #. So the first instruction is:
```armasm
.global _start
_start:
    mov r0, #30 ; move the decimal value 30 to the r0 register
    mov r1, #0x1F ; move the hex value 0x1F (31 decimal) to the r1 register
```

##### Comments
Comments are used to explain the code. They are ignored by the assembler and therefore not executed by the CPU. The syntax for comments in assembly is:
```armasm
; <comment>
```

In the CPUlator emulator, however, comments are written in C style _//_:
```armasm
// <comment>
```

##### End the program
To end the program, we need to make a system call to let the operating system know that the program has finished. The syntax for a system call is:
```armasm
mov r7, <system call number>  ; move the system call number to the r7 register. The system call number for the exit system call is 1
swi <interrupt number>        ; make the system call by interrupting the CPU (swi = software interrupt).
```
When the OS receives the interrupt, it looks at the r7 register to see which system call was made. In this case, it is the exit system call (1), so the OS knows that the program has finished and can free the memory that was allocated for the program. In the emulator, software interrupts are not supported, but in later real-world use, this is how a program is finished.

##### Adressing modes
There are different ways to address the memory. The most common ones are:

**immediate addressing**: the value is stored in the instruction itself
```armasm
mov r0, #30 ; move the decimal value 30 to the r0 register
```
**register direct addressing**: the value is stored in a register
```armasm
mov r0, r1 ; move the value in the r1 register to the r0 register
```
**register indirect addressing**: the value is stored in the memory address that is stored in a register
```armasm
ldr r0, [r1] ; load the value in the memory address that is stored in the r1 register to the r0 register
```

##### Arithmetic operations
```armasm
add r2, r0, r1 ; add r0 and r1 and store the value in r2
sub r2, r0, r1 ; r2 = r0 - r1
mul r2, r0, r1 ; r2 = r0 * r1
```

##### CPSR register
Negative numbers are stored as 2's complement, so -1 is stored as ffffff. But the computer doesn't know if _ffffff_ is a representing a negative number (-1) or a huge positive number (16777215). To solve this, the CPSR register is used. Each bit in this register has a special purpose. The MSB (most significant bit) is the _N_ bit. If it is set to 1, it indicates that the last operation returned a negative value.
```armasm
subs r2, r0, r1 ; the subs command is needed to include the cpsr register operation.
```
Another bit in CPSR is the _carry_ bit that indicates if a carry took place, e.g. when the operation returns a value bigger than the register can hold. For that, a slighly different add-operation is needed:
```armasm
adc r2, r0, r1 ; add carry: r2 = r0+r1+carry
```

##### Logical operations
49:30 dans le vidéo



## Assembly language for x86
I will not go into detail about x86 assembly language because it is not used in embedded systems and I will not use it in the future. However, I will show the key differences to ARM assembly language.

## Reverse engineering with gdb, radare2 and Ghidra (only if time permits)

## Useful resources
### Tutorials
- https://www.youtube.com/watch?v=gfmRrPjnEw4 (2:30:00 freeCodeCamp tutorial on ARM assembly)
- https://azeria-labs.com/writing-arm-assembly-part-1/ (tutorial on ARM assembly)

### Tools
- https://cpulator.01xz.net/?sys=arm-de1soc (online ARM emulator)
- https://defuse.ca/online-x86-assembler.htm (online x86 assembler/disassembler)

### Other resources
- https://youtube.com/playlist?list=PLowKtXNTBypFbtuVMUVXNR0z1mu7dp7eH (Ben Eater - "Build a 6502 computer from scratch" (youtube series in which a computer is built from a microcontroller, every step is explained - very entertaining and educating at the same time))
- Larry Pyeatt: Modern Assembly Language Programming with the ARM Processor (https://www.amazon.com/Modern-Assembly-Language-Programming-Processor/dp/0128036982) - great book on ARM assembly

### Sources
- chatGPT (https://chat.openai.com/)
- https://lioncash.github.io/ARMBook/the_apsr,_cpsr,_and_the_difference_between_them.html
