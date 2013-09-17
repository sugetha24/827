global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
a:	resd	1
SECTION .text

re:	
push ebp
mov ebp, esp
push	dword [a]
push formati
call printf
mov	eax,[a]
add	eax,1
mov	ebx,eax
mov	dword [a],ebx
cmp	dword [a],10
jge	L$1
call	re
L$1:	
mov esp, ebp
pop dword ebp
ret
main:	
push ebp
mov ebp, esp
mov	dword [a],0
call	re
push	dword [a]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

