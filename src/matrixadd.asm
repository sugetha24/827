global main
extern printf
SECTION .data
formati:	db "%d",10,0,
formatr:	db "%f",10,0
SECTION .bss
z1:    resd    1
i:	resd	1
j:	resd	1
a:	resd	16
b:	resd	16
c:	resd	16
SECTION .text

main:	
push ebp
mov ebp, esp
mov	dword [i],0
mov	dword [j],0
L$1:	
L$2:	
mov	eax,[i]
imul	eax,4
mov	ebx,eax
mov	eax,ebx
add	eax,[j]
mov	ecx,eax
mov	eax,ecx
imul	eax,4
mov	dword [a + eax],1
mov	eax,[i]
imul	eax,4
mov	ebx,eax
mov	eax,ebx
add	eax,[j]
mov	ecx,eax
mov	eax,ecx
imul	eax,4
mov	dword [b + eax],2
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	dword [j],ebx
cmp	dword [j],4
jl	L$2
mov	dword [j],0
mov	eax,[i]
add	eax,1
mov	ebx,eax
mov	dword [i],ebx
cmp	dword [i],4
jl	L$1
mov	dword [i],0
mov	dword [j],0
L$5:	
L$6:	
mov	eax,[i]
imul	eax,4
mov	ebx,eax
mov	eax,ebx
add	eax,[j]
mov	ecx,eax
mov	eax,ecx
imul	eax,4
mov	eax,[a + eax]
mov	ebx,eax
mov	eax,[i]
imul	eax,4
mov	ecx,eax
mov	eax,ecx
add	eax,[j]
mov	esi,eax
mov	eax,esi
imul	eax,4
mov	eax,[b + eax]
mov	ecx,eax
mov	eax,ebx
add	eax,ecx
mov	esi,eax
mov	eax,[i]
imul	eax,4
mov	ebx,eax
mov	eax,ebx
add	eax,[j]
mov	ecx,eax
mov	eax,ecx
imul	eax,4
mov	dword [c + eax],esi
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	dword [j],ebx
cmp	dword [j],4
jl	L$6
mov	dword [j],0
mov	eax,[i]
add	eax,1
mov	ebx,eax
mov	dword [i],ebx
cmp	dword [i],4
jl	L$5
mov	dword [i],0
mov	dword [j],0
L$9:	
L$10:	
mov	eax,[i]
imul	eax,4
mov	ebx,eax
mov	eax,ebx
add	eax,[j]
mov	ecx,eax
mov	eax,ecx
imul	eax,4
push	dword [c + eax]
push formati
call printf
mov	eax,[j]
add	eax,1
mov	ebx,eax
mov	dword [j],ebx
cmp	dword [j],4
jl	L$10
mov	dword [j],0
mov	eax,[i]
add	eax,1
mov	ebx,eax
mov	dword [i],ebx
cmp	dword [i],4
jl	L$9
mov esp, ebp
pop dword ebp
ret

