global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
i:	resd	1
j:	resd	1
temp:	resd	1
a:	resd	5
SECTION .text

main:	
push ebp
mov ebp, esp
mov	eax,0
imul	eax,4
mov	dword [a + eax],2
mov	eax,1
imul	eax,4
mov	dword [a + eax],-3
mov	eax,2
imul	eax,4
mov	dword [a + eax],4
mov	eax,3
imul	eax,4
mov	dword [a + eax],-51
mov	eax,4
imul	eax,4
mov	dword [a + eax],5
mov	dword [i],0
mov	dword [j],0
mov	eax,0
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,1
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,2
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,3
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,4
imul	eax,4
push	dword [a + eax]
push formati
call printf
L$1:	
L$2:	
mov	eax,[j]
imul	eax,4
mov	eax,[a + eax]
mov	ebx,eax
mov	eax,[j]
add	eax,1
mov	ecx,eax
mov	eax,ecx
imul	eax,4
mov	eax,[a + eax]
mov	esi,eax
cmp	ebx,esi
jl	L$3
mov	eax,[j]
imul	eax,4
mov	eax,[a + eax]
mov	ebx,eax
mov	dword [temp],ebx
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	eax,ebx
imul	eax,4
mov	eax,[a + eax]
mov	ecx,eax
mov	eax,[j]
imul	eax,4
mov	dword [a + eax],ecx
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	eax,ebx
imul	eax,4
mov	edx,[temp]
mov	dword [a + eax],edx
L$3:	
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	dword [j],ebx
mov	eax,4
sub	eax,[i]
mov	ebx,eax
cmp	[j],ebx
jl	L$2
mov	dword [j],0
mov	eax,[i]
add	eax,1
mov	ebx,eax
mov	dword [i],ebx
cmp	dword [i],5
jl	L$1
mov	eax,0
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,1
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,2
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,3
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov	eax,4
imul	eax,4
push	dword [a + eax]
push formati
call printf
mov esp, ebp
pop dword ebp
ret

