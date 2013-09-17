global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
x:	resd	1
SECTION .text

call1:	
push ebp
mov ebp, esp
mov	dword [x],10
push	dword [x]
push formati
call printf
mov esp, ebp
pop dword ebp
ret
main:	
push ebp
mov ebp, esp
mov	dword [x],5
push	dword [x]
push formati
call printf
call	call1
push	dword [x]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

