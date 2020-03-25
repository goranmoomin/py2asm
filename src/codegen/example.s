.section __TEXT,__text
.globl _main
_main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	callq _input
	movq %rax, -4(%rbp)
	movq -4(%rbp), %rax
	negq %rax
	movq %rax, -8(%rbp)
	movq -8(%rbp), %rax
	movq $2, %rbx
	addq %rbx, %rax
	movq %rax, -12(%rbp)
	movq %rax, %rdi
	callq _print_int_nl
	addq $4, %rsp
	movq $0, %rax
	leave
	retq
