global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
a:	resd	1
SECTION .text

cvalue:	
push ebp
mov ebp, esp
pop	dword ebx
mov	ebx,15
mov	dword [z1],15
push	dword [z1]
push formati
call printf
mov esp, ebp
pop dword ebp
ret
main:	
push ebp
mov ebp, esp
mov	dword [a],10
push	dword [a]
push formati
call printf
call	cvalue
push	dword [a]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

