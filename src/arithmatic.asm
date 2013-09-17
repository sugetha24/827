global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
a:	 dd	1.0
b:	 dd	5.5
SECTION .bss
z1:    resd    1
c:	resd	1
SECTION .text

main:	
push ebp
mov ebp, esp
fld	dword [a]
fld	dword [b]
fsubp	st1,st0
sub	esp,8
fstp	qword [esp]
push	formatr
call	printf
add	esp,12
mov esp, ebp
pop dword ebp
ret

