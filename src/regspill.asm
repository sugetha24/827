global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
a:	resd	1
b:	resd	1
c:	resd	1
d:	resd	1
e:	resd	1
f:	resd	1
x:	resd	1
SECTION .text

main:	
push ebp
mov ebp, esp
mov	dword [a],1
mov	dword [b],2
mov	dword [c],3
mov	dword [d],4
mov	dword [e],5
mov	dword [f],5
mov	eax,[a]
add	eax,[b]
mov	ebx,eax
mov	eax,[c]
add	eax,[d]
mov	ecx,eax
mov	eax,ebx
add	eax,ecx
mov	esi,eax
mov	eax,[e]
add	eax,[f]
mov	ebx,eax
mov	eax,esi
add	eax,ebx
mov	ecx,eax
mov	eax,[a]
add	eax,[b]
mov	ebx,eax
mov	eax,[c]
add	eax,[d]
mov	esi,eax
mov	eax,ebx
add	eax,esi
mov	edi,eax
mov	eax,[e]
add	eax,[f]
mov	ebx,eax
mov	eax,edi
add	eax,ebx
mov	esi,eax
mov	eax,ecx
add	eax,esi
mov	ebx,eax
mov	dword [x],ebx
push	dword [x]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

