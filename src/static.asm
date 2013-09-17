global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
a:	resd	1
b:	resd	1
SECTION .text

change:	
push ebp
mov ebp, esp
mov	ebx,10
mov	dword [z1],10
mov	dword [b],20
push	dword [z1]
push formati
call printf
push	dword [b]
push formati
call printf
mov esp, ebp
pop dword ebp
ret
main:	
push ebp
mov ebp, esp
mov	dword [a],15
mov	dword [b],5
push	dword [a]
push formati
call printf
push	dword [b]
push formati
call printf
call	change
push	dword [a]
push formati
call printf
push	dword [b]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

